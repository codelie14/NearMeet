"""Logging utilities for NearMeet"""

import logging
import logging.handlers
from pathlib import Path
from src.config import LogConfig, AppConfig


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance
    
    Args:
        name: Logger name (typically __name__)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Only configure if not already configured
    if not logger.handlers:
        logger.setLevel(LogConfig.FORMAT if isinstance(LogConfig.FORMAT, int) else logging.DEBUG)
        
        # Create formatters
        formatter = logging.Formatter(
            LogConfig.FORMAT,
            datefmt=LogConfig.DATE_FORMAT
        )
        
        # File handler with rotation
        log_file = LogConfig.FILE_PATH
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=LogConfig.MAX_SIZE,
            backupCount=LogConfig.BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger


def setup_logging():
    """Setup logging for the application"""
    root_logger = logging.getLogger()
    
    # Set root logger level
    level_str = AppConfig.LOG_LEVEL.upper()
    level = getattr(logging, level_str, logging.INFO)
    root_logger.setLevel(level)
    
    # Get NearMeet logger to ensure it's configured
    get_logger("nearmeet")
    
    return root_logger
