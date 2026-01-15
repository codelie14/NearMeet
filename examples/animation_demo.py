"""Demo application for advanced animations"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from src.ui.styles import get_stylesheet
from src.ui.widgets import ChatHeaderFrame, SeparatorLine, RoundedButton
from src.ui.animations import (
    SmoothFadeEffect, SlideInAnimation, PulseEffect, ScaleEffect,
    NotificationBadge, TypingIndicator, FloatingLabelAnimation,
    apply_animation
)


class AnimationDemoWindow(QMainWindow):
    """Demo window for animations"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NearMeet Animation Demo")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet(get_stylesheet("dark"))
        
        self._create_demo()
    
    def _create_demo(self):
        """Create animation demos"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = ChatHeaderFrame("Animation Demo", "Advanced visual effects")
        layout.addWidget(header)
        layout.addWidget(SeparatorLine())
        
        # Content
        content_layout = QVBoxLayout()
        content_layout.setSpacing(16)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Section 1: Fade Effects
        content_layout.addWidget(self._create_fade_demo())
        content_layout.addWidget(SeparatorLine())
        
        # Section 2: Slide Effects
        content_layout.addWidget(self._create_slide_demo())
        content_layout.addWidget(SeparatorLine())
        
        # Section 3: Pulse Effects
        content_layout.addWidget(self._create_pulse_demo())
        content_layout.addWidget(SeparatorLine())
        
        # Section 4: Scale Effects
        content_layout.addWidget(self._create_scale_demo())
        content_layout.addWidget(SeparatorLine())
        
        # Section 5: Special Effects
        content_layout.addWidget(self._create_special_demo())
        
        content_layout.addStretch()
        
        scroll_widget = QWidget()
        scroll_widget.setLayout(content_layout)
        layout.addWidget(scroll_widget)
        
        self.setCentralWidget(widget)
    
    def _create_fade_demo(self):
        """Create fade effect demo"""
        frame = QFrame()
        layout = QHBoxLayout(frame)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("Fade Effects")
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        title.setFont(title_font)
        
        # Demo widget
        demo_label = QLabel("Fade Me!")
        demo_label.setStyleSheet("""
            QLabel {
                background-color: #0078d4;
                color: white;
                padding: 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        
        # Buttons
        fade_in_btn = RoundedButton("Fade In", style="primary")
        fade_out_btn = RoundedButton("Fade Out", style="danger")
        
        # Connect signals
        fade_effect = SmoothFadeEffect(demo_label)
        fade_in_btn.clicked.connect(fade_effect.fade_in)
        fade_out_btn.clicked.connect(fade_effect.fade_out)
        
        layout.addWidget(QLabel("Fade Effects"))
        layout.addWidget(demo_label)
        layout.addWidget(fade_in_btn)
        layout.addWidget(fade_out_btn)
        layout.addStretch()
        
        return frame
    
    def _create_slide_demo(self):
        """Create slide effect demo"""
        frame = QFrame()
        layout = QHBoxLayout(frame)
        layout.setSpacing(16)
        
        # Demo widget
        demo_label = QLabel("Slide Me!")
        demo_label.setStyleSheet("""
            QLabel {
                background-color: #107c10;
                color: white;
                padding: 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        demo_label.setMinimumWidth(150)
        
        # Buttons
        slide_left_btn = RoundedButton("Slide Left", style="primary")
        slide_right_btn = RoundedButton("Slide Right", style="primary")
        
        # Connect signals
        slide_effect = SlideInAnimation(demo_label)
        slide_left_btn.clicked.connect(slide_effect.slide_in_left)
        slide_right_btn.clicked.connect(slide_effect.slide_in_right)
        
        layout.addWidget(QLabel("Slide Effects"))
        layout.addWidget(demo_label)
        layout.addWidget(slide_left_btn)
        layout.addWidget(slide_right_btn)
        layout.addStretch()
        
        return frame
    
    def _create_pulse_demo(self):
        """Create pulse effect demo"""
        frame = QFrame()
        layout = QHBoxLayout(frame)
        layout.setSpacing(16)
        
        # Demo widget
        demo_label = QLabel("Pulsing!")
        demo_label.setStyleSheet("""
            QLabel {
                background-color: #f7630c;
                color: white;
                padding: 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        demo_label.setMinimumWidth(150)
        
        # Buttons
        start_btn = RoundedButton("Start Pulse", style="success")
        stop_btn = RoundedButton("Stop Pulse", style="danger")
        
        # Connect signals
        pulse_effect = PulseEffect(demo_label)
        start_btn.clicked.connect(pulse_effect.start_pulse)
        stop_btn.clicked.connect(pulse_effect.stop_pulse)
        
        layout.addWidget(QLabel("Pulse Effects"))
        layout.addWidget(demo_label)
        layout.addWidget(start_btn)
        layout.addWidget(stop_btn)
        layout.addStretch()
        
        return frame
    
    def _create_scale_demo(self):
        """Create scale effect demo"""
        frame = QFrame()
        layout = QHBoxLayout(frame)
        layout.setSpacing(16)
        
        # Demo widget
        demo_label = QLabel("Scale Me!")
        demo_label.setStyleSheet("""
            QLabel {
                background-color: #d13438;
                color: white;
                padding: 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        demo_label.setMinimumWidth(150)
        demo_label.setMinimumHeight(60)
        
        # Buttons
        scale_up_btn = RoundedButton("Scale Up", style="primary")
        scale_down_btn = RoundedButton("Scale Down", style="danger")
        
        # Connect signals
        scale_effect = ScaleEffect(demo_label, scale_factor=1.3)
        scale_up_btn.clicked.connect(scale_effect.scale_up)
        scale_down_btn.clicked.connect(scale_effect.scale_down)
        
        layout.addWidget(QLabel("Scale Effects"))
        layout.addWidget(demo_label)
        layout.addWidget(scale_up_btn)
        layout.addWidget(scale_down_btn)
        layout.addStretch()
        
        return frame
    
    def _create_special_demo(self):
        """Create special effects demo"""
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setSpacing(12)
        
        # Title
        title = QLabel("Special Effects")
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Row 1: Notification Badge
        row1 = QHBoxLayout()
        badge = NotificationBadge(5)
        badge_btn = RoundedButton("Update Badge", style="primary")
        badge_btn.clicked.connect(lambda: badge.set_count(10))
        row1.addWidget(QLabel("Notification Badge:"))
        row1.addWidget(badge)
        row1.addWidget(badge_btn)
        row1.addStretch()
        layout.addLayout(row1)
        
        # Row 2: Typing Indicator
        row2 = QHBoxLayout()
        typing = TypingIndicator()
        typing_start_btn = RoundedButton("Start Typing", style="success")
        typing_stop_btn = RoundedButton("Stop Typing", style="danger")
        typing_start_btn.clicked.connect(typing.start)
        typing_stop_btn.clicked.connect(typing.stop)
        row2.addWidget(QLabel("Typing Indicator:"))
        row2.addWidget(typing.label)
        row2.addWidget(typing_start_btn)
        row2.addWidget(typing_stop_btn)
        row2.addStretch()
        layout.addLayout(row2)
        
        return frame


def main():
    """Run the demo"""
    app = QApplication(sys.argv)
    window = AnimationDemoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
