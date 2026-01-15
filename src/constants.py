"""Constants for NearMeet application"""

# Default values
DEFAULT_USERNAME = "Anonymous"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000
DEFAULT_TIMEOUT = 30

# Message limits
MAX_MESSAGE_LENGTH = 10000
MAX_USERNAME_LENGTH = 32
MIN_USERNAME_LENGTH = 3

# File transfer
MAX_FILE_SIZE = 104857600  # 100MB
ALLOWED_FILE_EXTENSIONS = {
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    "txt", "zip", "rar", "7z",
    "jpg", "jpeg", "png", "gif", "bmp",
    "mp3", "wav", "flac", "aac",
    "mp4", "avi", "mkv", "mov"
}

# Video/Audio
VIDEO_CODEC = "H.264"
AUDIO_CODEC = "AAC"
VIDEO_BITRATE = 500000  # 500 kbps
AUDIO_BITRATE = 128000  # 128 kbps

# Connection
HEARTBEAT_INTERVAL = 30  # seconds
RECONNECT_ATTEMPTS = 5
RECONNECT_INTERVAL = 2  # seconds
