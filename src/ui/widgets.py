"""Custom PyQt6 widgets for NearMeet"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QScrollArea, QListWidget, QListWidgetItem, QApplication
)
from PyQt6.QtCore import Qt, pyqtSignal, QPropertyAnimation, QSize, QEasingCurve
from PyQt6.QtGui import QColor, QFont, QIcon, QPixmap, QPalette
from datetime import datetime
from typing import Optional


class MessageBubble(QFrame):
    """Custom message bubble widget with styling"""
    
    def __init__(self, sender: str, message: str, timestamp: Optional[str] = None, is_own: bool = False):
        """
        Initialize message bubble.
        
        Args:
            sender: Sender username
            message: Message text
            timestamp: Message timestamp
            is_own: Whether this is the user's own message
        """
        super().__init__()
        self.sender = sender
        self.message = message
        self.timestamp = timestamp or datetime.now().strftime("%H:%M")
        self.is_own = is_own
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components"""
        self.setObjectName("chatMessage")
        self.setStyleSheet("""
            QFrame#chatMessage {
                background-color: #0078d4 if is_own else #252525;
                border-radius: 10px;
                padding: 10px;
                margin: 4px;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        
        # Sender name
        sender_label = QLabel(self.sender)
        sender_label.setObjectName("username")
        sender_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        layout.addWidget(sender_label)
        
        # Message text
        msg_label = QLabel(self.message)
        msg_label.setWordWrap(True)
        msg_label.setFont(QFont("Segoe UI", 10))
        msg_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(msg_label)
        
        # Timestamp
        time_label = QLabel(self.timestamp)
        time_label.setObjectName("timestamp")
        time_label.setStyleSheet("color: #a0a0a0; font-size: 9px;")
        time_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(time_label)
        
        self.setMinimumWidth(300)
        self.setMaximumWidth(600)


class UserItem(QFrame):
    """Custom user list item widget"""
    
    clicked = pyqtSignal(str)  # username
    
    def __init__(self, username: str, status: str = "online", avatar: Optional[QPixmap] = None):
        """
        Initialize user item.
        
        Args:
            username: User's username
            status: User status ('online', 'offline', 'away')
            avatar: User's avatar pixmap
        """
        super().__init__()
        self.username = username
        self.status = status
        self.avatar = avatar
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components"""
        self.setStyleSheet("""
            QFrame {
                background-color: #252525;
                border-radius: 5px;
                padding: 8px;
                margin: 4px 0px;
            }
            QFrame:hover {
                background-color: #303030;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        
        # Status indicator
        status_indicator = QFrame()
        status_color = {
            "online": "#107c10",
            "offline": "#d13438",
            "away": "#f7630c"
        }.get(self.status, "#808080")
        
        status_indicator.setStyleSheet(f"""
            QFrame {{
                background-color: {status_color};
                border-radius: 5px;
                min-width: 10px;
                max-width: 10px;
                min-height: 10px;
                max-height: 10px;
            }}
        """)
        layout.addWidget(status_indicator)
        
        # Username
        name_label = QLabel(self.username)
        name_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        name_label.setStyleSheet("color: #ffffff; margin-left: 8px;")
        layout.addWidget(name_label, 1)
    
    def mousePressEvent(self, event):
        """Handle click event"""
        self.clicked.emit(self.username)


class RoundedButton(QPushButton):
    """Custom rounded button with hover animation"""
    
    def __init__(self, text: str, icon: Optional[QIcon] = None, style: str = "primary"):
        """
        Initialize rounded button.
        
        Args:
            text: Button text
            icon: Button icon
            style: Button style ('primary', 'secondary', 'danger', 'success')
        """
        super().__init__(text)
        self.style = style
        
        if icon:
            self.setIcon(icon)
            self.setIconSize(QSize(16, 16))
        
        self.setMinimumHeight(36)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setObjectName(style)
        
        # Setup animation
        self.setProperty("hovered", False)
    
    def enterEvent(self, event):
        """Handle mouse enter"""
        self.setProperty("hovered", True)
        QApplication.style().polish(self)
    
    def leaveEvent(self, event):
        """Handle mouse leave"""
        self.setProperty("hovered", False)
        QApplication.style().polish(self)


class StatusBadge(QFrame):
    """Custom status badge widget"""
    
    def __init__(self, text: str, status_type: str = "info"):
        """
        Initialize status badge.
        
        Args:
            text: Badge text
            status_type: Badge type ('info', 'success', 'warning', 'error')
        """
        super().__init__()
        self.text = text
        self.status_type = status_type
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components"""
        colors = {
            "info": "#0078d4",
            "success": "#107c10",
            "warning": "#f7630c",
            "error": "#d13438"
        }
        color = colors.get(self.status_type, "#0078d4")
        
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 12px;
                padding: 4px 12px;
            }}
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel(self.text)
        label.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 11px;")
        label.setFont(QFont("Segoe UI", 10))
        layout.addWidget(label)


class AnimatedLabel(QLabel):
    """Label with fade-in animation"""
    
    def __init__(self, text: str = ""):
        """Initialize animated label"""
        super().__init__(text)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    
    def animate_in(self):
        """Start fade-in animation"""
        self.setWindowOpacity(0.0)
        self.animation.start()


class ChatHeaderFrame(QFrame):
    """Custom header frame for chat window"""
    
    def __init__(self, title: str = "NearMeet", subtitle: str = ""):
        """
        Initialize chat header.
        
        Args:
            title: Header title
            subtitle: Header subtitle
        """
        super().__init__()
        self._setup_ui(title, subtitle)
    
    def _setup_ui(self, title: str, subtitle: str):
        """Setup UI components"""
        self.setObjectName("header")
        self.setStyleSheet("""
            QFrame#header {
                background-color: #2d2d2d;
                border-bottom: 1px solid #404040;
                padding: 12px;
            }
        """)
        self.setMinimumHeight(60)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(4)
        
        # Title
        title_label = QLabel(title)
        title_label.setObjectName("title")
        title_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # Subtitle
        if subtitle:
            subtitle_label = QLabel(subtitle)
            subtitle_label.setStyleSheet("color: #a0a0a0; font-size: 10px;")
            layout.addWidget(subtitle_label)


class SeparatorLine(QFrame):
    """Horizontal separator line"""
    
    def __init__(self, color: str = "#404040"):
        """
        Initialize separator line.
        
        Args:
            color: Separator color
        """
        super().__init__()
        self.setStyleSheet(f"background-color: {color};")
        self.setMinimumHeight(1)
        self.setMaximumHeight(1)
