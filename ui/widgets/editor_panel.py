import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QTextEdit, QPushButton)
from PyQt5.QtCore import pyqtSignal

from styles import STYLES

logger = logging.getLogger(__name__)

class EditorPanel(QWidget):
    """编辑器面板组件 - 使用样式化组件"""
    
    content_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.text_editor = None
        self.stats_label = None
        self.clear_btn = None
        self._init_ui()
    
    def _init_ui(self):
        """初始化UI"""
        self.setStyleSheet(STYLES["card"])
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 编辑器标签
        editor_label = QLabel("✏️ 文本编辑器")
        editor_label.setStyleSheet(STYLES["subtitle_label"])
        layout.addWidget(editor_label)
        
        # 文本编辑器
        self.text_editor = QTextEdit()
        self.text_editor.setStyleSheet(STYLES["text_edit"])
        self.text_editor.setPlaceholderText(
            "在此输入或粘贴您想要自动输入的内容...\n"
            "每行内容将会被自动输入，空行也会被输入为换行"
        )
        self.text_editor.textChanged.connect(self._on_text_changed)
        layout.addWidget(self.text_editor)
        
        # 统计信息和清空按钮
        bottom_layout = QHBoxLayout()
        
        self.stats_label = QLabel("内容长度: 0 字符, 行数: 0")
        self.stats_label.setStyleSheet(STYLES["status_label"])
        
        self.clear_btn = QPushButton("清空内容")
        self.clear_btn.setStyleSheet(STYLES["button_secondary"])
        self.clear_btn.clicked.connect(self.clear_content)
        
        bottom_layout.addWidget(self.stats_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.clear_btn)
        
        layout.addLayout(bottom_layout)
    
    def _on_text_changed(self):
        """文本变化处理"""
        content = self.get_content()
        char_count = len(content)
        line_count = len(content.splitlines()) if content else 0
        self.stats_label.setText(f"内容长度: {char_count} 字符, 行数: {line_count}")
        self.content_changed.emit(content)
    
    def get_content(self):
        """获取编辑器内容"""
        return self.text_editor.toPlainText()
    
    def clear_content(self):
        """清空内容"""
        self.text_editor.clear()
    
    def set_enabled(self, enabled):
        """设置组件可用状态"""
        self.text_editor.setEnabled(enabled)
        self.clear_btn.setEnabled(enabled)
    
    def set_content(self, content):
        """设置内容"""
        self.text_editor.setPlainText(content)