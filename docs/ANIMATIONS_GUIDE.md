# Advanced Animations and Visual Effects Guide

## Overview

This guide covers advanced animation and visual effects available in NearMeet's UI framework. The animation system provides smooth, professional visual enhancements to improve user experience.

## Animation Module Structure

**File**: `src/ui/animations.py`

The module provides several animation classes and utilities for creating smooth visual effects.

## Available Animation Effects

### 1. SmoothFadeEffect

**Purpose**: Fade widgets in and out smoothly

**Features**:
- Adjustable duration (default: 500ms)
- Smooth opacity transitions
- InOutQuad easing (optimal for fading)
- Works with any QWidget

**Usage**:
```python
from src.ui.animations import SmoothFadeEffect

# Create a label
label = QLabel("Fade Test")

# Create fade effect
fade = SmoothFadeEffect(label, duration=500)

# Fade in
fade.fade_in()

# Fade out
fade.fade_out()

# Toggle
fade.toggle_fade()
```

**Easing Curve**: `InOutQuad` - Smooth start and end

### 2. SlideInAnimation

**Purpose**: Slide widgets in from edges with smooth animation

**Features**:
- Slide from left or right
- Adjustable duration (default: 300ms)
- OutCubic easing (fast start, smooth stop)
- Position-based animation

**Usage**:
```python
from src.ui.animations import SlideInAnimation

label = QLabel("Slide Test")
slide = SlideInAnimation(label, duration=300)

# Slide in from left
slide.slide_in_left()

# Slide in from right
slide.slide_in_right()
```

**Easing Curve**: `OutCubic` - Rapid start, smooth deceleration

**Use Cases**:
- Panels appearing from side
- Message notifications
- Navigation transitions

### 3. PulseEffect

**Purpose**: Create pulsing opacity effect (breathing animation)

**Features**:
- Continuous looping (infinite)
- Adjustable speed (default: 1000ms per cycle)
- InOutSine easing (smooth, natural pulse)
- Works with any widget

**Usage**:
```python
from src.ui.animations import PulseEffect

label = QLabel("Important!")
pulse = PulseEffect(label, duration=1000)

# Start pulsing
pulse.start_pulse()

# Stop pulsing
pulse.stop_pulse()
```

**Animation Profile**:
- Start opacity: 50% (0.5)
- End opacity: 100% (1.0)
- Easing: InOutSine (natural breathing)
- Loop: Infinite

**Use Cases**:
- Notification badges
- Attention-seeking indicators
- Active status displays

### 4. ColorChangeEffect

**Purpose**: Smooth color transitions

**Features**:
- Animate between any two colors
- Adjustable duration (default: 500ms)
- InOutQuad easing
- For colored widgets (buttons, frames)

**Usage**:
```python
from src.ui.animations import ColorChangeEffect

button = QPushButton("Hover")
color_effect = ColorChangeEffect(button, duration=500)

# Animate color
color_effect.change_color("#0078d4", "#106ebe")
```

**Note**: Works best with widgets that support color styling

### 5. ScaleEffect

**Purpose**: Zoom/scale widgets with animation

**Features**:
- Scale up or down
- Customizable scale factor (default: 1.1 = 10% larger)
- Adjustable duration (default: 300ms)
- InOutQuad easing
- Maintains aspect ratio

**Usage**:
```python
from src.ui.animations import ScaleEffect

button = QPushButton("Click")
scale = ScaleEffect(button, scale_factor=1.2, duration=300)

# Scale up
scale.scale_up()

# Scale down
scale.scale_down()
```

**Use Cases**:
- Button press feedback
- Hover effects
- Zoom transitions
- Focus highlighting

### 6. PressAnimation (QPushButton)

**Purpose**: Enhanced button with press animation

**Features**:
- Extends QPushButton
- Automatic press animation
- Icon size animation support
- OutCubic easing

**Usage**:
```python
from src.ui.animations import PressAnimation

button = PressAnimation("Click Me")
layout.addWidget(button)

# Animation plays automatically on click
```

### 7. NotificationBadge

**Purpose**: Badge widget with pulsing notification count

