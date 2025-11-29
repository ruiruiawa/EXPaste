from PyQt5.QtWidgets import QComboBox
from styles import STYLES

class StyledComboBox(QComboBox):
    """样式化下拉框"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(STYLES["combo_box"])