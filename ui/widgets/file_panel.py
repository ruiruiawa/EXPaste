import os
import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QTextEdit, QFileDialog)
from PyQt5.QtCore import pyqtSignal

from core.file_manager import FileManager
from styles import STYLES

logger = logging.getLogger(__name__)

class FilePanel(QWidget):
    """文件面板组件 - 使用样式化组件"""
    
    file_selected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self._init_ui()
    
    def _init_ui(self):
        """初始化UI"""
        self.setStyleSheet(STYLES["card"])
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 文件信息卡片
        file_info_widget = self._create_file_info_widget()
        layout.addWidget(file_info_widget)
        
        # 预览卡片
        preview_widget = self._create_preview_widget()
        layout.addWidget(preview_widget)
    
    def _create_file_info_widget(self):
        """创建文件信息卡片"""
        widget = QWidget()
        widget.setStyleSheet(STYLES["card"])
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
        self.file_name_label.setStyleSheet(STYLES["normal_label"])
        
        self.file_lines_label = QLabel("📊 行数: -")
        self.file_lines_label.setStyleSheet(STYLES["normal_label"])
        
        self.file_path_label = QLabel("📁 路径: -")
        self.file_path_label.setStyleSheet(STYLES["normal_label"])
        
        for label in [self.file_name_label, self.file_lines_label, self.file_path_label]:
            file_info_content_layout.addWidget(label)
        
        layout.addWidget(file_info_content)
        
        # 选择文件按钮
        self.select_btn = QPushButton("选择文件")
        self.select_btn.setStyleSheet(STYLES["button_primary"])
        self.select_btn.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_btn)
        
        return widget
    
    def _create_preview_widget(self):
        """创建预览卡片"""
        widget = QWidget()
        widget.setStyleSheet(STYLES["card"])
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(15, 15, 15, 15)
        
        preview_label = QLabel("👁️ 内容预览")
        preview_label.setStyleSheet(STYLES["subtitle_label"])
        layout.addWidget(preview_label)
        
        self.preview_text = QTextEdit()
        self.preview_text.setStyleSheet(STYLES["text_edit"])
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
            self.update_file_info(file_path)
            self.file_selected.emit(file_path)
    
    def update_file_info(self, file_path):
        """更新文件信息显示"""
        self.current_file = file_path
        file_info = FileManager.get_file_info(file_path)
        
        if file_info['exists']:
            self.file_name_label.setText(f"📄 当前文件: {os.path.basename(file_path)}")
            self.file_lines_label.setText(f"📊 行数: {file_info['line_count']}")
            self.file_path_label.setText(f"📁 路径: {file_path}")
            self.preview_text.setPlainText(file_info['content_preview'])
            logger.info(f"文件加载成功: {file_path}")
        else:
            self._clear_file_info()
            logger.warning(f"文件不存在或无法读取: {file_path}")
    
    def _clear_file_info(self):
        """清空文件信息"""
        self.file_name_label.setText("📄 当前文件: 未选择")
        self.file_lines_label.setText("📊 行数: -")
        self.file_path_label.setText("📁 路径: -")
        self.preview_text.clear()
    
    def set_enabled(self, enabled):
        """设置组件可用状态"""
        self.select_btn.setEnabled(enabled)
    
    def load_file(self, file_path):
        """加载文件（用于拖拽功能）"""
        self.update_file_info(file_path)
        self.file_selected.emit(file_path)