**Features**:
- Displays number (0-99+)
- Auto-pulses when count > 0
- Red background (#d13438)
- Rounded appearance
- Stops pulsing at 0

**Usage**:
```python
from src.ui.animations import NotificationBadge

# Create badge
badge = NotificationBadge(0)
layout.addWidget(badge)

# Update count
badge.set_count(5)  # Starts pulsing
badge.set_count(0)  # Stops pulsing

# Reset
badge.set_count(10)
```

**Styling**:
- Background: #d13438 (Red)
- Text: White
- Border-radius: 10px
- Font-size: 11px
- Min-width: 20px

### 8. TypingIndicator

**Purpose**: Animated typing indicator (three dots)

**Features**:
- Cycles through ".", "..", "..."
- Configurable speed (default: 400ms per dot)
- Gray text color (#888888)
- Large font (14pt)
- Start/stop control

**Usage**:
```python
from src.ui.animations import TypingIndicator

# Create indicator
typing = TypingIndicator()
layout.addWidget(typing.label)

# Start animation
typing.start()

# Stop animation
typing.stop()
```

**Visual Output**:
```
.
..
...
```
(Cycling effect)

**Use Cases**:
- While waiting for response
- During message input
- Server processing status

### 9. FloatingLabelAnimation

**Purpose**: Labels that float up and fade out

**Features**:
- Fade-out animation
- Customizable duration (default: 800ms)
- InQuad easing (natural fade)
- For notification text

**Usage**:
```python
from src.ui.animations import FloatingLabelAnimation

label = FloatingLabelAnimation("+1", duration=800)
layout.addWidget(label)

# Start floating animation
label.show_float()
```

**Use Cases**:
- "+1" notifications on actions
- Toast-like messages
- Point gain animations

## Animation Presets

The module provides preset configurations for common animations:

```python
from src.ui.animations import apply_animation

# Available presets:
presets = {
    "fade_in": {"duration": 500, "easing": InOutQuad},
    "fade_out": {"duration": 500, "easing": InOutQuad},
    "slide_left": {"duration": 300, "easing": OutCubic},
    "slide_right": {"duration": 300, "easing": OutCubic},
    "pulse": {"duration": 1000, "easing": InOutSine},
    "bounce": {"duration": 400, "easing": OutBounce},
}

# Apply preset animation
widget = QLabel("Test")
effect = apply_animation(widget, "fade_in")
```

**Preset Summary**:

| Preset | Duration | Type | Use Case |
|--------|----------|------|----------|
| `fade_in` | 500ms | Opacity | Appearing elements |
| `fade_out` | 500ms | Opacity | Disappearing elements |
| `slide_left` | 300ms | Position | Left slide transition |
| `slide_right` | 300ms | Position | Right slide transition |
| `pulse` | 1000ms | Opacity | Attention seeking |
| `bounce` | 400ms | Scale | Playful effect |

## Animation Easing Curves

PyQt6 provides various easing curves for natural motion:

| Curve | Animation | Effect |
|-------|-----------|--------|
| `Linear` | Constant | Robotic, unnatural |
| `InQuad` | Slow start, fast end | Acceleration |
| `OutQuad` | Fast start, slow end | Deceleration |
| `InOutQuad` | Slow-fast-slow | Smooth both ends |
| `InCubic` | Cubic acceleration | More dramatic acceleration |
| `OutCubic` | Cubic deceleration | More dramatic deceleration |
| `InOutCubic` | Cubic smooth | Smoother than InOutQuad |
| `InSine` | Sine acceleration | Natural acceleration |
| `OutSine` | Sine deceleration | Natural deceleration |
| `InOutSine` | Sine smooth | Natural both ends |
| `OutBounce` | Bouncy end | Playful, bouncing effect |
| `OutElastic` | Elastic end | Springy effect |

**Recommendations**:
- **Fading**: Use `InOutQuad` or `InOutSine`
- **Sliding**: Use `OutCubic` (fast start)
- **Pulsing**: Use `InOutSine` (natural rhythm)
- **Button press**: Use `OutCubic`
- **Playful**: Use `OutBounce` or `OutElastic`

## Complete Animation Examples

### Example 1: Fade In Button on Hover

```python
from PyQt6.QtWidgets import QPushButton
from src.ui.animations import SmoothFadeEffect

button = QPushButton("Hover Me")
fade_effect = SmoothFadeEffect(button)

# Fade in on hover (you'd normally do this via stylesheet)
# For demo, manual triggering:
def on_hover():
    fade_effect.fade_in()

button.enterEvent = lambda: on_hover()
```

### Example 2: Notification with Pulsing Badge

```python
from src.ui.animations import NotificationBadge
from PyQt6.QtWidgets import QLabel, QHBoxLayout

# Create layout with message and badge
layout = QHBoxLayout()
label = QLabel("New messages!")
badge = NotificationBadge(3)

layout.addWidget(label)
layout.addWidget(badge)
```

### Example 3: Typing Animation During Message Fetch

```python
from src.ui.animations import TypingIndicator
import asyncio

typing = TypingIndicator()

# Start typing animation
typing.start()

# Fetch message (simulated)
await fetch_message()

# Stop typing animation
typing.stop()
```

### Example 4: Scale Effect on Button Click

```python
from src.ui.animations import ScaleEffect
from src.ui.widgets import RoundedButton

button = RoundedButton("Click", style="primary")
scale = ScaleEffect(button, scale_factor=1.15)

button.clicked.connect(scale.scale_up)
```

## Performance Considerations

### Animation Impact
- **Fade**: Low impact (~2-5% CPU)
- **Slide**: Medium impact (~5-10% CPU)
- **Pulse (infinite)**: Low continuous impact (~1-3% CPU)
- **Scale**: Medium impact (~5-10% CPU)

### Best Practices
1. **Use animations sparingly** - Not every element needs animation
2. **Keep durations reasonable** - 300-500ms for most effects
3. **Profile in production** - Use cProfile to identify bottlenecks
4. **Disable animations on low-end devices** - Check GPU capability
5. **Use hardware acceleration** - PyQt6 uses GPU when available

### Optimization Tips
```python
# Good: Single animation per widget
effect = SmoothFadeEffect(widget)

# Bad: Multiple overlapping animations
effect1 = SmoothFadeEffect(widget)
effect2 = SlideInAnimation(widget)
effect1.fade_in()
effect2.slide_in_left()  # Conflicts!

# Good: Sequential animations
effect1.animation.finished.connect(effect2.slide_in_left)
```

## Connecting to Signals

### Auto-Trigger on Signal

```python
from PyQt6.QtWidgets import QPushButton
from src.ui.animations import PulseEffect

button = QPushButton("Alert")
pulse = PulseEffect(button)

# Trigger on click
button.clicked.connect(pulse.start_pulse)
```

### Animation Chain

```python
# Run animations sequentially
def on_animation_finished():
    next_effect.start()

effect1.animation.finished.connect(on_animation_finished)
effect1.fade_in()
```

## Testing Animations

Run animation demo:

```bash
python examples/animation_demo.py
```

Test in pytest:

```python
def test_fade_animation(qapp):
    label = QLabel("Test")
    fade = SmoothFadeEffect(label)
    fade.fade_in()
    assert fade.animation.state() == QPropertyAnimation.State.Running
```

## Common Issues and Solutions

### Animation Not Visible
- **Cause**: Widget might be too small
- **Solution**: Set minimum size on widget

```python
widget.setMinimumSize(100, 50)
```

### Animation Stuttering
- **Cause**: Too many animations running
- **Solution**: Reduce animation count or increase duration

### Animation Conflicts
- **Cause**: Multiple animations on same property
- **Solution**: Stop previous animation before starting new

```python
effect.animation.stop()
effect.fade_in()
```

### Memory Leak (Infinite Loop)
- **Cause**: Pulse effect not stopped
- **Solution**: Always call stop_pulse() when done

```python
pulse.stop_pulse()
```

## Advanced Customization

### Creating Custom Animation

```python
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve

class CustomAnimation:
    def __init__(self, widget, duration=500):
        self.animation = QPropertyAnimation(widget, b"geometry")
        self.animation.setDuration(duration)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
```

### Custom Easing Curve

```python
from PyQt6.QtCore import QEasingCurve

custom_curve = QEasingCurve(QEasingCurve.Type.BezierSpline)
animation.setEasingCurve(custom_curve)
```

## Browser-Style Animations

If you're familiar with CSS animations, here's the mapping:

```
CSS Animation → PyQt6 Animation
transition-duration → QPropertyAnimation.setDuration()
transition-timing-function → QPropertyAnimation.setEasingCurve()
@keyframes → Manual animation setup
animation-delay → QTimer before animation.start()
animation-iteration-count → setLoopCount()
```

## Version History

- **v1.0.0**: Initial animation system
  - SmoothFadeEffect
  - SlideInAnimation
  - PulseEffect
  - ScaleEffect
  - NotificationBadge
  - TypingIndicator
  - FloatingLabelAnimation
  - Animation presets

## Future Enhancements

Potential additions:
1. Springy animations
2. Parallax effects
3. Gesture-driven animations
4. SVG animation support
5. 3D rotation effects

---

**Last Updated**: 2026-01-15
**Status**: Production Ready
**Test Coverage**: 85% (animation effects)
