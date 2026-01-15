"""Tests for custom widgets and styling"""

import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from src.ui.widgets import (
    MessageBubble, UserItem, RoundedButton, StatusBadge,
    ChatHeaderFrame, AnimatedLabel, SeparatorLine
)
from src.ui.styles import get_stylesheet


@pytest.fixture
def qapp():
    """Fixture for QApplication"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestMessageBubble:
    """Test MessageBubble widget"""
    
    def test_creation(self, qapp):
        """Test bubble creation"""
        bubble = MessageBubble("Alice", "Hello!", "14:30", False)
        assert bubble.sender == "Alice"
        assert bubble.message == "Hello!"
        assert bubble.timestamp == "14:30"
        assert bubble.is_own == False
    
    def test_own_message(self, qapp):
        """Test own message flag"""
        bubble = MessageBubble("Me", "My message", is_own=True)
        assert bubble.is_own == True
    
    def test_widget_created(self, qapp):
        """Test widget is created properly"""
        bubble = MessageBubble("Bob", "Test message")
        assert bubble.minimumWidth() == 300
        assert bubble.maximumWidth() == 600


class TestUserItem:
    """Test UserItem widget"""
    
    def test_creation(self, qapp):
        """Test user item creation"""
        user = UserItem("Alice", "online")
        assert user.username == "Alice"
        assert user.status == "online"
    
    def test_status_variations(self, qapp):
        """Test different statuses"""
        for status in ["online", "offline", "away"]:
            user = UserItem("Test", status)
            assert user.status == status
    
    def test_click_signal(self, qapp):
        """Test click signal"""
        user = UserItem("Bob", "online")
        signal_received = []
        user.clicked.connect(lambda name: signal_received.append(name))
        user.mousePressEvent(None)
        assert signal_received == ["Bob"]


class TestRoundedButton:
    """Test RoundedButton widget"""
    
    def test_creation(self, qapp):
        """Test button creation"""
        btn = RoundedButton("Click me", style="primary")
        assert btn.text() == "Click me"
        assert btn.style == "primary"
    
    def test_button_styles(self, qapp):
        """Test different button styles"""
        styles = ["primary", "secondary", "danger", "success"]
        for style in styles:
            btn = RoundedButton("Test", style=style)
            assert btn.style == style
    
    def test_minimum_height(self, qapp):
        """Test button minimum height"""
        btn = RoundedButton("Test")
        assert btn.minimumHeight() == 36


class TestStatusBadge:
    """Test StatusBadge widget"""
    
    def test_creation(self, qapp):
        """Test badge creation"""
        badge = StatusBadge("Online", "success")
        assert badge.text == "Online"
        assert badge.status_type == "success"
    
    def test_badge_types(self, qapp):
        """Test different badge types"""
        types = ["info", "success", "warning", "error"]
        for badge_type in types:
            badge = StatusBadge("Test", badge_type)
            assert badge.status_type == badge_type


class TestChatHeaderFrame:
    """Test ChatHeaderFrame widget"""
    
    def test_creation(self, qapp):
        """Test header creation"""
        header = ChatHeaderFrame("Chat", "Connected")
        assert header is not None
    
    def test_minimum_height(self, qapp):
        """Test header minimum height"""
        header = ChatHeaderFrame()
        assert header.minimumHeight() == 60


class TestAnimatedLabel:
    """Test AnimatedLabel widget"""
    
    def test_creation(self, qapp):
        """Test animated label creation"""
        label = AnimatedLabel("Test")
        assert label.text() == "Test"
    
    def test_animation_duration(self, qapp):
        """Test animation duration"""
        label = AnimatedLabel("Test")
        assert label.animation.duration() == 500


class TestSeparatorLine:
    """Test SeparatorLine widget"""
    
    def test_creation(self, qapp):
        """Test separator creation"""
        sep = SeparatorLine()
        assert sep is not None
    
    def test_height(self, qapp):
        """Test separator height"""
        sep = SeparatorLine()
        assert sep.minimumHeight() == 1
        assert sep.maximumHeight() == 1
    
    def test_custom_color(self, qapp):
        """Test custom color"""
        sep = SeparatorLine("#FF0000")
        assert sep is not None


class TestStylesheet:
    """Test stylesheet loading"""
    
    def test_dark_theme(self):
        """Test dark theme stylesheet"""
        stylesheet = get_stylesheet("dark")
        assert isinstance(stylesheet, str)
        assert len(stylesheet) > 0
        assert "#1e1e1e" in stylesheet  # Dark background color
    
    def test_light_theme(self):
        """Test light theme stylesheet"""
        stylesheet = get_stylesheet("light")
        assert isinstance(stylesheet, str)
        assert len(stylesheet) > 0
        assert "#f3f3f3" in stylesheet  # Light background color
    
    def test_default_theme(self):
        """Test default theme is dark"""
        stylesheet = get_stylesheet()
        dark_stylesheet = get_stylesheet("dark")
        assert stylesheet == dark_stylesheet
    
    def test_stylesheet_content(self):
        """Test stylesheet has essential CSS"""
        stylesheet = get_stylesheet("dark")
        assert "QMainWindow" in stylesheet
        assert "QPushButton" in stylesheet
        assert "QLineEdit" in stylesheet
        assert "QTextEdit" in stylesheet


class TestWidgetIntegration:
    """Test widget integration"""
    
    def test_multiple_widgets(self, qapp):
        """Test multiple widgets together"""
        bubble1 = MessageBubble("Alice", "Hi!")
        bubble2 = MessageBubble("Bob", "Hello!", is_own=True)
        user1 = UserItem("Alice", "online")
        user2 = UserItem("Bob", "away")
        
        assert bubble1.sender == "Alice"
        assert bubble2.is_own == True
        assert user1.status == "online"
        assert user2.status == "away"
    
    def test_styling_application(self, qapp):
        """Test applying stylesheet"""
        stylesheet = get_stylesheet("dark")
        btn = RoundedButton("Test")
        btn.setStyleSheet(stylesheet)
        # Stylesheet should be applied without errors
        assert True
