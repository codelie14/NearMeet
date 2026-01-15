# Integration Guide - Using the Visual Design System

## Overview

This guide explains how to use the new visual design system in the NearMeet application and how to extend it for additional windows and dialogs.

## Table of Contents

1. [Quick Integration](#quick-integration)
2. [Main Window](#main-window)
3. [Creating Custom Dialogs](#creating-custom-dialogs)
4. [Creating Custom Widgets](#creating-custom-widgets)
5. [Adding Animations](#adding-animations)
6. [Managing Preferences](#managing-preferences)
7. [Troubleshooting](#troubleshooting)

---

## Quick Integration

### Step 1: Apply Stylesheet to Your Window

```python
from PyQt6.QtWidgets import QMainWindow
from src.ui.styles import get_stylesheet

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Apply modern stylesheet
        theme = "dark"  # or "light"
        self.setStyleSheet(get_stylesheet(theme))
        
        # Now all child widgets will have modern styling
```

### Step 2: Use Custom Widgets

```python
from src.ui.widgets import (
    RoundedButton, MessageBubble, UserItem, 
    StatusBadge, ChatHeaderFrame, SeparatorLine
)

# Create a styled button
send_btn = RoundedButton("Send", style="success")
send_btn.clicked.connect(self.on_send_clicked)

# Create a message display
message = MessageBubble("Alice", "Hello!", "14:30", is_own=False)

# Create a user item
user = UserItem("Bob", "online")
```

### Step 3: Add Animations (Optional)

```python
from src.ui.animations import SmoothFadeEffect, apply_animation

# Create fade effect
fade = SmoothFadeEffect(widget)
fade.fade_in()

# Or use preset
apply_animation(widget, "fade_in")
```

---

## Main Window

### Current Implementation

The main window has been updated with modern styling:

```python
# In src/ui/main_window.py

class MainWindow(QMainWindow):
    def __init__(self, mode: str = "client"):
        super().__init__()
        
        # Apply modern stylesheet
        self.setStyleSheet(get_stylesheet("dark"))
        
        # Create UI with modern widgets
        self._create_ui()
    
    def _create_ui(self):
        """Create UI with modern widgets"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Add header
        self.header = ChatHeaderFrame("NearMeet", "Ready to chat")
        main_layout.addWidget(self.header)
        
        # Add separator
        main_layout.addWidget(SeparatorLine())
        
        # Add buttons
        self.connect_btn = RoundedButton("Connect", style="primary")
        main_layout.addWidget(self.connect_btn)
        
        # Add status
        self.status_badge = StatusBadge("Offline", "error")
        main_layout.addWidget(self.status_badge)
```

### Customizing the Main Window

**Change the theme:**
```python
# In __init__
theme = "light"  # Change to light theme
self.setStyleSheet(get_stylesheet(theme))
```

**Change header text:**
```python
self.header.setTitle("My Chat App")
self.header.setSubtitle("Connected")
```

**Update status badge:**
```python
self.status_badge.set_count(5)  # For notifications
# or
status = StatusBadge("Connected", "success")
```

---

## Creating Custom Dialogs

### Example: Connection Dialog

```python
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from src.ui.styles import get_stylesheet
from src.ui.widgets import RoundedButton, SeparatorLine

class ConnectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Connect to Server")
        self.setGeometry(100, 100, 400, 200)
        
        # Apply stylesheet
        self.setStyleSheet(get_stylesheet("dark"))
        
        self._create_ui()
    
    def _create_ui(self):
        """Create dialog UI"""
        layout = QVBoxLayout()
        
        # Host field
        host_layout = QHBoxLayout()
        host_label = QLabel("Host:")
        host_label.setMinimumWidth(80)
        self.host_input = QLineEdit()
        self.host_input.setText("localhost")
        host_layout.addWidget(host_label)
        host_layout.addWidget(self.host_input)
        layout.addLayout(host_layout)
        
        # Port field
        port_layout = QHBoxLayout()
        port_label = QLabel("Port:")
        port_label.setMinimumWidth(80)
        self.port_input = QLineEdit()
        self.port_input.setText("5000")
        port_layout.addWidget(port_label)
        port_layout.addWidget(self.port_input)
        layout.addLayout(port_layout)
        
        # Separator
        layout.addWidget(SeparatorLine())
        
        # Buttons
        button_layout = QHBoxLayout()
        
        connect_btn = RoundedButton("Connect", style="primary")
        cancel_btn = RoundedButton("Cancel", style="secondary")
        
        connect_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(connect_btn)
        button_layout.addWidget(cancel_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def get_host_port(self):
        """Get entered host and port"""
        return self.host_input.text(), int(self.port_input.text())
```

### Using the Dialog

```python
from your_module import ConnectionDialog

# Show dialog
dialog = ConnectionDialog(self)
if dialog.exec() == QDialog.DialogCode.Accepted:
    host, port = dialog.get_host_port()
    self.connect_to_server(host, port)
```

---

## Creating Custom Widgets

### Example: Custom Chat Widget

```python
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLineEdit
from src.ui.widgets import MessageBubble, RoundedButton, SeparatorLine
from src.ui.styles import get_stylesheet

class ChatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(get_stylesheet("dark"))
        self._create_ui()
    
    def _create_ui(self):
        """Create chat widget"""
        layout = QVBoxLayout(self)
        
        # Message display area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.message_widget = QWidget()
        self.message_layout = QVBoxLayout(self.message_widget)
        self.message_layout.addStretch()
        scroll.setWidget(self.message_widget)
        layout.addWidget(scroll)
        
        # Separator
        layout.addWidget(SeparatorLine())
        
        # Input area
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type a message...")
        
        send_btn = RoundedButton("Send", style="success")
        send_btn.clicked.connect(self.send_message)
        
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_btn)
        
        layout.addLayout(input_layout)
    
    def add_message(self, sender: str, text: str, timestamp: str, is_own: bool):
        """Add message to chat"""
        message = MessageBubble(sender, text, timestamp, is_own)
        # Insert before stretch
        self.message_layout.insertWidget(
            self.message_layout.count() - 1, message
        )
    
    def send_message(self):
        """Send message"""
        text = self.input_field.text()
        if text:
            # Process message
            self.input_field.clear()
```

### Using Custom Widget

```python
# In your main window
chat = ChatWidget()
main_layout.addWidget(chat)

# Add messages
chat.add_message("Alice", "Hello!", "14:30", False)
chat.add_message("You", "Hi there!", "14:31", True)
```

---

## Adding Animations

### Fade Animation on Message Arrival

```python
from src.ui.animations import SmoothFadeEffect

def on_message_received(sender, text, timestamp):
    """Handle incoming message with animation"""
    # Create message bubble
    message = MessageBubble(sender, text, timestamp, is_own=False)
    
    # Add to layout
    self.message_layout.addWidget(message)
    
    # Animate it in
    fade = SmoothFadeEffect(message, duration=500)
    fade.fade_in()
```

### Pulse Effect for Notifications

```python
from src.ui.animations import PulseEffect

def notify_user(count):
    """Show notification with pulse effect"""
    badge = StatusBadge(f"{count} new messages", "info")
    
    # Add to UI
    self.notification_area.addWidget(badge)
    
    # Pulse the badge
    pulse = PulseEffect(badge)
    pulse.start_pulse()
```

### Typing Indicator

```python
from src.ui.animations import TypingIndicator

def show_typing_indicator():
    """Show that user is typing"""
    typing = TypingIndicator()
    self.message_layout.addWidget(typing.label)
    typing.start()
    return typing

def hide_typing_indicator(typing):
    """Hide typing indicator"""
    typing.stop()
```

---

## Managing Preferences

### Load and Apply Preferences

```python
from src.ui.preferences import get_preferences, Theme, AnimationSpeed

def init_application():
    """Initialize app with saved preferences"""
    prefs = get_preferences()
    
    # Get theme preference
    theme = prefs.preferences.theme.value
    
    # Apply theme
    window.setStyleSheet(get_stylesheet(theme))
    
    # Apply animation settings
    if not prefs.preferences.animations.enabled:
        disable_all_animations()
```

### Save User Preferences

```python
def on_settings_changed(theme, animation_speed):
    """Save settings when changed"""
    prefs = get_preferences()
    
    # Update preferences
    prefs.preferences.set_theme(Theme(theme))
    prefs.set_animation_speed(AnimationSpeed[animation_speed])
    prefs.enable_animations(True)
    
    # Save to file
    prefs.save_preferences()
    
    # Apply changes immediately
    window.setStyleSheet(get_stylesheet(theme))
```

### Create Settings Dialog

```python
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from src.ui.widgets import RoundedButton, SeparatorLine
from src.ui.preferences import get_preferences, Theme, AnimationSpeed

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.prefs = get_preferences()
        self._create_ui()
    
    def _create_ui(self):
        layout = QVBoxLayout()
        
        # Theme selection
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["dark", "light"])
        self.theme_combo.setCurrentText(
            self.prefs.preferences.theme.value
        )
        theme_layout.addWidget(self.theme_combo)
        layout.addLayout(theme_layout)
        
        # Animation speed
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Animation Speed:"))
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["SLOW", "NORMAL", "FAST", "INSTANT"])
        self.speed_combo.setCurrentText(
            self.prefs.preferences.animations.speed.name
        )
        speed_layout.addWidget(self.speed_combo)
        layout.addLayout(speed_layout)
        
        # Separator
        layout.addWidget(SeparatorLine())
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = RoundedButton("Save", style="success")
        cancel_btn = RoundedButton("Cancel", style="secondary")
        
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def get_settings(self):
        """Get selected settings"""
        return {
            "theme": self.theme_combo.currentText(),
            "animation_speed": self.speed_combo.currentText(),
        }
```

---

## Troubleshooting

### Problem: Stylesheet Not Applied

**Solution:**
```python
# Apply stylesheet AFTER creating widget
widget = QLineEdit()
widget.setStyleSheet(get_stylesheet("dark"))  # After creation
```

### Problem: Animation Not Visible

**Solution:**
```python
# Ensure widget has size
widget.setMinimumSize(100, 50)

# Then apply animation
fade = SmoothFadeEffect(widget)
fade.fade_in()
```

### Problem: Colors Look Different

**Solution:**
- Check monitor color calibration
- Try different theme (light instead of dark)
- Verify hex color values in `preferences.py`

### Problem: Performance Issues

**Solution:**
```python
# Reduce animation count
from src.ui.preferences import get_preferences
prefs = get_preferences()
prefs.enable_animations(False)  # Disable if needed

# Or reduce animation speed
from src.ui.preferences import AnimationSpeed
prefs.set_animation_speed(AnimationSpeed.FAST)
```

---

## Best Practices

1. **Always apply stylesheet to main window:**
   ```python
   window.setStyleSheet(get_stylesheet("dark"))
   ```

2. **Use custom widgets consistently:**
   ```python
   # Good
   btn = RoundedButton("Click", style="primary")
   
   # Avoid
   btn = QPushButton("Click")
   ```

3. **Keep animations subtle:**
   ```python
   # Good - 300-500ms duration
   fade = SmoothFadeEffect(widget, duration=500)
   
   # Avoid - too long or too many
   fade = SmoothFadeEffect(widget, duration=3000)
   ```

4. **Save user preferences:**
   ```python
   prefs = get_preferences()
   prefs.apply_dark_theme()
   prefs.save_preferences()
   ```

---

## Next Steps

1. **Review the examples:**
   - `examples/widget_showcase.py`
   - `examples/animation_demo.py`

2. **Read the documentation:**
   - `VISUAL_DESIGN_QUICK_START.md`
   - `UI_IMPROVEMENTS.md`
   - `ANIMATIONS_GUIDE.md`

3. **Customize for your needs:**
   - Adjust colors in `src/ui/preferences.py`
   - Create custom widgets based on examples
   - Add animations to enhance UX

4. **Test thoroughly:**
   - Run `pytest tests/test_widgets.py`
   - Run `pytest tests/test_animations.py`
   - Test with both dark and light themes

---

## Summary

The visual design system is ready to use! Key steps:

1. Apply stylesheet: `window.setStyleSheet(get_stylesheet("dark"))`
2. Use custom widgets: `RoundedButton`, `MessageBubble`, etc.
3. Add animations: `SmoothFadeEffect`, `PulseEffect`, etc.
4. Manage preferences: `get_preferences().apply_dark_theme()`

Enjoy building beautiful interfaces! 🎨

---

**For more help, see:**
- `VISUAL_DESIGN_QUICK_START.md` - Quick reference
- `UI_IMPROVEMENTS.md` - Widget details
- `ANIMATIONS_GUIDE.md` - Animation details
- `DESIGN_SYSTEM.md` - Architecture
