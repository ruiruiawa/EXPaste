from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from styles import STYLES

class DragDropHint(QLabel):
    """拖拽提示组件 - 使用样式化组件"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """设置UI"""
        self.setText("💡 提示: 您也可以直接将文本文件拖拽到此窗口")
        self.setAlignment(Qt.AlignCenter)
        self.set_normal_style()
    
    def set_dragging_style(self):
        """设置拖拽时的样式"""
        self.setStyleSheet(STYLES["drag_hint_active"])
    
    def set_normal_style(self):
        """设置正常样式"""
        self.setStyleSheet(STYLES["drag_hint"])