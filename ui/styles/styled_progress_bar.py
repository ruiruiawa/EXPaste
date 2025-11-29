from PyQt5.QtWidgets import QProgressBar
from styles import STYLES

class StyledProgressBar(QProgressBar):
    """样式化进度条"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(STYLES["progress_bar"])