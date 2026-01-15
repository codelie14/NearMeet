"""Validators for NearMeet"""

import re
from typing import Tuple


class ValidationError(Exception):
    """Validation error exception"""
    pass


def validate_username(username: str) -> Tuple[bool, str]:
    """
    Validate username
    
    Returns:
        (is_valid, error_message)
    """
    if not username:
        return False, "Username cannot be empty"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    if len(username) > 32:
        return False, "Username must be at most 32 characters"
    
    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return False, "Username can only contain letters, numbers, underscores, and hyphens"
    
    return True, ""


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate email address
    
    Returns:
        (is_valid, error_message)
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not email:
        return False, "Email cannot be empty"
    
    if not re.match(pattern, email):
        return False, "Invalid email format"
    
    return True, ""


def validate_port(port: int) -> Tuple[bool, str]:
    """
    Validate port number
    
    Returns:
        (is_valid, error_message)
    """
    if not isinstance(port, int):
        return False, "Port must be an integer"
    
    if port < 1 or port > 65535:
        return False, "Port must be between 1 and 65535"
    
    return True, ""


def validate_ip_address(ip: str) -> Tuple[bool, str]:
    """
    Validate IP address
    
    Returns:
        (is_valid, error_message)
    """
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    
    if not ip:
        return False, "IP address cannot be empty"
    
    if not re.match(pattern, ip):
        return False, "Invalid IP address format"
    
    parts = ip.split(".")
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False, "IP address octets must be between 0 and 255"
        except ValueError:
            return False, "Invalid IP address format"
    
    return True, ""


def validate_file_path(path: str) -> Tuple[bool, str]:
    """
    Validate file path
    
    Returns:
        (is_valid, error_message)
    """
    if not path:
        return False, "Path cannot be empty"
    
    # Check for path traversal attacks
    if ".." in path:
        return False, "Path traversal not allowed"
    
    return True, ""


def validate_password(password: str, min_length: int = 8) -> Tuple[bool, str]:
    """
    Validate password strength
    
    Returns:
        (is_valid, error_message)
    """
    if not password:
        return False, "Password cannot be empty"
    
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    
    return True, ""
