"""Message handling for NearMeet"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Message:
    """Message object"""
    sender: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    message_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_encrypted: bool = False
    attachments: list = field(default_factory=list)
    reply_to: Optional[str] = None
    reactions: dict = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "id": self.message_id,
            "sender": self.sender,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "is_encrypted": self.is_encrypted,
            "attachments": self.attachments,
            "reply_to": self.reply_to,
            "reactions": self.reactions
        }
    
    def __repr__(self) -> str:
        return f"Message(sender={self.sender}, content={self.content[:50]}..., timestamp={self.timestamp})"
