"""Tests for advanced animations"""

import pytest
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton
from PyQt6.QtCore import Qt

from src.ui.animations import (
    SmoothFadeEffect, SlideInAnimation, PulseEffect, ScaleEffect,
    NotificationBadge, TypingIndicator, FloatingLabelAnimation,
    apply_animation
)


@pytest.fixture
def qapp():
    """Fixture for QApplication"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestSmoothFadeEffect:
    """Test fade effects"""
    
    def test_creation(self, qapp):
        """Test fade effect creation"""
        label = QLabel("Test")
        fade = SmoothFadeEffect(label)
        assert fade.widget == label
        assert fade.duration == 500
    
    def test_custom_duration(self, qapp):
        """Test custom duration"""
        label = QLabel("Test")
        fade = SmoothFadeEffect(label, duration=1000)
        assert fade.animation.duration() == 1000
    
    def test_fade_in(self, qapp):
        """Test fade in animation"""
        label = QLabel("Test")
        fade = SmoothFadeEffect(label)
        fade.fade_in()
        assert fade.animation.startValue() == 0.0
        assert fade.animation.endValue() == 1.0
    
    def test_fade_out(self, qapp):
        """Test fade out animation"""
        label = QLabel("Test")
        fade = SmoothFadeEffect(label)
        fade.fade_out()
        assert fade.animation.startValue() == 1.0
        assert fade.animation.endValue() == 0.0


class TestSlideInAnimation:
    """Test slide animations"""
    
    def test_creation(self, qapp):
        """Test slide animation creation"""
        label = QLabel("Test")
        slide = SlideInAnimation(label)
        assert slide.widget == label
        assert slide.duration == 300
    
    def test_custom_duration(self, qapp):
        """Test custom duration"""
        label = QLabel("Test")
        slide = SlideInAnimation(label, duration=500)
        assert slide.animation.duration() == 500
    
    def test_slide_in_left(self, qapp):
        """Test slide in from left"""
        label = QLabel("Test")
        label.setGeometry(100, 100, 100, 50)
        slide = SlideInAnimation(label)
        slide.slide_in_left()
        # Animation should be started
        assert slide.animation.state() > 0


class TestPulseEffect:
    """Test pulse effects"""
    
    def test_creation(self, qapp):
        """Test pulse effect creation"""
        label = QLabel("Test")
        pulse = PulseEffect(label)
        assert pulse.widget == label
        assert pulse.duration == 1000
    
    def test_custom_duration(self, qapp):
        """Test custom duration"""
        label = QLabel("Test")
        pulse = PulseEffect(label, duration=1500)
        assert pulse.animation.duration() == 1500
    
    def test_pulse_values(self, qapp):
        """Test pulse animation values"""
        label = QLabel("Test")
        pulse = PulseEffect(label)
        assert pulse.animation.startValue() == 0.5
        assert pulse.animation.endValue() == 1.0
    
    def test_pulse_infinite_loop(self, qapp):
        """Test infinite loop count"""
        label = QLabel("Test")
        pulse = PulseEffect(label)
        assert pulse.animation.loopCount() == -1


class TestScaleEffect:
    """Test scale effects"""
    
    def test_creation(self, qapp):
        """Test scale effect creation"""
        label = QLabel("Test")
        label.setMinimumSize(100, 50)
        scale = ScaleEffect(label)
        assert scale.widget == label
        assert scale.scale_factor == 1.1
    
    def test_custom_scale_factor(self, qapp):
        """Test custom scale factor"""
        label = QLabel("Test")
        label.setMinimumSize(100, 50)
        scale = ScaleEffect(label, scale_factor=1.5)
        assert scale.scale_factor == 1.5
    
    def test_scale_up(self, qapp):
        """Test scale up"""
        label = QLabel("Test")
        label.setMinimumSize(100, 50)
        scale = ScaleEffect(label, scale_factor=1.1)
        # Just verify it doesn't crash
        assert scale is not None


class TestNotificationBadge:
    """Test notification badge"""
    
    def test_creation(self, qapp):
        """Test badge creation"""
        badge = NotificationBadge(5)
        assert badge.count == 5
        assert badge.text() == "5"
    
    def test_initial_count_zero(self, qapp):
        """Test badge with zero count"""
        badge = NotificationBadge(0)
        assert badge.count == 0
        assert badge.text() == "0"
    
    def test_set_count(self, qapp):
        """Test setting count"""
        badge = NotificationBadge(0)
        badge.set_count(10)
        assert badge.count == 10
        assert badge.text() == "10"
    
    def test_styling(self, qapp):
        """Test badge has styling"""
        badge = NotificationBadge(1)
        stylesheet = badge.styleSheet()
        assert "d13438" in stylesheet  # Red color
        assert "white" in stylesheet


class TestTypingIndicator:
    """Test typing indicator"""
    
    def test_creation(self, qapp):
        """Test typing indicator creation"""
        typing = TypingIndicator()
        assert typing.label is not None
    
    def test_initial_text(self, qapp):
        """Test initial text is empty"""
        typing = TypingIndicator()
        assert typing.label.text() == ""
    
    def test_start_animation(self, qapp):
        """Test start animation"""
        typing = TypingIndicator()
        typing.start()
        # Timer should be active
        assert typing.timer.isActive()
    
    def test_stop_animation(self, qapp):
        """Test stop animation"""
        typing = TypingIndicator()
        typing.start()
        typing.stop()
        assert typing.label.text() == ""
        assert not typing.timer.isActive()


class TestFloatingLabelAnimation:
    """Test floating label"""
    
    def test_creation(self, qapp):
        """Test floating label creation"""
        label = FloatingLabelAnimation("+1")
        assert label.text() == "+1"
        assert label.duration == 800
    
    def test_custom_duration(self, qapp):
        """Test custom duration"""
        label = FloatingLabelAnimation("Test", duration=1000)
        assert label.duration == 1000
    
    def test_styling(self, qapp):
        """Test label styling"""
        label = FloatingLabelAnimation("+1")
        stylesheet = label.styleSheet()
        assert "888888" in stylesheet  # Gray color


class TestAnimationPresets:
    """Test animation presets"""
    
    def test_fade_in_preset(self, qapp):
        """Test fade in preset"""
        label = QLabel("Test")
        effect = apply_animation(label, "fade_in")
        assert effect is not None
    
    def test_fade_out_preset(self, qapp):
        """Test fade out preset"""
        label = QLabel("Test")
        effect = apply_animation(label, "fade_out")
        assert effect is not None
    
    def test_slide_left_preset(self, qapp):
        """Test slide left preset"""
        label = QLabel("Test")
        label.setGeometry(0, 0, 100, 50)
        effect = apply_animation(label, "slide_left")
        assert effect is not None
    
    def test_pulse_preset(self, qapp):
        """Test pulse preset"""
        label = QLabel("Test")
        effect = apply_animation(label, "pulse")
        assert effect is not None
    
    def test_invalid_preset(self, qapp):
        """Test invalid preset raises error"""
        label = QLabel("Test")
        with pytest.raises(ValueError):
            apply_animation(label, "invalid_preset")


class TestAnimationIntegration:
    """Test animation integration"""
    
    def test_multiple_animations(self, qapp):
        """Test multiple animations on different widgets"""
        label1 = QLabel("Test 1")
        label2 = QLabel("Test 2")
        
        fade1 = SmoothFadeEffect(label1)
        fade2 = SmoothFadeEffect(label2)
        
        fade1.fade_in()
        fade2.fade_out()
        
        assert fade1.widget == label1
        assert fade2.widget == label2
    
    def test_animation_cleanup(self, qapp):
        """Test animation cleanup"""
        label = QLabel("Test")
        fade = SmoothFadeEffect(label)
        fade.fade_in()
        fade.animation.stop()
        assert not fade.animation.state()
