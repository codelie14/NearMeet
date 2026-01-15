"""Tests for network module"""

import pytest
from src.network.server import Server
from src.network.client import Client
from src.network.protocol import Protocol, TextMessage
from src.utils.logger import setup_logging

setup_logging()


class TestProtocol:
    """Test Protocol class"""
    
    def test_pack_unpack_message(self):
        """Test packing and unpacking a message"""
        msg = TextMessage(sender="test", content="Hello")
        packed = Protocol.pack_message(msg.to_json().encode('utf-8'))
        
        msg_id, payload = Protocol.unpack_message(packed)
        assert msg_id == 0
        assert payload == msg.to_json().encode('utf-8')
    
    def test_create_handshake(self):
        """Test creating a handshake message"""
        handshake = Protocol.create_handshake()
        assert "HANDSHAKE" in handshake
        assert "protocol_version" in handshake
    
    def test_create_ack(self):
        """Test creating an acknowledgment"""
        ack = Protocol.create_ack(123)
        assert "ACK" in ack
        assert "message_id" in ack


class TestServer:
    """Test Server class"""
    
    def test_server_initialization(self):
        """Test server initialization"""
        server = Server(host="127.0.0.1", port=9999)
        assert server.host == "127.0.0.1"
        assert server.port == 9999
        assert not server.running
    
    def test_get_client_count(self):
        """Test getting client count"""
        server = Server(host="127.0.0.1", port=9999)
        assert server.get_client_count() == 0


class TestClient:
    """Test Client class"""
    
    def test_client_initialization(self):
        """Test client initialization"""
        client = Client(host="127.0.0.1", port=5000)
        assert client.host == "127.0.0.1"
        assert client.port == 5000
        assert not client.connected
    
    def test_is_connected(self):
        """Test connection status"""
        client = Client(host="127.0.0.1", port=5000)
        assert not client.is_connected()
