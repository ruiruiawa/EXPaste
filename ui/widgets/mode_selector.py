from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import pyqtSignal

class ModeSelector(QWidget):
    """模式选择器组件"""
    
    mode_changed = pyqtSignal(str)  # 模式变化信号
    
    def __init__(self):
        super().__init__()
        self.mode_combo = None
        self._setup_ui()
    
    def _setup_ui(self):
        """设置UI"""
        self.setStyleSheet("""
            QWidget {
                background: rgba(255, 255, 255, 0.7);
                border-radius: 14px;
                border: 1px solid rgba(255, 255, 255, 0.5);
            }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        
        # 控制面板
        control_layout = QHBoxLayout()
        control_label = QLabel("输入模式:")
        control_label.setStyleSheet("""
            QLabel {
                color: #4a5a7a;
                font-weight: bold;
                min-width: 80px;
            }
        """)
        
        self.mode_combo = QComboBox()
        self.mode_combo.setStyleSheet("""
            QComboBox {
                background: rgba(255, 255, 255, 0.9);
                border: 1px solid rgba(209, 227, 255, 0.8);
                border-radius: 10px;
                padding: 8px 12px;
                color: #2d3c5c;
                font-size: 13px;
                min-width: 180px;
            }
            QComboBox:focus {
                border-color: #4a90e2;
            }
        """)
        self.mode_combo.addItem("📁 文件模式", "file")
        self.mode_combo.addItem("✏️ 编辑模式", "editor")
        self.mode_combo.currentIndexChanged.connect(self._on_mode_changed)
        
        control_layout.addWidget(control_label)
        control_layout.addWidget(self.mode_combo)
        control_layout.addStretch()
        
        layout.addLayout(control_layout)
    
    def _on_mode_changed(self, index):
        """模式切换处理"""
        mode = self.mode_combo.currentData()
        self.mode_changed.emit(mode)
    
    def set_mode(self, mode):
        """设置当前模式"""
        if mode == "file":
            self.mode_combo.setCurrentIndex(0)
        else:
            self.mode_combo.setCurrentIndex(1)