"""Modern QSS Stylesheet for NearMeet"""

# Dark Modern Theme
DARK_STYLESHEET = """
/* ======================== MAIN WINDOW ======================== */
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
}

QWidget {
    background-color: #1e1e1e;
    color: #ffffff;
}

/* ======================== MENU BAR ======================== */
QMenuBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-bottom: 1px solid #404040;
    padding: 4px;
}

QMenuBar::item:selected {
    background-color: #0078d4;
    border-radius: 3px;
}

QMenu {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #404040;
    border-radius: 5px;
}

QMenu::item:selected {
    background-color: #0078d4;
    padding: 4px 10px;
}

QMenu::item:pressed {
    background-color: #0066b2;
}

/* ======================== STATUS BAR ======================== */
QStatusBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-top: 1px solid #404040;
    padding: 3px;
}

/* ======================== LABELS ======================== */
QLabel {
    color: #ffffff;
    background-color: transparent;
}

QLabel#title {
    font-size: 16px;
    font-weight: bold;
    color: #0078d4;
}

/* ======================== LINE EDITS ======================== */
QLineEdit {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 2px solid #404040;
    border-radius: 5px;
    padding: 8px;
    font-size: 12px;
    selection-background-color: #0078d4;
}

QLineEdit:focus {
    border: 2px solid #0078d4;
    background-color: #2d2d2d;
}

QLineEdit:hover {
    border: 2px solid #505050;
}

/* ======================== TEXT EDITS ======================== */
QTextEdit {
    background-color: #252525;
    color: #ffffff;
    border: 1px solid #404040;
    border-radius: 5px;
    padding: 8px;
    font-size: 12px;
    font-family: 'Segoe UI', Arial;
}

QTextEdit:focus {
    border: 1px solid #0078d4;
}

QTextEdit:hover {
    border: 1px solid #505050;
}

/* ======================== PUSH BUTTONS ======================== */
QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
    font-size: 12px;
    font-weight: bold;
    outline: none;
}

QPushButton:hover {
    background-color: #1084d8;
}

QPushButton:pressed {
    background-color: #0066b2;
}

QPushButton:focus {
    border: 2px solid #ffffff;
}

QPushButton:disabled {
    background-color: #404040;
    color: #808080;
}

QPushButton#secondary {
    background-color: #404040;
    color: #ffffff;
}

QPushButton#secondary:hover {
    background-color: #505050;
}

QPushButton#secondary:pressed {
    background-color: #303030;
}

QPushButton#danger {
    background-color: #d13438;
    color: #ffffff;
}

QPushButton#danger:hover {
    background-color: #d13438;
    opacity: 0.9;
}

QPushButton#success {
    background-color: #107c10;
    color: #ffffff;
}

QPushButton#success:hover {
    background-color: #127513;
}

/* ======================== LIST WIDGET ======================== */
QListWidget {
    background-color: #252525;
    color: #ffffff;
    border: 1px solid #404040;
    border-radius: 5px;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #404040;
}

QListWidget::item:selected {
    background-color: #0078d4;
    border-radius: 3px;
}

QListWidget::item:hover {
    background-color: #303030;
}

/* ======================== SCROLL BARS ======================== */
QScrollBar:vertical {
    background-color: #252525;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #505050;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #606060;
}

QScrollBar::handle:vertical:pressed {
    background-color: #707070;
}

QScrollBar:horizontal {
    background-color: #252525;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #505050;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #606060;
}

QScrollBar::handle:horizontal:pressed {
    background-color: #707070;
}

QScrollBar::sub-line, QScrollBar::add-line {
    border: none;
    background: none;
}

/* ======================== COMBO BOX ======================== */
QComboBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 2px solid #404040;
    border-radius: 5px;
    padding: 5px;
}

QComboBox:hover {
    border: 2px solid #505050;
}

QComboBox:focus {
    border: 2px solid #0078d4;
}

QComboBox::drop-down {
    border: none;
    background-color: transparent;
}

QComboBox::down-arrow {
    image: url(down-arrow.png);
}

QComboBox QAbstractItemView {
    background-color: #2d2d2d;
    color: #ffffff;
    selection-background-color: #0078d4;
}

/* ======================== CHECK BOX ======================== */
QCheckBox {
    color: #ffffff;
    spacing: 8px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #404040;
    border-radius: 3px;
    background-color: #2d2d2d;
}

QCheckBox::indicator:hover {
    border: 2px solid #505050;
}

QCheckBox::indicator:checked {
    background-color: #0078d4;
    border: 2px solid #0078d4;
}

/* ======================== RADIO BUTTON ======================== */
QRadioButton {
    color: #ffffff;
    spacing: 8px;
}

QRadioButton::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #404040;
    border-radius: 9px;
    background-color: #2d2d2d;
}

QRadioButton::indicator:hover {
    border: 2px solid #505050;
}

QRadioButton::indicator:checked {
    background-color: #0078d4;
    border: 2px solid #0078d4;
}

/* ======================== SPIN BOX ======================== */
QSpinBox, QDoubleSpinBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 2px solid #404040;
    border-radius: 5px;
    padding: 5px;
}

QSpinBox:focus, QDoubleSpinBox:focus {
    border: 2px solid #0078d4;
}

/* ======================== SLIDER ======================== */
QSlider::groove:horizontal {
    background-color: #404040;
    border-radius: 5px;
    height: 8px;
}

QSlider::handle:horizontal {
    background-color: #0078d4;
    width: 18px;
    margin: -5px 0;
    border-radius: 9px;
}

QSlider::handle:horizontal:hover {
    background-color: #1084d8;
}

/* ======================== PROGRESS BAR ======================== */
QProgressBar {
    background-color: #404040;
    border: 1px solid #505050;
    border-radius: 5px;
    text-align: center;
    color: #ffffff;
}

QProgressBar::chunk {
    background-color: #0078d4;
    border-radius: 4px;
}

/* ======================== TAB WIDGET ======================== */
QTabWidget::pane {
    border: 1px solid #404040;
    background-color: #1e1e1e;
}

QTabBar::tab {
    background-color: #2d2d2d;
    color: #ffffff;
    padding: 8px 20px;
    margin-right: 2px;
    border: none;
}

QTabBar::tab:selected {
    background-color: #0078d4;
    color: #ffffff;
}

QTabBar::tab:hover {
    background-color: #303030;
}

/* ======================== DIALOG ======================== */
QDialog {
    background-color: #1e1e1e;
    color: #ffffff;
}

/* ======================== FRAME ======================== */
QFrame {
    background-color: transparent;
    border: none;
}

QFrame#header {
    background-color: #2d2d2d;
    border-bottom: 1px solid #404040;
}

QFrame#footer {
    background-color: #2d2d2d;
    border-top: 1px solid #404040;
}

/* ======================== SEPARATORS ======================== */
QFrame[frameShape="4"],
QFrame[frameShape="5"] {
    color: #404040;
}

/* ======================== TOOL TIP ======================== */
QToolTip {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #404040;
    border-radius: 3px;
    padding: 4px;
}

/* ======================== CUSTOM CLASSES ======================== */

/* Chat Message Container */
QFrame#chatMessage {
    background-color: #252525;
    border-radius: 8px;
    padding: 12px;
    margin: 4px 0px;
}

QFrame#chatMessage:hover {
    background-color: #2d2d2d;
}

/* User Status Indicator */
QLabel#statusOnline {
    color: #107c10;
    font-weight: bold;
}

QLabel#statusOffline {
    color: #d13438;
    font-weight: bold;
}

QLabel#statusAway {
    color: #f7630c;
    font-weight: bold;
}

/* Notification Badge */
QLabel#badge {
    background-color: #d13438;
    color: #ffffff;
    border-radius: 10px;
    padding: 2px 6px;
    font-weight: bold;
    font-size: 10px;
}

/* Timestamp */
QLabel#timestamp {
    color: #a0a0a0;
    font-size: 10px;
}

/* Username */
QLabel#username {
    color: #0078d4;
    font-weight: bold;
    font-size: 12px;
}
"""

