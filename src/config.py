"""
NearMeet Application Configuration Module
Manages all application settings from environment variables and config files
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base Paths
BASE_DIR = Path(__file__).parent.parent
SRC_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
CONFIG_DIR = BASE_DIR / "config"
SHARED_FILES_DIR = BASE_DIR / "shared_files"

# Create necessary directories
for directory in [DATA_DIR, LOGS_DIR, SHARED_FILES_DIR]:
    directory.mkdir(exist_ok=True)


class ServerConfig:
    """Server configuration"""
    HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    PORT = int(os.getenv("SERVER_PORT", 5000))
    DEBUG = os.getenv("SERVER_DEBUG", "True").lower() == "true"
    MAX_CLIENTS = 100
    BUFFER_SIZE = 4096
    TIMEOUT = 30


class ClientConfig:
    """Client configuration"""
    AUTO_CONNECT = os.getenv("CLIENT_AUTO_CONNECT", "False").lower() == "true"
    TIMEOUT = int(os.getenv("CLIENT_TIMEOUT", 30))
    RECONNECT_ATTEMPTS = 5
    RECONNECT_INTERVAL = 2


class AppConfig:
    """Application configuration"""
    NAME = os.getenv("APP_NAME", "NearMeet")
    VERSION = os.getenv("APP_VERSION", "1.0.0")
    LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "INFO")
    ORGANIZATION = "IndraLabs"


class DatabaseConfig:
    """Database configuration"""
    PATH = Path(os.getenv("DATABASE_PATH", str(DATA_DIR / "nearmeet.db")))
    BACKUP_ENABLED = os.getenv("DATABASE_BACKUP_ENABLED", "True").lower() == "true"
    BACKUP_INTERVAL = int(os.getenv("DATABASE_BACKUP_INTERVAL", 3600))
    TIMEOUT = 30


class FileShareConfig:
    """File sharing configuration"""
    ENABLED = os.getenv("FILE_SHARING_ENABLED", "True").lower() == "true"
    MAX_SIZE = int(os.getenv("FILE_SHARING_MAX_SIZE", 104857600))  # 100MB
    UPLOAD_PATH = Path(os.getenv("FILE_SHARING_PATH", str(SHARED_FILES_DIR)))
    TIMEOUT = int(os.getenv("FILE_SHARING_TIMEOUT", 300))
    ALLOWED_EXTENSIONS = {
        "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
        "txt", "zip", "rar", "7z",
        "jpg", "jpeg", "png", "gif", "bmp",
        "mp3", "wav", "flac", "aac",
        "mp4", "avi", "mkv", "mov"
    }


class AudioConfig:
    """Audio configuration"""
    ENABLED = os.getenv("AUDIO_ENABLED", "True").lower() == "true"
    INPUT_DEVICE = os.getenv("AUDIO_INPUT_DEVICE", "default")
    OUTPUT_DEVICE = os.getenv("AUDIO_OUTPUT_DEVICE", "default")
    SAMPLE_RATE = int(os.getenv("AUDIO_SAMPLE_RATE", 44100))
    CHUNK_SIZE = int(os.getenv("AUDIO_CHUNK_SIZE", 1024))
    CHANNELS = 2
    FORMAT = "float32"
    BITRATE = 128000  # 128 kbps


class VideoConfig:
    """Video configuration"""
    ENABLED = os.getenv("VIDEO_ENABLED", "True").lower() == "true"
    DEVICE = int(os.getenv("VIDEO_DEVICE", 0))
    WIDTH = int(os.getenv("VIDEO_WIDTH", 640))
    HEIGHT = int(os.getenv("VIDEO_HEIGHT", 480))
    FPS = int(os.getenv("VIDEO_FPS", 30))
    BITRATE = int(os.getenv("VIDEO_BITRATE", 500000))


class ScreenConfig:
    """Screen sharing configuration"""
    ENABLED = os.getenv("SCREEN_SHARING_ENABLED", "True").lower() == "true"
    QUALITY = int(os.getenv("SCREEN_SHARE_QUALITY", 80))
    FPS = int(os.getenv("SCREEN_SHARE_FPS", 15))


class SecurityConfig:
    """Security configuration"""
    ENCRYPTION_ENABLED = os.getenv("ENCRYPTION_ENABLED", "True").lower() == "true"
    ENCRYPTION_ALGORITHM = os.getenv("ENCRYPTION_ALGORITHM", "AES-256-GCM")
    PASSWORD_HASH_ALGORITHM = os.getenv("PASSWORD_HASH_ALGORITHM", "argon2")
    SESSION_TIMEOUT = 3600  # 1 hour
    MAX_LOGIN_ATTEMPTS = 5


class LogConfig:
    """Logging configuration"""
    FILE_PATH = Path(os.getenv("LOG_FILE_PATH", str(LOGS_DIR / "nearmeet.log")))
    MAX_SIZE = int(os.getenv("LOG_MAX_SIZE", 10485760))  # 10MB
    BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 5))
    FORMAT = os.getenv(
        "LOG_FORMAT",
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class UIConfig:
    """UI configuration"""
    THEME = os.getenv("UI_THEME", "dark")
    LANGUAGE = os.getenv("UI_LANGUAGE", "fr")
    WINDOW_WIDTH = int(os.getenv("UI_WINDOW_WIDTH", 1200))
    WINDOW_HEIGHT = int(os.getenv("UI_WINDOW_HEIGHT", 800))
    WINDOW_MIN_WIDTH = 800
    WINDOW_MIN_HEIGHT = 600
    FONT_FAMILY = "Segoe UI"
    FONT_SIZE = 10


class FeatureFlags:
    """Feature flags for enabling/disabling features"""
    NOTIFICATIONS = os.getenv("FEATURE_NOTIFICATIONS", "True").lower() == "true"
    MESSAGE_SEARCH = os.getenv("FEATURE_MESSAGE_SEARCH", "True").lower() == "true"
    USER_PROFILES = os.getenv("FEATURE_USER_PROFILES", "True").lower() == "true"
    MESSAGE_REACTIONS = os.getenv("FEATURE_MESSAGE_REACTIONS", "False").lower() == "true"
    MESSAGE_EDIT = os.getenv("FEATURE_MESSAGE_EDIT", "True").lower() == "true"


# Convenience functions
def get_config(section: str) -> Optional[object]:
    """Get configuration for a specific section"""
    configs = {
        "server": ServerConfig,
        "client": ClientConfig,
        "app": AppConfig,
        "database": DatabaseConfig,
        "file_share": FileShareConfig,
        "audio": AudioConfig,
        "video": VideoConfig,
        "screen": ScreenConfig,
        "security": SecurityConfig,
        "log": LogConfig,
        "ui": UIConfig,
        "features": FeatureFlags,
    }
    return configs.get(section.lower())


def print_config():
    """Print current configuration (for debugging)"""
    print(f"\n{'='*60}")
    print(f"NearMeet Configuration - Version {AppConfig.VERSION}")
    print(f"{'='*60}")
    
    configs = {
        "Server": ServerConfig,
        "Client": ClientConfig,
        "Database": DatabaseConfig,
        "Audio": AudioConfig,
        "Video": VideoConfig,
        "Security": SecurityConfig,
    }
    
    for name, config in configs.items():
        print(f"\n{name} Configuration:")
        for key, value in config.__dict__.items():
            if not key.startswith("_"):
                print(f"  {key}: {value}")
    
    print(f"{'='*60}\n")


if __name__ == "__main__":
    print_config()
