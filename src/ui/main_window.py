"""Main window for NearMeet application"""

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QListWidget, QListWidgetItem,
    QLabel, QLineEdit, QSplitter, QStatusBar, QMenuBar,
    QMenu, QMessageBox, QDialog, QFrame, QScrollArea
)
from PyQt6.QtCore import Qt, pyqtSignal, QThread, QTimer
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor

from src.config import UIConfig, AppConfig
from src.chat.manager import ChatManager
from src.chat.message import Message
from src.utils.logger import get_logger
from src.ui.styles import get_stylesheet
from src.ui.widgets import (
    MessageBubble, UserItem, RoundedButton, ChatHeaderFrame,
    StatusBadge, SeparatorLine
)

logger = get_logger(__name__)


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, mode: str = "client", parent=None):
        """Initialize main window"""
        super().__init__(parent)
        
        self.mode = mode
        self.chat_manager = ChatManager()
        
        logger.info(f"Initializing main window in {mode} mode")
        
        # Set window properties
        self.setWindowTitle(f"{AppConfig.NAME} - {mode.capitalize()}")
        self.setGeometry(100, 100, UIConfig.WINDOW_WIDTH, UIConfig.WINDOW_HEIGHT)
        self.setMinimumSize(UIConfig.WINDOW_MIN_WIDTH, UIConfig.WINDOW_MIN_HEIGHT)
        
        # Apply modern stylesheet
        self.setStyleSheet(get_stylesheet("dark"))
        
        # Create UI
        self._create_ui()
        self._create_menu()
        self._create_status_bar()
        
        logger.info("Main window initialized")
    
    def _create_ui(self):
        """Create user interface elements"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setContentsMargins(0, 0, 0, 0)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header with modern design
        self.header = ChatHeaderFrame(f"NearMeet ({self.mode.capitalize()})", "Ready to chat")
        main_layout.addWidget(self.header)
        
        # Separator
        main_layout.addWidget(SeparatorLine())
        
        # Top section - User info with custom button
        top_frame = QFrame()
        top_frame.setContentsMargins(12, 12, 12, 12)
        top_layout = QHBoxLayout(top_frame)
        top_layout.setSpacing(8)
        
        user_label = QLabel("Username:")
        user_label.setMinimumWidth(80)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMaximumWidth(200)
        
        self.connect_btn = RoundedButton("Connect", style="primary")
        self.disconnect_btn = RoundedButton("Disconnect", style="danger")
        self.disconnect_btn.setEnabled(False)
        
        top_layout.addWidget(user_label)
        top_layout.addWidget(self.username_input)
        top_layout.addWidget(self.connect_btn)
        top_layout.addWidget(self.disconnect_btn)
        top_layout.addStretch()
        
        main_layout.addWidget(top_frame)
        main_layout.addWidget(SeparatorLine())
        
        # Content section - Chat and users
        content_layout = QHBoxLayout()
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Left side - User list
        left_frame = QFrame()
        left_frame.setMaximumWidth(250)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(12, 12, 6, 12)
        left_layout.setSpacing(8)
        
        left_label = QLabel("Online Users")
        left_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        left_label.setMinimumHeight(24)
        left_layout.addWidget(left_label)
        
        self.users_list = QListWidget()
        self.users_list.setSpacing(4)
        left_layout.addWidget(self.users_list)
        
        self.status_badge = StatusBadge("Offline", "error")
        left_layout.addWidget(self.status_badge)
        
        content_layout.addWidget(left_frame)
        
        # Vertical separator
        content_layout.addWidget(SeparatorLine("#404040"))
        
        # Middle/Right side - Chat area
        chat_frame = QFrame()
        chat_layout = QVBoxLayout(chat_frame)
        chat_layout.setContentsMargins(12, 12, 12, 12)
        chat_layout.setSpacing(8)
        
        # Chat display
        chat_label = QLabel("Messages")
        chat_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        chat_label.setMinimumHeight(24)
        chat_layout.addWidget(chat_label)
        
        # Scroll area for messages
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(8)
        scroll_layout.addStretch()
        
        self.messages_container = scroll_widget
        self.messages_layout = scroll_layout
        scroll_area.setWidget(scroll_widget)
        
        chat_layout.addWidget(scroll_area)
        
        # Input area
        input_frame = QFrame()
        input_layout = QHBoxLayout(input_frame)
        input_layout.setSpacing(8)
        input_layout.setContentsMargins(0, 0, 0, 0)
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")
        self.message_input.setMinimumHeight(36)
        
        self.send_btn = RoundedButton("Send", style="success")
        self.send_btn.setMaximumWidth(100)
        
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_btn)
        
        chat_layout.addWidget(input_frame)
        
        content_layout.addWidget(chat_frame)
        
        # Add content to main layout
        main_layout.addLayout(content_layout)
        
        # Connect button signals
        self.message_input.returnPressed.connect(self._send_message)
        self.send_btn.clicked.connect(self._send_message)
    
    def _create_menu(self):
        """Create menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        connect_action = file_menu.addAction("Connect...")
        connect_action.triggered.connect(self._show_connect_dialog)
        
        disconnect_action = file_menu.addAction("Disconnect")
        disconnect_action.triggered.connect(self._disconnect)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        clear_action = edit_menu.addAction("Clear Chat")
        clear_action.triggered.connect(self._clear_chat)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self._show_about)
    
    def _create_status_bar(self):
        """Create status bar"""
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Ready")
    
    def _send_message(self):
        """Send a message"""
        text = self.message_input.text().strip()
        
        if not text:
            return
        
        username = self.username_input.text().strip() or "Anonymous"
        
        # Create message
        message = Message(sender=username, content=text)
        
        # Add to chat manager
        self.chat_manager.add_message(message)
        
        # Display in chat
        self._display_message(message)
        
        # Clear input
        self.message_input.clear()
        
        # Update status
        self.status.showMessage(f"Message sent by {username}")
        
        logger.debug(f"Message sent: {text}")
    
    def _display_message(self, message: Message):
        """Display a message in the chat"""
        timestamp = message.timestamp.strftime("%H:%M")
        
        # Create message bubble
        bubble = MessageBubble(
            sender=message.sender,
            message=message.content,
            timestamp=timestamp,
            is_own=(message.sender == self.username_input.text().strip())
        )
        
        # Insert before stretch in messages layout
        self.messages_layout.insertWidget(
            self.messages_layout.count() - 1, bubble
        )
    
    def _initiate_call(self):
        """Initiate a call"""
        self.status.showMessage("Call feature coming soon...")
        logger.info("Call button clicked")
    
    def _share_screen(self):
        """Share screen"""
        self.status.showMessage("Screen sharing feature coming soon...")
        logger.info("Share screen button clicked")
    
    def _send_file(self):
        """Send a file"""
        self.status.showMessage("File sharing feature coming soon...")
        logger.info("File button clicked")
    
    def _show_connect_dialog(self):
        """Show connect dialog"""
        QMessageBox.information(
            self,
            "Connect",
            "Connect feature will be implemented soon"
        )
    
    def _disconnect(self):
        """Disconnect from server"""
        self.status.showMessage("Disconnected")
        logger.info("Disconnected from server")
    
    def _clear_chat(self):
        """Clear chat"""
        reply = QMessageBox.question(
            self,
            "Clear Chat",
            "Are you sure you want to clear the chat?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Clear messages from layout
            while self.messages_layout.count() > 1:
                item = self.messages_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            
            self.chat_manager.clear_messages()
            self.status.showMessage("Chat cleared")
    
    def _show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "About NearMeet",
            f"{AppConfig.NAME} v{AppConfig.VERSION}\n\n"
            "A local network communication application\n\n"
            "© 2026 IndraLabs"
        )
    
    def closeEvent(self, event):
        """Handle window close event"""
        reply = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            logger.info("Application closing")
            event.accept()
        else:
            event.ignore()
