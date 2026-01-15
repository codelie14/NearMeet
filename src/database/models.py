"""Database models for NearMeet"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class User:
    """User model"""
    username: str
    status: str = "offline"
    last_seen: datetime = None
    created_at: datetime = None
    profile_picture: Optional[bytes] = None


@dataclass
class MessageModel:
    """Message model for storage"""
    id: str
    sender: str
    content: str
    timestamp: datetime
    is_encrypted: bool = False
    attachments: List[str] = None
    reply_to: Optional[str] = None


@dataclass
class FileTransfer:
    """File transfer model"""
    id: str
    sender: str
    recipient: str
    filename: str
    filesize: int
    status: str  # pending, in_progress, completed, failed
    checksum: Optional[str] = None
    created_at: datetime = None
    completed_at: Optional[datetime] = None


@dataclass
class Session:
    """Session model"""
    id: str
    user_id: str
    token: str
    created_at: datetime
    expires_at: datetime
    ip_address: str
    is_active: bool = True
