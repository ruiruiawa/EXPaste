from PyQt5.QtWidgets import QPushButton
from styles import STYLES

class StyledButton(QPushButton):
    """样式化按钮 - 支持多种预设样式"""
    
    STYLES = {
        "primary": STYLES["button_primary"],
        "secondary": STYLES["button_secondary"],
        "success": STYLES["button_success"],
        "warning": STYLES["button_warning"],
        "small": STYLES["button_small"]
    }
    
    def __init__(self, text="", style="primary", parent=None):
        super().__init__(text, parent)
        self.set_style(style)
    
    def set_style(self, style):
        """设置按钮样式"""
        if style in self.STYLES:
            self.setStyleSheet(self.STYLES[style])
        else:
            # 默认使用主按钮样式
            self.setStyleSheet(self.STYLES["primary"])