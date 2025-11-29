from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class HeaderPanel(QWidget):
    """标题面板组件"""
    
    def __init__(self):
        super().__init__()
        self.hotkey_info_label = None
        self._setup_ui()
    
    def _setup_ui(self):
        """设置UI"""
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f0f7ff, stop:1 #e1eeff);
                border-radius: 10px;
                border-bottom: 1px solid rgba(209, 227, 255, 0.8);
            }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        
        # 标题行
        title_layout = QHBoxLayout()
        title_label = QLabel("EXPaste")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #1a2c4c;
            }
        """)
        
        version_badge = QLabel("v0.1.1")
        version_badge.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357abd);
                color: white;
                padding: 3px 10px;
                border-radius: 10px;
                font-size: 11px;
                font-weight: bold;
            }
        """)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(version_badge)
        title_layout.addStretch()
        
        # 热键信息
        self.hotkey_info_label = QLabel()
        self.hotkey_info_label.setStyleSheet("""
            QLabel {
                color: #6b7b9c;
                font-size: 13px;
            }
        """)
        
        layout.addLayout(title_layout)
        layout.addWidget(self.hotkey_info_label)
    
    def update_hotkey_info(self, hotkey_info):
        """更新热键信息"""
        self.hotkey_info_label.setText(f"现代化自动粘贴工具 - 热键: {hotkey_info}")