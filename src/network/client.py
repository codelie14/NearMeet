"""Network client implementation"""

import socket
import threading
import json
from typing import Callable, Optional

from src.config import ClientConfig
from src.network.protocol import Protocol
from src.utils.logger import get_logger

logger = get_logger(__name__)


class Client:
    """TCP/IP Client for NearMeet"""
    
    def __init__(self, host: str, port: int):
        """Initialize client"""
        self.host = host
        self.port = port
        self.socket: Optional[socket.socket] = None
        self.connected = False
        self.message_handlers: list[Callable] = []
        self.receive_thread: Optional[threading.Thread] = None
    
    def connect(self) -> bool:
        """Connect to server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(ClientConfig.TIMEOUT)
            self.socket.connect((self.host, self.port))
            
            self.connected = True
            logger.info(f"Connected to server at {self.host}:{self.port}")
            
            # Send handshake
            handshake = Protocol.create_handshake()
            self.socket.sendall(handshake.encode('utf-8'))
            
            # Start receiving messages in a separate thread
            self.receive_thread = threading.Thread(
                target=self._receive_messages,
                daemon=True
            )
            self.receive_thread.start()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to server: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from server"""
        try:
            self.connected = False
            if self.socket:
                self.socket.close()
            logger.info("Disconnected from server")
        except Exception as e:
            logger.error(f"Error disconnecting: {e}")
    
    def send_message(self, message: str) -> bool:
        """Send a message to the server"""
        try:
            if not self.connected or not self.socket:
                logger.warning("Not connected to server")
                return False
            
            packed = Protocol.pack_message(message.encode('utf-8'))
            self.socket.sendall(packed)
            return True
            
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            return False
    
    def send_json(self, data: dict) -> bool:
        """Send a JSON message to the server"""
        try:
            json_str = json.dumps(data)
            return self.send_message(json_str)
        except Exception as e:
            logger.error(f"Error sending JSON: {e}")
            return False
    
    def _receive_messages(self):
        """Receive messages from server"""
        while self.connected:
            try:
                # Read header
                header = self.socket.recv(20)
                if not header:
                    break
                
                # Unpack message
                msg_id, payload = Protocol.unpack_message(header + b'')
                
                # Try to decode as JSON
                try:
                    message = json.loads(payload.decode('utf-8'))
                except:
                    message = payload.decode('utf-8')
                
                logger.debug(f"Received message: {message}")
                
                # Call registered handlers
                for handler in self.message_handlers:
                    try:
                        handler(message)
                    except Exception as e:
                        logger.error(f"Handler error: {e}")
                        
            except socket.timeout:
                # Timeout is normal, continue
                continue
            except Exception as e:
                if self.connected:
                    logger.error(f"Error receiving message: {e}")
                break
        
        self.connected = False
    
    def register_message_handler(self, handler: Callable):
        """Register a message handler function"""
        self.message_handlers.append(handler)
    
    def unregister_message_handler(self, handler: Callable):
        """Unregister a message handler function"""
        if handler in self.message_handlers:
            self.message_handlers.remove(handler)
    
    def is_connected(self) -> bool:
        """Check if connected to server"""
        return self.connected
