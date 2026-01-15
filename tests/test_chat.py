"""Tests for chat module"""

import pytest
from src.chat.manager import ChatManager
from src.chat.message import Message
from datetime import datetime


class TestMessage:
    """Test Message class"""
    
    def test_message_creation(self):
        """Test creating a message"""
        msg = Message(sender="john", content="Hello world")
        assert msg.sender == "john"
        assert msg.content == "Hello world"
        assert msg.message_id is not None
        assert isinstance(msg.timestamp, datetime)
    
    def test_message_to_dict(self):
        """Test converting message to dict"""
        msg = Message(sender="john", content="Hello")
        data = msg.to_dict()
        
        assert data["sender"] == "john"
        assert data["content"] == "Hello"
        assert "id" in data
        assert "timestamp" in data


class TestChatManager:
    """Test ChatManager class"""
    
    def setup_method(self):
        """Setup for each test"""
        self.manager = ChatManager()
    
    def test_add_message(self):
        """Test adding a message"""
        msg = Message(sender="john", content="Hello")
        self.manager.add_message(msg)
        
        assert self.manager.get_message_count() == 1
    
    def test_get_messages(self):
        """Test getting messages"""
        msg1 = Message(sender="john", content="First")
        msg2 = Message(sender="jane", content="Second")
        
        self.manager.add_message(msg1)
        self.manager.add_message(msg2)
        
        messages = self.manager.get_messages()
        assert len(messages) == 2
    
    def test_get_messages_with_limit(self):
        """Test getting messages with limit"""
        for i in range(5):
            msg = Message(sender="user", content=f"Message {i}")
            self.manager.add_message(msg)
        
        messages = self.manager.get_messages(limit=2)
        assert len(messages) == 2
    
    def test_search_messages(self):
        """Test searching messages"""
        msg1 = Message(sender="john", content="Hello world")
        msg2 = Message(sender="jane", content="Goodbye")
        
        self.manager.add_message(msg1)
        self.manager.add_message(msg2)
        
        results = self.manager.search_messages("Hello")
        assert len(results) == 1
        assert results[0].content == "Hello world"
    
    def test_search_messages_case_insensitive(self):
        """Test case-insensitive search"""
        msg = Message(sender="john", content="HELLO")
        self.manager.add_message(msg)
        
        results = self.manager.search_messages("hello")
        assert len(results) == 1
    
    def test_delete_message(self):
        """Test deleting a message"""
        msg = Message(sender="john", content="To delete")
        self.manager.add_message(msg)
        
        assert self.manager.get_message_count() == 1
        
        deleted = self.manager.delete_message(msg.message_id)
        assert deleted
        assert self.manager.get_message_count() == 0
    
    def test_get_messages_from_user(self):
        """Test getting messages from a specific user"""
        msg1 = Message(sender="john", content="John's message")
        msg2 = Message(sender="jane", content="Jane's message")
        msg3 = Message(sender="john", content="Another from john")
        
        self.manager.add_message(msg1)
        self.manager.add_message(msg2)
        self.manager.add_message(msg3)
        
        john_msgs = self.manager.get_messages_from_user("john")
        assert len(john_msgs) == 2
    
    def test_clear_messages(self):
        """Test clearing all messages"""
        msg1 = Message(sender="john", content="Message 1")
        msg2 = Message(sender="jane", content="Message 2")
        
        self.manager.add_message(msg1)
        self.manager.add_message(msg2)
        assert self.manager.get_message_count() == 2
        
        self.manager.clear_messages()
        assert self.manager.get_message_count() == 0
    
    def test_add_reaction(self):
        """Test adding a reaction to a message"""
        msg = Message(sender="john", content="Funny message")
        self.manager.add_message(msg)
        
        result = self.manager.add_reaction(msg.message_id, "😂", "jane")
        assert result
        assert "😂" in msg.reactions
        assert "jane" in msg.reactions["😂"]
    
    def test_callback_on_new_message(self):
        """Test callback on new message"""
        callback_called = []
        
        def test_callback(msg):
            callback_called.append(msg)
        
        self.manager.register_callback(test_callback)
        
        msg = Message(sender="john", content="Test")
        self.manager.add_message(msg)
        
        assert len(callback_called) == 1
        assert callback_called[0].content == "Test"