# Light Theme (Alternative)
LIGHT_STYLESHEET = """
/* ======================== MAIN WINDOW ======================== */
QMainWindow {
    background-color: #f3f3f3;
    color: #000000;
}

QWidget {
    background-color: #f3f3f3;
    color: #000000;
}

/* ======================== LABELS ======================== */
QLabel {
    color: #000000;
    background-color: transparent;
}

QLabel#title {
    font-size: 16px;
    font-weight: bold;
    color: #0078d4;
}

/* ======================== LINE EDITS ======================== */
QLineEdit {
    background-color: #ffffff;
    color: #000000;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    padding: 8px;
    font-size: 12px;
}

QLineEdit:focus {
    border: 2px solid #0078d4;
}

/* ======================== TEXT EDITS ======================== */
QTextEdit {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    padding: 8px;
}

QTextEdit:focus {
    border: 1px solid #0078d4;
}

/* ======================== PUSH BUTTONS ======================== */
QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1084d8;
}

QPushButton:pressed {
    background-color: #0066b2;
}

/* ======================== LIST WIDGET ======================== */
QListWidget {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
}

QListWidget::item:selected {
    background-color: #0078d4;
    color: #ffffff;
}

QListWidget::item:hover {
    background-color: #f0f0f0;
}
"""


def get_stylesheet(theme: str = "dark") -> str:
    """
    Get stylesheet for specified theme.
    
    Args:
        theme: Theme name ('dark' or 'light')
    
    Returns:
        QSS stylesheet string
    """
    if theme.lower() == "light":
        return LIGHT_STYLESHEET
    return DARK_STYLESHEET
