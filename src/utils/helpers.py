"""Helper utilities for NearMeet"""

import socket
import hashlib
import json
from pathlib import Path
from typing import Optional, List
import platform
import uuid


def get_local_ip() -> str:
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_hostname() -> str:
    """Get computer hostname"""
    return socket.gethostname()


def get_platform_info() -> dict:
    """Get platform information"""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def calculate_file_hash(filepath: Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file"""
    hash_obj = hashlib.new(algorithm)
    
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def generate_unique_id() -> str:
    """Generate a unique ID"""
    return str(uuid.uuid4())


def get_timestamp_string() -> str:
    """Get current timestamp as string"""
    from datetime import datetime
    return datetime.now().isoformat()


def is_valid_ip(ip: str) -> bool:
    """Check if string is a valid IP address"""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def is_port_available(port: int, host: str = "127.0.0.1") -> bool:
    """Check if a port is available"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.close()
        return True
    except OSError:
        return False


def deep_merge(dict1: dict, dict2: dict) -> dict:
    """Deep merge two dictionaries"""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
