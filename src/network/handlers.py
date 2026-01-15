"""Network handlers for message processing"""

import json
from typing import Callable, Dict, Any

from src.utils.logger import get_logger

logger = get_logger(__name__)


class MessageHandler:
    """Handles different types of messages"""
    
    def __init__(self):
        """Initialize message handler"""
        self.handlers: Dict[str, Callable] = {}
    
    def register(self, message_type: str, handler: Callable):
        """Register a handler for a message type"""
        self.handlers[message_type] = handler
        logger.debug(f"Handler registered for message type: {message_type}")
    
    def unregister(self, message_type: str):
        """Unregister a handler for a message type"""
        if message_type in self.handlers:
            del self.handlers[message_type]
            logger.debug(f"Handler unregistered for message type: {message_type}")
    
    def handle(self, message: Dict[str, Any]) -> Any:
        """Handle a message"""
        try:
            message_type = message.get("type") or message.get("message_type")
            
            if not message_type:
                logger.warning(f"Message type not found in: {message}")
                return None
            
            handler = self.handlers.get(message_type)
            
            if not handler:
                logger.warning(f"No handler found for message type: {message_type}")
                return None
            
            return handler(message)
            
        except Exception as e:
            logger.error(f"Error handling message: {e}", exc_info=True)
            return None
    
    def get_handler(self, message_type: str) -> Callable:
        """Get handler for a message type"""
        return self.handlers.get(message_type)


# Global message handler instance
_message_handler = MessageHandler()


def get_message_handler() -> MessageHandler:
    """Get the global message handler"""
    return _message_handler


def setup_default_handlers(handler: MessageHandler):
    """Setup default message handlers"""
    
    def handle_text(message: Dict[str, Any]):
        """Handle text message"""
        logger.debug(f"Text message from {message.get('sender')}: {message.get('content')}")
        return {"status": "received", "message_id": message.get("message_id")}
    
    def handle_ack(message: Dict[str, Any]):
        """Handle acknowledgment"""
        logger.debug(f"ACK received for message {message.get('message_id')}")
        return None
    
    def handle_heartbeat(message: Dict[str, Any]):
        """Handle heartbeat"""
        return {"type": "HEARTBEAT_ACK"}
    
    handler.register("TEXT", handle_text)
    handler.register("ACK", handle_ack)
    handler.register("HEARTBEAT", handle_heartbeat)
