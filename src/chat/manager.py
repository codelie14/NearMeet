"""Chat manager for NearMeet"""

from typing import List, Optional, Callable
from datetime import datetime, timedelta
import threading

from src.chat.message import Message
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ChatManager:
    """Manages chat messages and conversations"""
    
    def __init__(self):
        """Initialize chat manager"""
        self.messages: List[Message] = []
        self.callbacks: List[Callable] = []
        self.lock = threading.Lock()
    
    def add_message(self, message: Message) -> None:
        """Add a message to chat"""
        with self.lock:
            self.messages.append(message)
            logger.debug(f"Message added from {message.sender}: {message.content[:50]}...")
            self._notify_callbacks(message)
    
    def get_messages(self, limit: int = None, offset: int = 0) -> List[Message]:
        """Get messages with optional limit and offset"""
        with self.lock:
            if limit:
                return self.messages[offset:offset + limit]
            return self.messages[offset:]
    
    def get_messages_from_user(self, username: str) -> List[Message]:
        """Get all messages from a specific user"""
        with self.lock:
            return [msg for msg in self.messages if msg.sender == username]
    
    def get_messages_after(self, timestamp: datetime) -> List[Message]:
        """Get messages after a specific timestamp"""
        with self.lock:
            return [msg for msg in self.messages if msg.timestamp > timestamp]
    
    def search_messages(self, keyword: str, case_sensitive: bool = False) -> List[Message]:
        """Search messages by keyword"""
        with self.lock:
            results = []
            for msg in self.messages:
                if case_sensitive:
                    if keyword in msg.content:
                        results.append(msg)
                else:
                    if keyword.lower() in msg.content.lower():
                        results.append(msg)
            return results
    
    def delete_message(self, message_id: str) -> bool:
        """Delete a message by ID"""
        with self.lock:
            for i, msg in enumerate(self.messages):
                if msg.message_id == message_id:
                    self.messages.pop(i)
                    logger.info(f"Message {message_id} deleted")
                    return True
            return False
    
    def edit_message(self, message_id: str, new_content: str) -> bool:
        """Edit a message"""
        with self.lock:
            for msg in self.messages:
                if msg.message_id == message_id:
                    msg.content = new_content
                    logger.info(f"Message {message_id} edited")
                    return True
            return False
    
    def add_reaction(self, message_id: str, emoji: str, username: str) -> bool:
        """Add a reaction to a message"""
        with self.lock:
            for msg in self.messages:
                if msg.message_id == message_id:
                    if emoji not in msg.reactions:
                        msg.reactions[emoji] = []
                    if username not in msg.reactions[emoji]:
                        msg.reactions[emoji].append(username)
                    return True
            return False
    
    def clear_messages(self) -> None:
        """Clear all messages"""
        with self.lock:
            self.messages.clear()
            logger.info("Chat cleared")
    
    def get_message_count(self) -> int:
        """Get total number of messages"""
        with self.lock:
            return len(self.messages)
    
    def register_callback(self, callback: Callable) -> None:
        """Register a callback function for new messages"""
        self.callbacks.append(callback)
    
    def unregister_callback(self, callback: Callable) -> None:
        """Unregister a callback function"""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
    
    def _notify_callbacks(self, message: Message) -> None:
        """Notify all registered callbacks"""
        for callback in self.callbacks:
            try:
                callback(message)
            except Exception as e:
                logger.error(f"Callback error: {e}", exc_info=True)
