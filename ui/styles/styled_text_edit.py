from PyQt5.QtWidgets import QTextEdit
from styles import STYLES

class StyledTextEdit(QTextEdit):
    """样式化文本编辑器"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(STYLES["text_edit"])