"""Message formatting for NearMeet"""

from datetime import datetime
from src.chat.message import Message


class MessageFormatter:
    """Formats messages for display"""
    
    @staticmethod
    def format_timestamp(dt: datetime, format_str: str = "%H:%M:%S") -> str:
        """Format timestamp"""
        return dt.strftime(format_str)
    
    @staticmethod
    def format_message_for_display(message: Message) -> str:
        """Format message for display in UI"""
        timestamp = MessageFormatter.format_timestamp(message.timestamp)
        return f"[{timestamp}] {message.sender}: {message.content}"
    
    @staticmethod
    def format_message_for_storage(message: Message) -> dict:
        """Format message for storage in database"""
        return {
            "id": message.message_id,
            "sender": message.sender,
            "content": message.content,
            "timestamp": message.timestamp.isoformat(),
            "is_encrypted": message.is_encrypted,
            "attachments": message.attachments,
            "reply_to": message.reply_to,
            "reactions": message.reactions
        }
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
        """Truncate text if it exceeds max length"""
        if len(text) > max_length:
            return text[:max_length - len(suffix)] + suffix
        return text
    
    @staticmethod
    def escape_html(text: str) -> str:
        """Escape HTML characters in text"""
        return (text.replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;")
                   .replace('"', "&quot;")
                   .replace("'", "&#x27;"))
    
    @staticmethod
    def highlight_mentions(text: str, username: str) -> str:
        """Highlight mentions of a username in text"""
        return text.replace(f"@{username}", f"<b>@{username}</b>")
