"""Advanced animation and visual effects for PyQt6 widgets"""

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QSize
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtEffect import QGraphicsOpacityEffect
from typing import Optional


class SmoothFadeEffect(QWidget):
    """Widget with smooth fade-in/fade-out effects"""
    
    def __init__(self, widget: QWidget, duration: int = 500):
        """
        Initialize fade effect
        
        Args:
            widget: Widget to apply effect to
            duration: Animation duration in milliseconds
        """
        super().__init__()
        self.widget = widget
        self.duration = duration
        
        # Create opacity effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.widget.setGraphicsEffect(self.opacity_effect)
        
        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(self.duration)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    
    def fade_in(self):
        """Fade in the widget"""
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()
    
    def fade_out(self):
        """Fade out the widget"""
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.start()
    
    def toggle_fade(self):
        """Toggle between fade in and out"""
        if self.opacity_effect.opacity() < 0.5:
            self.fade_in()
        else:
            self.fade_out()


class SlideInAnimation(QWidget):
    """Widget with slide-in animation from left"""
    
    def __init__(self, widget: QWidget, duration: int = 300):
        """
        Initialize slide-in animation
        
        Args:
            widget: Widget to animate
            duration: Animation duration in milliseconds
        """
        super().__init__()
        self.widget = widget
        self.duration = duration
        self.start_x = -widget.width()
        self.end_x = 0
        
        # Create animation for geometry
        self.animation = QPropertyAnimation(self.widget, b"geometry")
        self.animation.setDuration(self.duration)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def slide_in_left(self):
        """Slide in from left"""
        self.animation.setStartValue(
            self.widget.geometry().translated(self.start_x, 0)
        )
        self.animation.setEndValue(self.widget.geometry())
        self.animation.start()
    
    def slide_in_right(self):
        """Slide in from right"""
        self.animation.setStartValue(
            self.widget.geometry().translated(-self.start_x, 0)
        )
        self.animation.setEndValue(self.widget.geometry())
        self.animation.start()


class PulseEffect(QWidget):
    """Widget with pulsing opacity effect"""
    
    def __init__(self, widget: QWidget, duration: int = 1000):
        """
        Initialize pulse effect
        
        Args:
            widget: Widget to pulse
            duration: Animation duration in milliseconds
        """
        super().__init__()
        self.widget = widget
        self.duration = duration
        
        # Create opacity effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.widget.setGraphicsEffect(self.opacity_effect)
        
        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(self.duration)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.animation.setStartValue(0.5)
        self.animation.setEndValue(1.0)
        self.animation.setLoopCount(-1)  # Infinite loop
    
    def start_pulse(self):
        """Start pulsing animation"""
        self.animation.start()
    
    def stop_pulse(self):
        """Stop pulsing animation"""
        self.animation.stop()
        self.opacity_effect.setOpacity(1.0)


class ColorChangeEffect(QWidget):
    """Widget with smooth color transition"""
    
    def __init__(self, widget: QWidget, duration: int = 500):
        """
        Initialize color change animation
        
        Args:
            widget: Widget to change color (must be QPushButton or similar)
            duration: Animation duration in milliseconds
        """
        super().__init__()
        self.widget = widget
        self.duration = duration
        self.animation = QPropertyAnimation(self.widget, b"color")
        self.animation.setDuration(self.duration)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    
    def change_color(self, start_color: str, end_color: str):
        """
        Animate color change
        
        Args:
            start_color: Starting color (hex or name)
            end_color: Ending color (hex or name)
        """
        self.animation.setStartValue(QColor(start_color))
        self.animation.setEndValue(QColor(end_color))
        self.animation.start()


class ScaleEffect(QWidget):
    """Widget with zoom/scale animation"""
    
    def __init__(self, widget: QWidget, scale_factor: float = 1.1, duration: int = 300):
        """
        Initialize scale animation
        
        Args:
            widget: Widget to scale
            scale_factor: Scale multiplier (1.1 = 10% larger)
            duration: Animation duration in milliseconds
        """
        super().__init__()
        self.widget = widget
        self.scale_factor = scale_factor
        self.duration = duration
        self.original_size = self.widget.size()
        
        # Create animation
        self.animation = QPropertyAnimation(self.widget, b"minimumSize")
        self.animation.setDuration(self.duration)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    
    def scale_up(self):
        """Scale widget larger"""
        new_size = QSize(
            int(self.original_size.width() * self.scale_factor),
            int(self.original_size.height() * self.scale_factor)
        )
        self.animation.setStartValue(self.original_size)
        self.animation.setEndValue(new_size)
        self.animation.start()
    
    def scale_down(self):
        """Scale widget smaller"""
        new_size = QSize(
            int(self.original_size.width() / self.scale_factor),
            int(self.original_size.height() / self.scale_factor)
        )
        self.animation.setStartValue(self.original_size)
        self.animation.setEndValue(new_size)
        self.animation.start()


