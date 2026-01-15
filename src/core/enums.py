"""Enumerations for NearMeet application"""

from enum import Enum, auto


class MessageType(Enum):
    """Types of messages"""
    TEXT = auto()
    IMAGE = auto()
    FILE = auto()
    AUDIO = auto()
    VIDEO = auto()
    SYSTEM = auto()
    NOTIFICATION = auto()


class UserStatus(Enum):
    """User status"""
    ONLINE = "online"
    OFFLINE = "offline"
    AWAY = "away"
    BUSY = "busy"
    IDLE = "idle"


class ConnectionStatus(Enum):
    """Connection status"""
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    ERROR = "error"


class CallType(Enum):
    """Types of calls"""
    AUDIO = "audio"
    VIDEO = "video"
    SCREEN_SHARE = "screen_share"
    VOICE_MESSAGE = "voice_message"


class CallStatus(Enum):
    """Call status"""
    IDLE = "idle"
    RINGING = "ringing"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    ENDED = "ended"
    REJECTED = "rejected"
    MISSED = "missed"


class EventType(Enum):
    """Event types for the application"""
    MESSAGE_SENT = auto()
    MESSAGE_RECEIVED = auto()
    USER_JOINED = auto()
    USER_LEFT = auto()
    USER_STATUS_CHANGED = auto()
    CALL_INITIATED = auto()
    CALL_ENDED = auto()
    FILE_TRANSFER_STARTED = auto()
    FILE_TRANSFER_COMPLETED = auto()
    FILE_TRANSFER_FAILED = auto()
    ERROR = auto()


class LogLevel(Enum):
    """Log levels"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
