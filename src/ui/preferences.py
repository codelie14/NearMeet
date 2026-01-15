"""Visual preferences and theme configuration for NearMeet"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict
import json
from pathlib import Path


class Theme(Enum):
    """Available themes"""
    DARK = "dark"
    LIGHT = "light"


class AnimationSpeed(Enum):
    """Animation speed presets"""
    SLOW = 1.5      # 50% slower
    NORMAL = 1.0    # Default speed
    FAST = 0.7      # 30% faster
    INSTANT = 0.1   # Minimal animation


@dataclass
class ThemeColors:
    """Theme color configuration"""
    
    # Primary colors
    primary_color: str = "#0078d4"
    success_color: str = "#107c10"
    warning_color: str = "#f7630c"
    error_color: str = "#d13438"
    
    # Background colors
    background_primary: str = "#1e1e1e"
    background_secondary: str = "#2d2d2d"
    background_tertiary: str = "#3d3d3d"
    
    # Text colors
    text_primary: str = "#ffffff"
    text_secondary: str = "#aaaaaa"
    text_tertiary: str = "#888888"
    
    # Border colors
    border_color: str = "#404040"
    border_color_light: str = "#505050"
    
    @staticmethod
    def dark() -> "ThemeColors":
        """Create dark theme colors"""
        return ThemeColors(
            primary_color="#0078d4",
            success_color="#107c10",
            warning_color="#f7630c",
            error_color="#d13438",
            background_primary="#1e1e1e",
            background_secondary="#2d2d2d",
            background_tertiary="#3d3d3d",
            text_primary="#ffffff",
            text_secondary="#aaaaaa",
            text_tertiary="#888888",
            border_color="#404040",
            border_color_light="#505050",
        )
    
    @staticmethod
    def light() -> "ThemeColors":
        """Create light theme colors"""
        return ThemeColors(
            primary_color="#0078d4",
            success_color="#107c10",
            warning_color="#f7630c",
            error_color="#d13438",
            background_primary="#f3f3f3",
            background_secondary="#ffffff",
            background_tertiary="#f0f0f0",
            text_primary="#1e1e1e",
            text_secondary="#555555",
            text_tertiary="#666666",
            border_color="#e0e0e0",
            border_color_light="#d0d0d0",
        )
    
    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary"""
        return {
            "primary_color": self.primary_color,
            "success_color": self.success_color,
            "warning_color": self.warning_color,
            "error_color": self.error_color,
            "background_primary": self.background_primary,
            "background_secondary": self.background_secondary,
            "background_tertiary": self.background_tertiary,
            "text_primary": self.text_primary,
            "text_secondary": self.text_secondary,
            "text_tertiary": self.text_tertiary,
            "border_color": self.border_color,
            "border_color_light": self.border_color_light,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "ThemeColors":
        """Create from dictionary"""
        return cls(**data)


@dataclass
class AnimationConfig:
    """Animation configuration"""
    
    # Enable/disable animations
    enabled: bool = True
    
    # Global animation speed multiplier
    speed: AnimationSpeed = AnimationSpeed.NORMAL
    
    # Individual animation durations (in ms)
    fade_duration: int = 500
    slide_duration: int = 300
    pulse_duration: int = 1000
    scale_duration: int = 300
    press_duration: int = 150
    
    # Easing curve preferences
    fade_easing: str = "InOutQuad"
    slide_easing: str = "OutCubic"
    pulse_easing: str = "InOutSine"
    
    # Effects toggles
    enable_hover_effects: bool = True
    enable_focus_effects: bool = True
    enable_press_effects: bool = True
    enable_transitions: bool = True
    
    def get_duration(self, duration: int) -> int:
        """Get adjusted duration based on speed"""
        return int(duration * self.speed.value)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "enabled": self.enabled,
            "speed": self.speed.name,
            "fade_duration": self.fade_duration,
            "slide_duration": self.slide_duration,
            "pulse_duration": self.pulse_duration,
            "scale_duration": self.scale_duration,
            "press_duration": self.press_duration,
            "fade_easing": self.fade_easing,
            "slide_easing": self.slide_easing,
            "pulse_easing": self.pulse_easing,
            "enable_hover_effects": self.enable_hover_effects,
            "enable_focus_effects": self.enable_focus_effects,
            "enable_press_effects": self.enable_press_effects,
            "enable_transitions": self.enable_transitions,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "AnimationConfig":
        """Create from dictionary"""
        config = cls()
        config.enabled = data.get("enabled", True)
        config.speed = AnimationSpeed[data.get("speed", "NORMAL")]
        config.fade_duration = data.get("fade_duration", 500)
        config.slide_duration = data.get("slide_duration", 300)
        config.pulse_duration = data.get("pulse_duration", 1000)
        config.scale_duration = data.get("scale_duration", 300)
        config.press_duration = data.get("press_duration", 150)
        config.fade_easing = data.get("fade_easing", "InOutQuad")
        config.slide_easing = data.get("slide_easing", "OutCubic")
        config.pulse_easing = data.get("pulse_easing", "InOutSine")
        config.enable_hover_effects = data.get("enable_hover_effects", True)
        config.enable_focus_effects = data.get("enable_focus_effects", True)
        config.enable_press_effects = data.get("enable_press_effects", True)
        config.enable_transitions = data.get("enable_transitions", True)
        return config


@dataclass
class VisualsPreferences:
    """Complete visual preferences"""
    
    # Theme selection
    theme: Theme = Theme.DARK
    
    # Colors
    colors: ThemeColors = None
    
    # Animation settings
    animations: AnimationConfig = None
    
    # Font preferences
    font_family: str = "Segoe UI"
    font_size_base: int = 10
    font_size_title: int = 14
    font_size_label: int = 11
    
    # Spacing preferences
    spacing_xs: int = 4
    spacing_sm: int = 8
    spacing_md: int = 12
    spacing_lg: int = 16
    spacing_xl: int = 20
    
    # Border radius
    border_radius_sm: int = 2
    border_radius_md: int = 4
    border_radius_lg: int = 8
    
    # Opacity/transparency
    opacity_disabled: float = 0.5
    opacity_hover: float = 0.85
    opacity_focus: float = 0.9
    
    def __post_init__(self):
        """Initialize defaults"""
        if self.colors is None:
            self.colors = ThemeColors.dark() if self.theme == Theme.DARK else ThemeColors.light()
        if self.animations is None:
            self.animations = AnimationConfig()
    
    def set_theme(self, theme: Theme):
        """Set theme and update colors"""
        self.theme = theme
        if theme == Theme.DARK:
            self.colors = ThemeColors.dark()
        else:
            self.colors = ThemeColors.light()
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "theme": self.theme.value,
            "colors": self.colors.to_dict(),
            "animations": self.animations.to_dict(),
            "font_family": self.font_family,
            "font_size_base": self.font_size_base,
            "font_size_title": self.font_size_title,
            "font_size_label": self.font_size_label,
            "spacing_xs": self.spacing_xs,
            "spacing_sm": self.spacing_sm,
            "spacing_md": self.spacing_md,
            "spacing_lg": self.spacing_lg,
            "spacing_xl": self.spacing_xl,
            "border_radius_sm": self.border_radius_sm,
            "border_radius_md": self.border_radius_md,
            "border_radius_lg": self.border_radius_lg,
            "opacity_disabled": self.opacity_disabled,
            "opacity_hover": self.opacity_hover,
            "opacity_focus": self.opacity_focus,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "VisualsPreferences":
        """Create from dictionary"""
        prefs = cls()
        prefs.theme = Theme(data.get("theme", "dark"))
        prefs.colors = ThemeColors.from_dict(data.get("colors", {}))
        prefs.animations = AnimationConfig.from_dict(data.get("animations", {}))
        prefs.font_family = data.get("font_family", "Segoe UI")
        prefs.font_size_base = data.get("font_size_base", 10)
        prefs.font_size_title = data.get("font_size_title", 14)
        prefs.font_size_label = data.get("font_size_label", 11)
        prefs.spacing_xs = data.get("spacing_xs", 4)
        prefs.spacing_sm = data.get("spacing_sm", 8)
        prefs.spacing_md = data.get("spacing_md", 12)
        prefs.spacing_lg = data.get("spacing_lg", 16)
        prefs.spacing_xl = data.get("spacing_xl", 20)
        prefs.border_radius_sm = data.get("border_radius_sm", 2)
        prefs.border_radius_md = data.get("border_radius_md", 4)
        prefs.border_radius_lg = data.get("border_radius_lg", 8)
        prefs.opacity_disabled = data.get("opacity_disabled", 0.5)
        prefs.opacity_hover = data.get("opacity_hover", 0.85)
        prefs.opacity_focus = data.get("opacity_focus", 0.9)
        return prefs


class VisualsPreferencesManager:
    """Manager for visual preferences"""
    
    DEFAULT_PREFS_FILE = Path("config/visual_preferences.json")
    
    def __init__(self, prefs_file: Optional[Path] = None):
        """Initialize preferences manager"""
        self.prefs_file = prefs_file or self.DEFAULT_PREFS_FILE
        self.preferences = VisualsPreferences()
        self.load_preferences()
    
    def load_preferences(self) -> bool:
        """Load preferences from file"""
        if not self.prefs_file.exists():
            return False
        
        try:
            with open(self.prefs_file, 'r') as f:
                data = json.load(f)
            self.preferences = VisualsPreferences.from_dict(data)
            return True
        except Exception as e:
            print(f"Error loading preferences: {e}")
            return False
    
    def save_preferences(self) -> bool:
        """Save preferences to file"""
        try:
            self.prefs_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.prefs_file, 'w') as f:
                json.dump(self.preferences.to_dict(), f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving preferences: {e}")
            return False
    
    def reset_to_defaults(self):
        """Reset to default preferences"""
        self.preferences = VisualsPreferences()
        self.save_preferences()
    
    def apply_dark_theme(self):
        """Apply dark theme"""
        self.preferences.set_theme(Theme.DARK)
        self.save_preferences()
    
    def apply_light_theme(self):
        """Apply light theme"""
        self.preferences.set_theme(Theme.LIGHT)
        self.save_preferences()
    
    def set_animation_speed(self, speed: AnimationSpeed):
        """Set animation speed"""
        self.preferences.animations.speed = speed
        self.save_preferences()
    
    def enable_animations(self, enabled: bool = True):
        """Enable/disable animations"""
        self.preferences.animations.enabled = enabled
        self.save_preferences()


# Global preferences instance
_global_preferences: Optional[VisualsPreferencesManager] = None


def get_preferences() -> VisualsPreferencesManager:
    """Get global preferences instance"""
    global _global_preferences
    if _global_preferences is None:
        _global_preferences = VisualsPreferencesManager()
    return _global_preferences


def init_preferences(prefs_file: Optional[Path] = None) -> VisualsPreferencesManager:
    """Initialize global preferences"""
    global _global_preferences
    _global_preferences = VisualsPreferencesManager(prefs_file)
    return _global_preferences
