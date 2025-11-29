from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal

class EditorPanel(QWidget):
    """编辑器面板组件"""
    
    content_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # 文本编辑器
        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText(
            "在此输入或粘贴您想要自动输入的内容...\n每行内容将会被自动输入，空行也会被输入为换行"
        )
        self.text_editor.textChanged.connect(self._on_text_changed)
        layout.addWidget(self.text_editor)
        
        # 统计信息
        self.stats_label = QLabel("内容长度: 0 字符, 行数: 0")
        layout.addWidget(self.stats_label)
        
        # 清空按钮
        self.clear_btn = QPushButton("清空内容")
        self.clear_btn.clicked.connect(self.clear_content)
        layout.addWidget(self.clear_btn)
    
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