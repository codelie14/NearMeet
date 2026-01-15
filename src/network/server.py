"""Network server implementation"""

import socket
import threading
import json
from typing import Callable, Optional

from src.config import ServerConfig
from src.network.protocol import Protocol
from src.utils.logger import get_logger

logger = get_logger(__name__)


class Server:
    """TCP/IP Server for NearMeet"""
    
    def __init__(self, host: str = ServerConfig.HOST, port: int = ServerConfig.PORT):
        """Initialize server"""
        self.host = host
        self.port = port
        self.server_socket: Optional[socket.socket] = None
        self.running = False
        self.clients: dict = {}  # {client_address: client_socket}
        self.client_lock = threading.Lock()
        self.message_handlers: list[Callable] = []
    
    def start(self) -> bool:
        """Start the server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(ServerConfig.MAX_CLIENTS)
            
            self.running = True
            logger.info(f"Server started on {self.host}:{self.port}")
            
            # Start accepting connections in a separate thread
            threading.Thread(target=self._accept_connections, daemon=True).start()
            return True
            
        except Exception as e:
            logger.error(f"Failed to start server: {e}", exc_info=True)
            return False
    
    def stop(self):
        """Stop the server"""
        try:
            self.running = False
            
            # Close all client connections
            with self.client_lock:
                for client_socket in self.clients.values():
                    try:
                        client_socket.close()
                    except:
                        pass
                self.clients.clear()
            
            # Close server socket
            if self.server_socket:
                self.server_socket.close()
            
            logger.info("Server stopped")
            
        except Exception as e:
            logger.error(f"Error stopping server: {e}", exc_info=True)
    
    def _accept_connections(self):
        """Accept incoming client connections"""
        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                logger.info(f"New connection from {client_address}")
                
                with self.client_lock:
                    self.clients[client_address] = client_socket
                
                # Handle client in a separate thread
                threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, client_address),
                    daemon=True
                ).start()
                
            except Exception as e:
                if self.running:
                    logger.error(f"Error accepting connection: {e}")
    
    def _handle_client(self, client_socket: socket.socket, client_address: tuple):
        """Handle individual client connection"""
        try:
            # Receive initial handshake
            data = client_socket.recv(ServerConfig.BUFFER_SIZE)
            if not data:
                return
            
            # Parse and respond to handshake
            message = json.loads(data.decode('utf-8'))
            logger.debug(f"Handshake from {client_address}: {message}")
            
            # Send acknowledgment
            ack = Protocol.create_ack(0)
            client_socket.sendall(ack.encode('utf-8'))
            
            # Continue receiving messages
            while self.running:
                data = client_socket.recv(ServerConfig.BUFFER_SIZE)
                if not data:
                    break
                
                try:
                    # Try to unpack message
                    msg_id, payload = Protocol.unpack_message(data)
                    message = json.loads(payload.decode('utf-8'))
                    
                    logger.debug(f"Message from {client_address}: {message}")
                    
                    # Call registered handlers
                    for handler in self.message_handlers:
                        handler(client_address, message)
                    
                    # Send acknowledgment
                    ack = Protocol.create_ack(msg_id)
                    client_socket.sendall(ack.encode('utf-8'))
                    
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    
        except Exception as e:
            logger.error(f"Error handling client {client_address}: {e}")
        
        finally:
            # Remove client from list
            with self.client_lock:
                if client_address in self.clients:
                    del self.clients[client_address]
            
            try:
                client_socket.close()
            except:
                pass
            
            logger.info(f"Client disconnected: {client_address}")
    
    def broadcast_message(self, message: str, exclude_address: tuple = None):
        """Broadcast a message to all connected clients"""
        try:
            with self.client_lock:
                for address, client_socket in self.clients.items():
                    if exclude_address and address == exclude_address:
                        continue
                    
                    try:
                        client_socket.sendall(message.encode('utf-8'))
                    except Exception as e:
                        logger.error(f"Failed to send message to {address}: {e}")
        
        except Exception as e:
            logger.error(f"Error broadcasting message: {e}")
    
    def send_to_client(self, client_address: tuple, message: str) -> bool:
        """Send a message to a specific client"""
        try:
            with self.client_lock:
                if client_address in self.clients:
                    self.clients[client_address].sendall(message.encode('utf-8'))
                    return True
            return False
        
        except Exception as e:
            logger.error(f"Error sending message to {client_address}: {e}")
            return False
    
    def register_message_handler(self, handler: Callable):
        """Register a message handler function"""
        self.message_handlers.append(handler)
    
    def unregister_message_handler(self, handler: Callable):
        """Unregister a message handler function"""
        if handler in self.message_handlers:
            self.message_handlers.remove(handler)
    
    def get_client_count(self) -> int:
        """Get number of connected clients"""
        with self.client_lock:
            return len(self.clients)
    
    def get_connected_clients(self) -> list:
        """Get list of connected client addresses"""
        with self.client_lock:
            return list(self.clients.keys())
