"""Main application class"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from src.config import AppConfig, UIConfig
from src.utils.logger import get_logger

logger = get_logger(__name__)


class NearMeetApp:
    """Main NearMeet Application"""
    
    def __init__(self, mode: str = "client"):
        """
        Initialize NearMeet application
        
        Args:
            mode: 'client' or 'server'
        """
        self.mode = mode
        self.app_instance: QApplication = None
        self.main_window = None
        
        logger.info(f"Initializing NearMeet {AppConfig.VERSION} in {mode} mode")
    
    def init_gui(self):
        """Initialize GUI"""
        try:
            # Import here to avoid circular imports
            from src.ui.main_window import MainWindow
            
            if not self.app_instance:
                self.app_instance = QApplication.instance() or QApplication(sys.argv)
            
            self.app_instance.setApplicationName(AppConfig.NAME)
            self.app_instance.setApplicationVersion(AppConfig.VERSION)
            
            self.main_window = MainWindow(mode=self.mode)
            logger.info("GUI initialized successfully")
            
            return self.main_window
            
        except Exception as e:
            logger.error(f"Failed to initialize GUI: {e}", exc_info=True)
            raise
    
    def run(self):
        """Run the application"""
        try:
            self.init_gui()
            self.main_window.show()
            
            logger.info("NearMeet application started")
            sys.exit(self.app_instance.exec())
            
        except Exception as e:
            logger.error(f"Failed to run application: {e}", exc_info=True)
            sys.exit(1)
    
    def shutdown(self):
        """Shutdown the application"""
        logger.info("Shutting down NearMeet application")
        if self.main_window:
            self.main_window.close()
        if self.app_instance:
            self.app_instance.quit()
