# ui_window.py
import os
import tempfile
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QProgressBar, QTextEdit, 
                            QMessageBox, QFileDialog, QGroupBox, QTabWidget)
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QIcon
from core import PasteWorker, FileManager
from styles import STYLES

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker_thread = None
        self.worker = None
        self.init_ui()
        self.check_file()
    
    def init_ui(self):
        self.setWindowTitle("EXPaste v0.1.0")
        self.setGeometry(100, 100, 700, 600)
        self.setStyleSheet(STYLES["main_window"])
        
        # 设置窗口图标
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'images', 'icon.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"图标文件未找到: {icon_path}")

        central_widget = QWidget()
        central_widget.setStyleSheet(STYLES["central_widget"])
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题
        title_label = QLabel("EXPaste")
        title_label.setStyleSheet(STYLES["title_label"])
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 创建选项卡
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #cbd5e0;
                border-radius: 8px;
                background: white;
            }
            QTabBar::tab {
                background: #e2e8f0;
                border: 1px solid #cbd5e0;
                padding: 8px 16px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #667eea;
                color: white;
            }
            QTabBar::tab:hover:!selected {
                background: #cbd5e0;
            }
        """)
        
        # 文件输入选项卡
        self.file_tab = QWidget()
        self.setup_file_tab()
        self.tab_widget.addTab(self.file_tab, "文件输入")
        
        # 文本编辑选项卡
        self.editor_tab = QWidget()
        self.setup_editor_tab()
        self.tab_widget.addTab(self.editor_tab, "文本编辑")
        
        layout.addWidget(self.tab_widget)
        
        # 进度组
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(STYLES["progress_bar"])
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("准备就绪")
        self.status_label.setStyleSheet(STYLES["normal_label"])
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # 控制按钮
        control_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("开始粘贴")
        self.start_btn.setStyleSheet(STYLES["button_primary"])
        self.start_btn.clicked.connect(self.start_paste)
        
        self.stop_btn = QPushButton("停止")
        self.stop_btn.setStyleSheet(STYLES["button_secondary"])
        self.stop_btn.clicked.connect(self.stop_paste)
        self.stop_btn.setEnabled(False)
        
        control_layout.addWidget(self.start_btn)
        control_layout.addWidget(self.stop_btn)
        layout.addLayout(control_layout)
        
        # 提示信息
        tip_label = QLabel("提示: 点击开始后，请将光标移动到目标输入框")
        tip_label.setStyleSheet("QLabel { color: #718096; font-size: 12px; }")
        tip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(tip_label)
    
    def setup_file_tab(self):
        layout = QVBoxLayout(self.file_tab)
        
        # 文件信息组
        file_group = QGroupBox("文件信息")
        file_group.setStyleSheet("QGroupBox { font-weight: bold; color: #2d3748; }")
        file_layout = QVBoxLayout()
        
        self.file_info_label = QLabel()
        self.file_info_label.setStyleSheet(STYLES["normal_label"])
        self.file_info_label.setWordWrap(True)
        file_layout.addWidget(self.file_info_label)
        
        btn_layout = QHBoxLayout()
        self.select_btn = QPushButton("选择文件")
        self.select_btn.setStyleSheet(STYLES["button_secondary"])
        self.select_btn.clicked.connect(self.select_file)
        
        btn_layout.addWidget(self.select_btn)
        file_layout.addLayout(btn_layout)
        
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)
        
        # 预览组
        preview_group = QGroupBox("内容预览")
        preview_group.setStyleSheet("QGroupBox { font-weight: bold; color: #2d3748; }")
        preview_layout = QVBoxLayout()
        
        self.preview_text = QTextEdit()
        self.preview_text.setStyleSheet(STYLES["text_edit"])
        self.preview_text.setReadOnly(True)
        self.preview_text.setMaximumHeight(150)
        preview_layout.addWidget(self.preview_text)
        
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
    
    def setup_editor_tab(self):
        layout = QVBoxLayout(self.editor_tab)
        
        # 编辑器组
        editor_group = QGroupBox("文本编辑器")
        editor_group.setStyleSheet("QGroupBox { font-weight: bold; color: #2d3748; }")
        editor_layout = QVBoxLayout()
        
        # 编辑器说明
        editor_info = QLabel("在此处直接输入或粘贴文本内容，然后点击'开始粘贴'按钮")
        editor_info.setStyleSheet("QLabel { color: #718096; font-size: 12px; padding: 5px; }")
        editor_layout.addWidget(editor_info)
        
        # 文本编辑器
        self.text_editor = QTextEdit()
        self.text_editor.setStyleSheet(STYLES["text_edit"])
        self.text_editor.setPlaceholderText("在此输入或粘贴您想要自动输入的内容...\n每行内容将会被自动输入，空行也会被输入为换行")
        editor_layout.addWidget(self.text_editor)
        
        # 编辑器按钮
        editor_btn_layout = QHBoxLayout()
        
        self.clear_btn = QPushButton("清空内容")
        self.clear_btn.setStyleSheet(STYLES["button_secondary"])
        self.clear_btn.clicked.connect(self.clear_editor)
        
        
        editor_layout.addLayout(editor_btn_layout)
        editor_group.setLayout(editor_layout)
        layout.addWidget(editor_group)
        
        # 编辑器预览
        editor_preview_group = QGroupBox("编辑器内容统计")
        editor_preview_group.setStyleSheet("QGroupBox { font-weight: bold; color: #2d3748; }")
        editor_preview_layout = QVBoxLayout()
        
        self.editor_info_label = QLabel("内容长度: 0 字符, 行数: 0")
        self.editor_info_label.setStyleSheet(STYLES["normal_label"])
        editor_preview_layout.addWidget(self.editor_info_label)
        
        editor_preview_group.setLayout(editor_preview_layout)
        layout.addWidget(editor_preview_group)
        
        # 连接文本变化信号
        self.text_editor.textChanged.connect(self.update_editor_info)
    
    def update_editor_info(self):
        content = self.text_editor.toPlainText()
        char_count = len(content)
        line_count = len(content.splitlines()) if content else 0
        
        self.editor_info_label.setText(f"内容长度: {char_count} 字符, 行数: {line_count}")
    
    def clear_editor(self):
        self.text_editor.clear()
    
    def load_example_content(self):
        example_content = """# 这是一个示例文本
