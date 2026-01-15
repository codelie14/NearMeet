"""Main window for NearMeet application"""

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QListWidget, QListWidgetItem,
    QLabel, QLineEdit, QSplitter, QStatusBar, QMenuBar,
    QMenu, QMessageBox, QDialog
)
from PyQt6.QtCore import Qt, pyqtSignal, QThread, QTimer
from PyQt6.QtGui import QIcon, QPixmap, QFont

from src.config import UIConfig, AppConfig
from src.chat.manager import ChatManager
from src.chat.message import Message
from src.utils.logger import get_logger

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
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Top section - User info
        top_layout = QHBoxLayout()
        
        user_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMaximumWidth(200)
        
        top_layout.addWidget(user_label)
        top_layout.addWidget(self.username_input)
        top_layout.addStretch()
        
        main_layout.addLayout(top_layout)
        
        # Content section - Chat and users
        content_layout = QHBoxLayout()
        
        # Left side - User list
        left_layout = QVBoxLayout()
        left_label = QLabel("Users Online")
        left_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        left_layout.addWidget(left_label)
        
        self.users_list = QListWidget()
        self.users_list.setMaximumWidth(200)
        left_layout.addWidget(self.users_list)
        
        content_layout.addLayout(left_layout)
        
        # Middle/Right side - Chat area
        chat_layout = QVBoxLayout()
        
        # Chat display
        chat_label = QLabel("Messages")
        chat_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        chat_layout.addWidget(chat_label)
        
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Courier", 9))
        chat_layout.addWidget(self.chat_display)
        
        # Message input
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type a message and press Enter...")
        self.message_input.returnPressed.connect(self._send_message)
        chat_layout.addWidget(self.message_input)
        
        # Buttons layout
        buttons_layout = QHBoxLayout()
        
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self._send_message)
        
        self.call_button = QPushButton("Call")
        self.call_button.clicked.connect(self._initiate_call)
        
        self.share_screen_button = QPushButton("Share Screen")
        self.share_screen_button.clicked.connect(self._share_screen)
        
        self.file_button = QPushButton("Send File")
        self.file_button.clicked.connect(self._send_file)
        
        buttons_layout.addWidget(self.send_button)
        buttons_layout.addWidget(self.call_button)
        buttons_layout.addWidget(self.share_screen_button)
        buttons_layout.addWidget(self.file_button)
        
        chat_layout.addLayout(buttons_layout)
        
        content_layout.addLayout(chat_layout)
        
        main_layout.addLayout(content_layout)
    
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
        timestamp = message.timestamp.strftime("%H:%M:%S")
        formatted = f"[{timestamp}] {message.sender}: {message.content}\n"
        self.chat_display.append(formatted)
    
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
            self.chat_display.clear()
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
