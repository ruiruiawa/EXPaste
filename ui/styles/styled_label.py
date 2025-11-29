from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from styles import STYLES

class StyledLabel(QLabel):
    """样式化标签 - 支持多种预设样式"""
    
    STYLES = {
        "title": STYLES["title_label"],
        "subtitle": STYLES["subtitle_label"],
        "normal": STYLES["normal_label"],
        "status": STYLES["status_label"],
        "success": STYLES["status_success"],
        "warning": STYLES["status_warning"],
        "error": STYLES["status_error"],
        "info": STYLES["status_info"]
    }
    
    def __init__(self, text="", style="normal", alignment=Qt.AlignLeft, parent=None):
        super().__init__(text, parent)
        self.set_style(style)
        self.setAlignment(alignment)
    
    def set_style(self, style):
        """设置标签样式"""
        if style in self.STYLES:
            self.setStyleSheet(self.STYLES[style])
        else:
            # 默认使用普通标签样式
            self.setStyleSheet(self.STYLES["normal"])