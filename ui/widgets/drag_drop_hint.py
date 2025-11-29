from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class DragDropHint(QLabel):
    """拖拽提示组件"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """设置UI"""
        self.setText("💡 提示: 您也可以直接将文本文件拖拽到此窗口")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                background: rgba(255, 255, 255, 0.7);
                border: 2px dashed #4a90e2;
                border-radius: 8px;
                padding: 10px;
                color: #4a5a7a;
                font-size: 12px;
                text-align: center;
            }
        """)
    
    def set_dragging_style(self):
        """设置拖拽时的样式"""
        self.setStyleSheet("""
            QLabel {
                background: rgba(74, 144, 226, 0.1);
                border: 2px dashed #4a90e2;
                border-radius: 8px;
                padding: 10px;
                color: #4a90e2;
                font-size: 12px;
                text-align: center;
                font-weight: bold;
            }
        """)
    
    def set_normal_style(self):
        """设置正常样式"""
        self.setStyleSheet("""
            QLabel {
                background: rgba(255, 255, 255, 0.7);
                border: 2px dashed #4a90e2;
                border-radius: 8px;
                padding: 10px;
                color: #4a5a7a;
                font-size: 12px;
                text-align: center;
            }
        """)