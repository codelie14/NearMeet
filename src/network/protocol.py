"""Communication protocol definitions for NearMeet"""

import json
import struct
from typing import Dict, Any, Union
from dataclasses import dataclass, asdict
from datetime import datetime

from src.core.enums import MessageType, CallType


PROTOCOL_VERSION = 1
MAGIC_NUMBER = b"NEAR"
MESSAGE_HEADER_SIZE = 20  # bytes


@dataclass
class Message:
    """Base message structure"""
    sender: str
    timestamp: str
    message_type: str
    content: Dict[str, Any]
    message_id: str = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        data = asdict(self)
        return data
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_json(cls, json_str: str):
        """Create message from JSON string"""
        data = json.loads(json_str)
        return cls(**data)


@dataclass
class TextMessage(Message):
    """Text message"""
    def __init__(self, sender: str, content: str, message_id: str = None):
        super().__init__(
            sender=sender,
            timestamp=datetime.now().isoformat(),
            message_type=MessageType.TEXT.name,
            content={"text": content},
            message_id=message_id
        )


@dataclass
class CallMessage(Message):
    """Call message"""
    def __init__(self, sender: str, call_type: str, action: str, target: str = None, 
                 message_id: str = None):
        super().__init__(
            sender=sender,
            timestamp=datetime.now().isoformat(),
            message_type="CALL",
            content={
                "call_type": call_type,
                "action": action,  # initiate, accept, reject, end
                "target": target
            },
            message_id=message_id
        )


@dataclass
class FileMessage(Message):
    """File transfer message"""
    def __init__(self, sender: str, filename: str, filesize: int, 
                 checksum: str = None, message_id: str = None):
        super().__init__(
            sender=sender,
            timestamp=datetime.now().isoformat(),
            message_type=MessageType.FILE.name,
            content={
                "filename": filename,
                "filesize": filesize,
                "checksum": checksum
            },
            message_id=message_id
        )


class Protocol:
    """Network protocol handler"""
    
    @staticmethod
    def pack_message(message: Union[Message, bytes], message_id: int = 0) -> bytes:
        """
        Pack a message with header for transmission
        
        Format:
        - Magic number (4 bytes): b"NEAR"
        - Version (1 byte)
        - Message ID (4 bytes)
        - Payload size (4 bytes)
        - Reserved (7 bytes)
        - Payload (variable)
        """
        if isinstance(message, Message):
            payload = message.to_json().encode('utf-8')
        else:
            payload = message
        
        header = struct.pack(
            '>4sBI4s7s',
            MAGIC_NUMBER,
            PROTOCOL_VERSION,
            message_id,
            len(payload),
            b'\x00' * 7  # Reserved
        )
        
        return header + payload
    
    @staticmethod
    def unpack_message(data: bytes) -> tuple[int, bytes]:
        """
        Unpack a message from received data
        
        Returns:
            (message_id, payload)
        """
        if len(data) < MESSAGE_HEADER_SIZE:
            raise ValueError("Incomplete message header")
        
        header = data[:MESSAGE_HEADER_SIZE]
        payload = data[MESSAGE_HEADER_SIZE:]
        
        magic, version, msg_id, size, reserved = struct.unpack(
            '>4sBI4s7s',
            header
        )
        
        if magic != MAGIC_NUMBER:
            raise ValueError("Invalid magic number")
        
        if version != PROTOCOL_VERSION:
            raise ValueError(f"Unsupported protocol version: {version}")
        
        if len(payload) != size:
            raise ValueError(f"Payload size mismatch: expected {size}, got {len(payload)}")
        
        return msg_id, payload
    
    @staticmethod
    def create_handshake() -> str:
        """Create handshake message"""
        return json.dumps({
            "type": "HANDSHAKE",
            "protocol_version": PROTOCOL_VERSION,
            "timestamp": datetime.now().isoformat()
        })
    
    @staticmethod
    def create_ack(message_id: int) -> str:
        """Create acknowledgment message"""
        return json.dumps({
            "type": "ACK",
            "message_id": message_id,
            "timestamp": datetime.now().isoformat()
        })
    
    @staticmethod
    def create_heartbeat() -> str:
        """Create heartbeat message"""
        return json.dumps({
            "type": "HEARTBEAT",
            "timestamp": datetime.now().isoformat()
        })
