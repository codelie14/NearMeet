"""Tests for security module"""

import pytest
from src.network.security import Encryption, PasswordHasher


class TestEncryption:
    """Test Encryption class"""
    
    def test_generate_key(self):
        """Test generating a key"""
        key1 = Encryption.generate_key()
        key2 = Encryption.generate_key()
        
        assert key1
        assert key2
        assert key1 != key2
    
    def test_encrypt_decrypt(self):
        """Test encrypting and decrypting a message"""
        key = Encryption.generate_key()
        message = "Secret message"
        
        encrypted = Encryption.encrypt_message(message, key)
        assert encrypted != message
        
        decrypted = Encryption.decrypt_message(encrypted, key)
        assert decrypted == message
    
    def test_derive_key(self):
        """Test deriving key from password"""
        password = "mypassword"
        
        key1, salt1 = Encryption.derive_key(password)
        # salt1 is base64 encoded, so we need to decode it first
        import base64
        salt_bytes = base64.b64decode(salt1)
        key2, salt2 = Encryption.derive_key(password, salt=salt_bytes)
        
        assert key1 == key2
        assert salt1 == salt2


class TestPasswordHasher:
    """Test PasswordHasher class"""
    
    def test_hash_password(self):
        """Test hashing a password"""
        password = "MyPassword123"
        
        hashed, salt = PasswordHasher.hash_password(password)
        assert hashed
        assert salt
    
    def test_verify_password_correct(self):
        """Test verifying correct password"""
        password = "MyPassword123"
        
        hashed, salt = PasswordHasher.hash_password(password)
        is_valid = PasswordHasher.verify_password(password, hashed, salt)
        
        assert is_valid
    
    def test_verify_password_incorrect(self):
        """Test verifying incorrect password"""
        password = "MyPassword123"
        wrong_password = "WrongPassword"
        
        hashed, salt = PasswordHasher.hash_password(password)
        is_valid = PasswordHasher.verify_password(wrong_password, hashed, salt)
        
        assert not is_valid