class PressAnimation(QPushButton):
    """Button with enhanced press animation effect"""
    
    def __init__(self, text: str = ""):
        """Initialize animated button"""
        super().__init__(text)
        self.scale_animation = None
        self.opacity_animation = None
        self._setup_animation()
    
    def _setup_animation(self):
        """Setup press animation"""
        # Scale animation
        self.scale_animation = QPropertyAnimation(self, b"iconSize")
        self.scale_animation.setDuration(150)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def mousePressEvent(self, event):
        """Handle mouse press with animation"""
        super().mousePressEvent(event)
        self._animate_press()
    
    def _animate_press(self):
        """Play press animation"""
        # Could add scale or color change animation here
        pass


class NotificationBadge(QLabel):
    """Notification badge with pulsing animation"""
    
    def __init__(self, count: int = 0):
        """
        Initialize notification badge
        
        Args:
            count: Initial notification count
        """
        super().__init__(str(count))
        self.count = count
        self._setup_styling()
        self._setup_animation()
    
    def _setup_styling(self):
        """Setup badge styling"""
        self.setStyleSheet("""
            QLabel {
                background-color: #d13438;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-size: 11px;
                padding: 2px 6px;
                min-width: 20px;
                text-align: center;
            }
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def _setup_animation(self):
        """Setup pulsing animation"""
        self.pulse_effect = PulseEffect(self, duration=1500)
    
    def set_count(self, count: int):
        """Update notification count"""
        self.count = count
        self.setText(str(count))
        if count > 0:
            self.pulse_effect.start_pulse()
        else:
            self.pulse_effect.stop_pulse()


class TypingIndicator(QWidget):
    """Animated typing indicator (three dots)"""
    
    def __init__(self):
        """Initialize typing indicator"""
        super().__init__()
        self.label = QLabel("...")
        
        # Setup styling
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #888888;")
        
        # Setup animation
        self._setup_animation()
    
    def _setup_animation(self):
        """Setup typing animation"""
        self.animation = QPropertyAnimation(self.label, b"text")
        self.animation.setDuration(600)
        
        # Manual animation with timer
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_dots)
        self.dot_count = 0
    
    def start(self):
        """Start typing animation"""
        self.timer.start(400)
    
    def stop(self):
        """Stop typing animation"""
        self.timer.stop()
        self.label.setText("")
    
    def _update_dots(self):
        """Update dots display"""
        self.dot_count = (self.dot_count + 1) % 4
        self.label.setText("." * self.dot_count)


class FloatingLabelAnimation(QLabel):
    """Label that floats above widget with fade-in animation"""
    
    def __init__(self, text: str, duration: int = 800):
        """
        Initialize floating label
        
        Args:
            text: Label text
            duration: Animation duration in milliseconds
        """
        super().__init__(text)
        self.duration = duration
        
        # Setup styling
        self.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 11px;
            }
        """)
        
        # Setup animation
        self._setup_animation()
    
    def _setup_animation(self):
        """Setup floating animation"""
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)
        
        # Fade out animation
        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(self.duration)
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.setEasingCurve(QEasingCurve.Type.InQuad)
    
    def show_float(self):
        """Show floating animation"""
        self.opacity_effect.setOpacity(1.0)
        self.fade_animation.start()


# Animation preset configurations
ANIMATION_PRESETS = {
    "fade_in": {
        "type": "fade",
        "direction": "in",
        "duration": 500,
        "easing": QEasingCurve.Type.InOutQuad,
    },
    "fade_out": {
        "type": "fade",
        "direction": "out",
        "duration": 500,
        "easing": QEasingCurve.Type.InOutQuad,
    },
    "slide_left": {
        "type": "slide",
        "direction": "left",
        "duration": 300,
        "easing": QEasingCurve.Type.OutCubic,
    },
    "slide_right": {
        "type": "slide",
        "direction": "right",
        "duration": 300,
        "easing": QEasingCurve.Type.OutCubic,
    },
    "pulse": {
        "type": "pulse",
        "duration": 1000,
        "easing": QEasingCurve.Type.InOutSine,
    },
    "bounce": {
        "type": "bounce",
        "duration": 400,
        "easing": QEasingCurve.Type.OutBounce,
    },
}


def apply_animation(widget: QWidget, preset: str = "fade_in"):
    """
    Apply preset animation to widget
    
    Args:
        widget: Widget to animate
        preset: Animation preset name
    
    Returns:
        Animation object
    """
    if preset not in ANIMATION_PRESETS:
        raise ValueError(f"Unknown preset: {preset}")
    
    config = ANIMATION_PRESETS[preset]
    
    if config["type"] == "fade":
        effect = SmoothFadeEffect(widget, config["duration"])
        if config["direction"] == "in":
            effect.fade_in()
        else:
            effect.fade_out()
        return effect
    
    elif config["type"] == "slide":
        effect = SlideInAnimation(widget, config["duration"])
        if config["direction"] == "left":
            effect.slide_in_left()
        else:
            effect.slide_in_right()
        return effect
    
    elif config["type"] == "pulse":
        effect = PulseEffect(widget, config["duration"])
        effect.start_pulse()
        return effect
    
    return None
