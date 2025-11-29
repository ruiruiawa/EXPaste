from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QTextEdit, QFileDialog)
from PyQt5.QtCore import pyqtSignal

from core.file_manager import FileManager

class FilePanel(QWidget):
    """文件面板组件"""
    
    file_selected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self._init_ui()
    
    def _init_ui(self):
        layout = QVBoxLayout(self)
        
        # 文件信息卡片
        file_info_widget = self._create_file_info_widget()
        layout.addWidget(file_info_widget)
        
        # 预览卡片
        preview_widget = self._create_preview_widget()
        layout.addWidget(preview_widget)
    
    def _create_file_info_widget(self):
        """创建文件信息卡片"""
        widget = QWidget()
        widget.setStyleSheet("""
            QWidget {
                background: rgba(255, 255, 255, 0.7);
                border-radius: 14px;
                border: 1px solid rgba(255, 255, 255, 0.5);
            }
        """)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 文件信息内容
        file_info_content = QWidget()
        file_info_content.setStyleSheet("""
            QWidget {
                background: rgba(237, 245, 255, 0.6);
                border-radius: 10px;
            }
        """)
        file_info_content_layout = QVBoxLayout(file_info_content)
        
        self.file_name_label = QLabel("📄 当前文件: 未选择")
        self.file_lines_label = QLabel("📊 行数: -")
        self.file_path_label = QLabel("📁 路径: -")
        
        for label in [self.file_name_label, self.file_lines_label, self.file_path_label]:
            label.setStyleSheet("color: #4a5a7a; font-size: 13px; padding: 5px;")
            file_info_content_layout.addWidget(label)
        
        layout.addWidget(file_info_content)
        
        # 选择文件按钮
        self.select_btn = QPushButton("选择文件")
        self.select_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6b7b9c, stop:1 #4a5a7a);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357abd);
            }
        """)
        self.select_btn.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_btn)
        
        return widget
    
    def _create_preview_widget(self):
        """创建预览卡片"""
        widget = QWidget()
        widget.setStyleSheet("""
            QWidget {
                background: rgba(255, 255, 255, 0.7);
                border-radius: 14px;
                border: 1px solid rgba(255, 255, 255, 0.5);
            }
        """)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(15, 15, 15, 15)
        
        preview_label = QLabel("👁️ 内容预览")
        preview_label.setStyleSheet("font-weight: bold; color: #2d3c5c;")
        layout.addWidget(preview_label)
        
        self.preview_text = QTextEdit()
        self.preview_text.setStyleSheet("""
            QTextEdit {
                background: rgba(255, 255, 255, 0.8);
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 6px;
                padding: 8px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
        """)
        self.preview_text.setReadOnly(True)
        self.preview_text.setMaximumHeight(120)
        layout.addWidget(self.preview_text)
        
        return widget
    
    def open_file_dialog(self):
        """打开文件选择对话框"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择文本文件", "", "文本文件 (*.txt);;所有文件 (*)"
        )
        if file_path:
            self.file_selected.emit(file_path)
            self.update_file_info(file_path)
    
    def update_file_info(self, file_path):
        """更新文件信息显示"""
        self.current_file = file_path
        file_info = FileManager.get_file_info(file_path)
        
        if file_info['exists']:
            import os
            self.file_name_label.setText(f"📄 当前文件: {os.path.basename(file_path)}")
            self.file_lines_label.setText(f"📊 行数: {file_info['line_count']}")
            self.file_path_label.setText(f"📁 路径: {file_path}")
            self.preview_text.setPlainText(file_info['content_preview'])
        else:
            self._clear_file_info()
    
    def _clear_file_info(self):
        """清空文件信息"""
        self.file_name_label.setText("📄 当前文件: 未选择")
        self.file_lines_label.setText("📊 行数: -")
        self.file_path_label.setText("📁 路径: -")
        self.preview_text.clear()
    
    def set_enabled(self, enabled):
        """设置组件可用状态"""
        self.select_btn.setEnabled(enabled)