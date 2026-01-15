"""Tests for validators"""

import pytest
from src.utils.validators import (
    validate_username,
    validate_email,
    validate_port,
    validate_ip_address,
    validate_password,
)


class TestValidators:
    """Test validation functions"""
    
    def test_validate_username_valid(self):
        """Test valid username"""
        is_valid, error = validate_username("john_doe")
        assert is_valid
        assert error == ""
    
    def test_validate_username_too_short(self):
        """Test username too short"""
        is_valid, error = validate_username("ab")
        assert not is_valid
        assert "at least 3 characters" in error
    
    def test_validate_username_invalid_chars(self):
        """Test username with invalid characters"""
        is_valid, error = validate_username("john@doe")
        assert not is_valid
    
    def test_validate_email_valid(self):
        """Test valid email"""
        is_valid, error = validate_email("john@example.com")
        assert is_valid
    
    def test_validate_email_invalid(self):
        """Test invalid email"""
        is_valid, error = validate_email("not_an_email")
        assert not is_valid
    
    def test_validate_port_valid(self):
        """Test valid port"""
        is_valid, error = validate_port(5000)
        assert is_valid
    
    def test_validate_port_out_of_range(self):
        """Test port out of range"""
        is_valid, error = validate_port(99999)
        assert not is_valid
    
    def test_validate_ip_address_valid(self):
        """Test valid IP address"""
        is_valid, error = validate_ip_address("192.168.1.1")
        assert is_valid
    
    def test_validate_ip_address_invalid(self):
        """Test invalid IP address"""
        is_valid, error = validate_ip_address("192.168.1.999")
        assert not is_valid
    
    def test_validate_password_valid(self):
        """Test valid password"""
        is_valid, error = validate_password("StrongPass123!")
        assert is_valid
    
    def test_validate_password_no_uppercase(self):
        """Test password without uppercase"""
        is_valid, error = validate_password("weakpass123")
        assert not is_valid
        assert "uppercase" in error
    
    def test_validate_password_too_short(self):
        """Test password too short"""
        is_valid, error = validate_password("Weak1")
        assert not is_valid
