"""Example application demonstrating all custom widgets and styling"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from src.ui.styles import get_stylesheet
from src.ui.widgets import (
    MessageBubble, UserItem, RoundedButton, StatusBadge,
    ChatHeaderFrame, AnimatedLabel, SeparatorLine
)


class WidgetExampleWindow(QMainWindow):
    """Example window showcasing all custom widgets"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NearMeet Widget Examples")
        self.setGeometry(100, 100, 1200, 800)
        
        # Apply modern stylesheet
        self.setStyleSheet(get_stylesheet("dark"))
        
        # Create example content
        self._create_examples()
        
    def _create_examples(self):
        """Create example tabs for each widget type"""
        tabs = QTabWidget()
        
        # Tab 1: MessageBubble Examples
        tabs.addTab(self._create_message_examples(), "Message Bubbles")
        
        # Tab 2: UserItem Examples
        tabs.addTab(self._create_user_examples(), "User Items")
        
        # Tab 3: Button Examples
        tabs.addTab(self._create_button_examples(), "Buttons")
        
        # Tab 4: Status Badge Examples
        tabs.addTab(self._create_badge_examples(), "Status Badges")
        
        # Tab 5: Other Widgets
        tabs.addTab(self._create_other_examples(), "Other Widgets")
        
        self.setCentralWidget(tabs)
    
    def _create_message_examples(self):
        """Create message bubble examples"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Header
        header = ChatHeaderFrame("Message Bubbles", "Chat message examples")
        layout.addWidget(header)
        
        layout.addWidget(SeparatorLine())
        
        # Scroll area for messages
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(12)
        
        # Example messages
        examples = [
            ("Alice", "Hello! How are you doing?", "14:30", False),
            ("You", "I'm doing great! How about you?", "14:31", True),
            ("Alice", "Pretty good! Working on some cool stuff 😊", "14:32", False),
            ("You", "That's awesome! Tell me more!", "14:33", True),
            ("Alice", "It's about building a modern chat app with PyQt6", "14:34", False),
            ("You", "Wow, that sounds interesting! I'd love to help.", "14:35", True),
        ]
        
        for sender, message, time, is_own in examples:
            bubble = MessageBubble(sender, message, time, is_own)
            scroll_layout.addWidget(bubble)
        
        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)
        
        return widget
    
    def _create_user_examples(self):
        """Create user item examples"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Header
        header = ChatHeaderFrame("User Items", "Online users with different statuses")
        layout.addWidget(header)
        
        layout.addWidget(SeparatorLine())
        
        # User examples
        users_frame = QFrame()
        users_layout = QVBoxLayout(users_frame)
        users_layout.setSpacing(8)
        
        examples = [
            ("Alice", "online"),
            ("Bob", "away"),
            ("Charlie", "offline"),
            ("Diana", "online"),
            ("Eve", "away"),
            ("Frank", "offline"),
            ("Grace", "online"),
        ]
        
        title = QFont()
        title.setBold(True)
        title.setPointSize(11)
        
        label = QFont("Arial", 11)
        label.setBold(True)
        
        for i, (name, status) in enumerate(examples):
            user = UserItem(name, status)
            # Optional: connect signal
            # user.clicked.connect(lambda n: print(f"Clicked: {n}"))
            users_layout.addWidget(user)
        
        users_layout.addStretch()
        layout.addWidget(users_frame)
        
        return widget
    
    def _create_button_examples(self):
        """Create button style examples"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Header
        header = ChatHeaderFrame("Button Styles", "RoundedButton with different styles")
        layout.addWidget(header)
        
        layout.addWidget(SeparatorLine())
        
        # Button examples
        button_frame = QFrame()
        button_layout = QVBoxLayout(button_frame)
        button_layout.setSpacing(12)
        button_layout.setContentsMargins(20, 20, 20, 20)
        
        # Primary button
        primary_section = QHBoxLayout()
        primary_section.addWidget(QFont().bold() and self._create_label("Primary Buttons") or None)
        primary_section.addStretch()
        
        btn1 = RoundedButton("Connect", style="primary")
        btn2 = RoundedButton("Submit", style="primary")
        btn3 = RoundedButton("Start Call", style="primary")
        btn3.setEnabled(False)  # Disabled state
        
        for btn in [btn1, btn2, btn3]:
            button_layout.addWidget(btn)
        
        button_layout.addWidget(SeparatorLine())
        
        # Success button
        btn4 = RoundedButton("Send", style="success")
        btn5 = RoundedButton("Confirm", style="success")
        
        for btn in [btn4, btn5]:
            button_layout.addWidget(btn)
        
        button_layout.addWidget(SeparatorLine())
        
        # Danger button
        btn6 = RoundedButton("Delete", style="danger")
        btn7 = RoundedButton("Disconnect", style="danger")
        
        for btn in [btn6, btn7]:
            button_layout.addWidget(btn)
        
        button_layout.addWidget(SeparatorLine())
        
        # Secondary button
        btn8 = RoundedButton("Cancel", style="secondary")
        btn9 = RoundedButton("Close", style="secondary")
        
        for btn in [btn8, btn9]:
            button_layout.addWidget(btn)
        
        button_layout.addStretch()
        layout.addWidget(button_frame)
        
        return widget
    
    def _create_badge_examples(self):
        """Create status badge examples"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Header
        header = ChatHeaderFrame("Status Badges", "Different status indicator styles")
        layout.addWidget(header)
        
        layout.addWidget(SeparatorLine())
        
        # Badge examples
        badge_frame = QFrame()
        badge_layout = QVBoxLayout(badge_frame)
        badge_layout.setSpacing(12)
        badge_layout.setContentsMargins(20, 20, 20, 20)
        
        # Success badges
        badge1 = StatusBadge("Connected", "success")
        badge2 = StatusBadge("Online", "success")
        
        for badge in [badge1, badge2]:
            badge_layout.addWidget(badge)
        
        badge_layout.addWidget(SeparatorLine())
        
        # Error badges
        badge3 = StatusBadge("Offline", "error")
        badge4 = StatusBadge("Connection Failed", "error")
        
        for badge in [badge3, badge4]:
            badge_layout.addWidget(badge)
        
        badge_layout.addWidget(SeparatorLine())
        
        # Warning badges
        badge5 = StatusBadge("Away", "warning")
        badge6 = StatusBadge("Low Connection", "warning")
        
        for badge in [badge5, badge6]:
            badge_layout.addWidget(badge)
        
        badge_layout.addWidget(SeparatorLine())
        
        # Info badges
        badge7 = StatusBadge("Synchronizing...", "info")
        badge8 = StatusBadge("Connected to server", "info")
        
        for badge in [badge7, badge8]:
            badge_layout.addWidget(badge)
        
        badge_layout.addStretch()
        layout.addWidget(badge_frame)
        
        return widget
    
    def _create_other_examples(self):
        """Create examples of other widgets"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Header
        header = ChatHeaderFrame("Other Widgets", "Separators and animated labels")
        layout.addWidget(header)
        
        layout.addWidget(SeparatorLine())
        
        # Examples
        content_frame = QFrame()
        content_layout = QVBoxLayout(content_frame)
        content_layout.setSpacing(16)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Animated Labels
        label1 = AnimatedLabel("Welcome to NearMeet!")
        label2 = AnimatedLabel("This is a fade-in animation demo")
        label3 = AnimatedLabel("Enjoy the modern UI!")
        
        for label in [label1, label2, label3]:
            content_layout.addWidget(label)
        
        content_layout.addWidget(SeparatorLine())
        
        # Different colored separators
        sep1 = SeparatorLine("#0078d4")  # Blue
        sep2 = SeparatorLine("#107c10")  # Green
        sep3 = SeparatorLine("#d13438")  # Red
        sep4 = SeparatorLine("#f7630c")  # Orange
        
        for sep in [sep1, sep2, sep3, sep4]:
            content_layout.addWidget(sep)
        
        content_layout.addStretch()
        layout.addWidget(content_frame)
        
        return widget
    
    def _create_label(self, text):
        """Create a label with proper styling"""
        from PyQt6.QtWidgets import QLabel
        label = QLabel(text)
        font = label.font()
        font.setPointSize(12)
        font.setBold(True)
        label.setFont(font)
        return label


def main():
    """Run the example application"""
    app = QApplication(sys.argv)
    window = WidgetExampleWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
