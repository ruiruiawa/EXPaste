import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QProgressBar)
from PyQt5.QtCore import Qt, pyqtSignal

from styles import STYLES

logger = logging.getLogger(__name__)

class ControlPanel(QWidget):
    """控制面板组件 - 使用样式化组件"""
    
    start_requested = pyqtSignal()
    stop_requested = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.progress_bar = None
        self.status_label = None
        self.start_btn = None
        self.stop_btn = None
        self._init_ui()
    
    def _init_ui(self):
        """初始化UI"""
        self.setStyleSheet(STYLES["card"])
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(STYLES["progress_bar"])
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # 状态标签
        self.status_label = QLabel("准备就绪")
        self.status_label.setStyleSheet(STYLES["status_label"])
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # 控制按钮
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("开始粘贴")
        self.start_btn.setStyleSheet(STYLES["button_success"])
        self.start_btn.clicked.connect(self.start_requested.emit)
        
        self.stop_btn = QPushButton("停止")
        self.stop_btn.setStyleSheet(STYLES["button_warning"])
        self.stop_btn.clicked.connect(self.stop_requested.emit)
        self.stop_btn.setEnabled(False)
        
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # 提示信息
        tip_label = QLabel("💡 提示: 点击开始后，请将光标移动到目标输入框")
        tip_label.setStyleSheet(STYLES["status_info"])
        tip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(tip_label)
    
    def set_running_state(self, running):
        """设置运行状态"""
        self.start_btn.setEnabled(not running)
        self.stop_btn.setEnabled(running)
        self.progress_bar.setVisible(running)
        
        if not running:
            self.progress_bar.setValue(0)
    
    def update_progress(self, progress, message):
        """更新进度"""
        self.progress_bar.setValue(progress)
        self.status_label.setText(message)
    
    def update_status(self, message):
        """更新状态消息"""
        self.status_label.setText(message)
    
    def can_start(self):
        """检查是否可以开始"""
        return self.start_btn.isEnabled()
    
    def can_stop(self):
        """检查是否可以停止"""
        return self.stop_btn.isEnabled()