# 请在此处输入您想要自动输入的内容
# 每行内容将会被自动输入
# 空行也会被输入为换行

Hello, World!
这是示例内容
第三行文本"""
        self.text_editor.setPlainText(example_content)
    
    def check_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, 'text.txt')
        self.update_file_info()
    
    def update_file_info(self):
        file_info = FileManager.get_file_info(self.file_path)
        
        if file_info['exists']:
            info_text = f"📄 当前文件: {os.path.basename(self.file_path)}\n"
            info_text += f"📊 行数: {file_info['line_count']}\n"
            info_text += f"📁 路径: {self.file_path}"
            self.preview_text.setPlainText(file_info['content_preview'])
        else:
            info_text = "请选择文件"
            self.preview_text.clear()
        
        self.file_info_label.setText(info_text)
    
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择文本文件", "", "文本文件 (*.txt);;所有文件 (*)"
        )
        if file_path:
            self.file_path = file_path
            self.update_file_info()
    
    def create_default_file(self):
        if FileManager.create_default_file(self.file_path):
            QMessageBox.information(self, "成功", "已创建示例文件！")
            self.update_file_info()
        else:
            QMessageBox.warning(self, "错误", "创建文件失败")
    
    def start_paste(self):
        current_tab = self.tab_widget.currentIndex()
        
        if current_tab == 0:  # 文件输入选项卡
            if not os.path.exists(self.file_path):
                QMessageBox.warning(self, "错误", "请先选择或创建文本文件")
                return
            content_source = self.file_path
        else:  # 文本编辑选项卡
            content = self.text_editor.toPlainText().strip()
            if not content:
                QMessageBox.warning(self, "错误", "请输入要粘贴的文本内容")
                return
            
            # 创建临时文件保存编辑器内容
            temp_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', 
                                                   suffix='.txt', delete=False)
            temp_file.write(content)
            temp_file.close()
            content_source = temp_file.name
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.select_btn.setEnabled(False)
        self.create_btn.setEnabled(False)
        self.clear_btn.setEnabled(False)
        self.load_example_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # 创建工作线程
        self.worker_thread = QThread()
        self.worker = PasteWorker(content_source)
        self.worker.moveToThread(self.worker_thread)
        
        self.worker_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        
        self.worker_thread.start()
    
    def stop_paste(self):
        if self.worker:
            self.worker.stop()
        self.on_finished()
    
    def update_progress(self, value, message):
        self.progress_bar.setValue(value)
        self.status_label.setText(message)
    
    def on_finished(self):
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
        
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.select_btn.setEnabled(True)
        self.create_btn.setEnabled(True)
        self.clear_btn.setEnabled(True)
        self.load_example_btn.setEnabled(True)
        self.status_label.setText("操作完成")
    
    def on_error(self, error_msg):
        QMessageBox.critical(self, "错误", error_msg)
        self.on_finished()
    
    def closeEvent(self, event):
        if self.worker_thread and self.worker_thread.isRunning():
            self.stop_paste()
        event.accept()