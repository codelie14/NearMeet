"""Security and encryption module for NearMeet"""

import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.backends import default_backend
import base64

from src.utils.logger import get_logger

logger = get_logger(__name__)


class Encryption:
    """Encryption utilities for NearMeet"""
    
    @staticmethod
    def generate_key() -> str:
        """Generate a new encryption key"""
        return Fernet.generate_key().decode()
    
    @staticmethod
    def derive_key(password: str, salt: bytes = None) -> tuple[str, str]:
        """Derive encryption key from password"""
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key.decode(), base64.b64encode(salt).decode()
    
    @staticmethod
    def encrypt_message(message: str, key: str) -> str:
        """Encrypt a message"""
        try:
            fernet = Fernet(key.encode())
            encrypted = fernet.encrypt(message.encode())
            return encrypted.decode()
        except Exception as e:
            logger.error(f"Encryption error: {e}")
            raise
    
    @staticmethod
    def decrypt_message(encrypted_message: str, key: str) -> str:
        """Decrypt a message"""
        try:
            fernet = Fernet(key.encode())
            decrypted = fernet.decrypt(encrypted_message.encode())
            return decrypted.decode()
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            raise


class PasswordHasher:
    """Password hashing utilities"""
    
    @staticmethod
    def hash_password(password: str) -> tuple[str, str]:
        """Hash a password"""
        key, salt = Encryption.derive_key(password)
        return key, salt
    
    @staticmethod
    def verify_password(password: str, hashed: str, salt: str) -> bool:
        """Verify a password against a hash"""
        try:
            salt_bytes = base64.b64decode(salt.encode())
            key, _ = Encryption.derive_key(password, salt_bytes)
            return key == hashed
        except Exception as e:
            logger.error(f"Password verification error: {e}")
            return False
