import os
import tempfile
import logging
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QLabel, QComboBox, QMenuBar, QAction, QMessageBox,
                            QFileDialog)
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QIcon, QDragEnterEvent, QDropEvent

from models.app_state import AppState, AppMode
from core.paste_engine import PasteEngine
from core.file_manager import FileManager
from ui.widgets.file_panel import FilePanel
from ui.widgets.editor_panel import EditorPanel
from ui.widgets.control_panel import ControlPanel
from ui.widgets.drag_drop_hint import DragDropHint
from ui.widgets.mode_selector import ModeSelector
from ui.widgets.header_panel import HeaderPanel
from ui.dialogs.settings_dialog import SettingsDialog
from services.hotkey_service import HotkeyService
from services.drag_drop_service import DragDropService
from utils.helpers import format_hotkey_display
from styles import STYLES

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    """主窗口 - 使用组件化的UI架构"""
    
    def __init__(self):
        super().__init__()
        self.app_state = AppState()
        self.paste_engine = PasteEngine()
        self.hotkey_service = HotkeyService()
        self.drag_drop_service = DragDropService()
        self.worker_thread = None
        self.temp_files = []  # 用于存储临时文件路径
        
        self._setup_ui()
        self._connect_signals()
        self._setup_hotkeys()
        self._enable_drag_drop()
    
    def _setup_ui(self):
        """初始化UI - 使用组件化的架构"""
        self.setWindowTitle("EXPaste v0.1.1")
        self.setGeometry(100, 100, 800, 700)
        
        # 应用主窗口样式
        self.setStyleSheet(STYLES["main_window"])
        
        # 设置图标
        self._set_window_icon()
        
        # 创建中央组件
        central_widget = QWidget()
        central_widget.setStyleSheet(STYLES["central_widget"])
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 使用HeaderPanel组件
        self.header_panel = HeaderPanel()
        layout.addWidget(self.header_panel)
        
        # 使用ModeSelector组件
        self.mode_selector = ModeSelector()
        layout.addWidget(self.mode_selector)
        
        # 热键状态显示
        self.hotkey_status_label = QLabel("热键状态: 准备中...")
        self.hotkey_status_label.setStyleSheet(STYLES["status_normal"])
        self._update_hotkey_status()
        layout.addWidget(self.hotkey_status_label)
        
        # 使用DragDropHint组件
        self.drag_drop_hint = DragDropHint()
        self.drag_drop_hint.setVisible(True)
        layout.addWidget(self.drag_drop_hint)
        
        # 使用各个面板组件
        self.file_panel = FilePanel()
        self.editor_panel = EditorPanel()
        self.control_panel = ControlPanel()
        
        layout.addWidget(self.file_panel)
        layout.addWidget(self.editor_panel)
        layout.addWidget(self.control_panel)
        
        # 初始状态：显示文件面板，隐藏编辑器面板
        self.editor_panel.setVisible(False)
        
        # 创建菜单
        self._create_menu()
        
        # 更新标题区域的热键信息
        self._update_title_hotkey_info()
    
    def _set_window_icon(self):
        """设置窗口图标"""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 尝试在不同位置查找图标
            possible_paths = [
                os.path.join(current_dir, '..', 'images', 'icon.ico'),
                os.path.join(current_dir, '..', 'res', 'icon.ico'),
                os.path.join(current_dir, 'icon.ico'),
                os.path.join(os.path.dirname(current_dir), 'images', 'icon.ico'),
                os.path.join(os.path.dirname(current_dir), 'res', 'icon.ico')
            ]
            
            for icon_path in possible_paths:
                if os.path.exists(icon_path):
                    self.setWindowIcon(QIcon(icon_path))
                    break
        except Exception as e:
            logger.warning(f"设置窗口图标失败: {e}")
    
    def _create_menu(self):
        """创建菜单栏"""
        menubar = self.menuBar()
        menubar.setStyleSheet(STYLES["menu_bar"])
        
        # 文件菜单
        file_menu = menubar.addMenu('文件')
        open_action = QAction('打开', self)
        open_action.triggered.connect(self._on_menu_open_file)
        file_menu.addAction(open_action)
        
        # 设置菜单
        settings_menu = menubar.addMenu('设置')
        preferences_action = QAction('偏好设置', self)
        preferences_action.triggered.connect(self._open_settings)
        settings_menu.addAction(preferences_action)
        
        # 帮助菜单
        help_menu = menubar.addMenu('帮助')
        about_action = QAction('关于', self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
    
    def _connect_signals(self):
        """连接信号槽"""
        # ModeSelector信号
        self.mode_selector.mode_changed.connect(self._on_mode_changed)
        
        # 文件面板信号
        self.file_panel.file_selected.connect(self._on_file_selected)
        
        # 编辑器面板信号
        self.editor_panel.content_changed.connect(self._on_editor_content_changed)
        
        # 控制面板信号
        self.control_panel.start_requested.connect(self._start_paste)
        self.control_panel.stop_requested.connect(self._stop_paste)
        
        # 粘贴引擎信号
        self.paste_engine.progress_updated.connect(self._on_progress_updated)
        self.paste_engine.status_changed.connect(self._on_status_changed)
        self.paste_engine.finished.connect(self._on_paste_finished)
        self.paste_engine.error_occurred.connect(self._on_paste_error)
        
        # 热键服务信号
        self.hotkey_service.start_paste_requested.connect(self._on_hotkey_start)
        self.hotkey_service.stop_paste_requested.connect(self._on_hotkey_stop)
        
        # 拖拽服务信号
        self.drag_drop_service.drag_entered.connect(self._on_drag_entered)
        self.drag_drop_service.drag_left.connect(self._on_drag_left)
        self.drag_drop_service.file_dropped.connect(self._on_file_dropped)
    
    def _setup_hotkeys(self):
        """设置热键"""
        if self.app_state.settings.hotkeys_enabled:
            success = self.hotkey_service.register_hotkeys(
                self.app_state.settings.start_hotkey,
                self.app_state.settings.stop_hotkey
            )
            
            if success:
                logger.info("热键注册成功")
                self._update_hotkey_status(True)
            else:
                logger.error("热键注册失败")
                self._update_hotkey_status(False)
                QMessageBox.warning(
                    self, 
                    "热键注册失败", 
                    "无法注册全局热键，热键功能将不可用。\n"
                    "可能的原因：\n"
                    "1. 热键已被其他程序占用\n"
                    "2. 热键格式不正确\n"
                    "3. 程序权限不足\n\n"
                    "请在设置中检查热键配置。"
                )
        else:
            self._update_hotkey_status(False)
    
    def _enable_drag_drop(self):
        """启用拖放功能"""
        self.setAcceptDrops(True)
    
    def _update_hotkey_status(self, success=None):
        """更新热键状态显示"""
        if success is None:
            # 如果没有提供状态，根据当前设置判断
            if self.app_state.settings.hotkeys_enabled and self.hotkey_service.is_registered():
                status = "热键已注册"
                style = STYLES["status_success"]
            elif self.app_state.settings.hotkeys_enabled:
                status = "热键注册失败"
                style = STYLES["status_error"]
            else:
                status = "热键已禁用"
                style = STYLES["status_normal"]
        else:
            if success:
                status = "热键已注册"
                style = STYLES["status_success"]
            else:
                status = "热键注册失败"
                style = STYLES["status_error"]
        
        self.hotkey_status_label.setText(f"热键状态: {status}")
        self.hotkey_status_label.setStyleSheet(style)
    
    def _update_title_hotkey_info(self):
        """更新标题区域的热键信息显示"""
        hotkey_info = self._get_hotkey_info()
        self.header_panel.update_hotkey_info(hotkey_info)
    
    def _get_hotkey_info(self):
        """获取热键信息字符串"""
        if self.app_state.settings.hotkeys_enabled:
            start_key = format_hotkey_display(self.app_state.settings.start_hotkey)
            stop_key = format_hotkey_display(self.app_state.settings.stop_hotkey)
            return f"{start_key} 开始 / {stop_key} 停止"
        else:
            return "热键已禁用"
    
    # 拖拽事件处理
    def dragEnterEvent(self, event: QDragEnterEvent):
        """拖拽进入事件"""
        if self.drag_drop_service.handle_drag_enter(event):
            self.drag_drop_hint.set_dragging_style()
    
    def dragLeaveEvent(self, event):
        """拖拽离开事件"""
        self.drag_drop_hint.set_normal_style()
        event.accept()
    
    def dropEvent(self, event: QDropEvent):
        """拖放事件"""
        self.drag_drop_service.handle_drop(event)
    
    def _on_drag_entered(self):
        """拖拽进入"""
        self.drag_drop_hint.set_dragging_style()
    
    def _on_drag_left(self):
        """拖拽离开"""
        self.drag_drop_hint.set_normal_style()
    
    def _on_file_dropped(self, file_path):
        """文件拖放处理"""
        try:
            # 切换到文件模式
            self.mode_selector.set_mode("file")
            
            # 更新文件信息
            self.file_panel.load_file(file_path)
            
            # 更新应用状态
            self.app_state.current_file = file_path
            
            # 显示成功消息
            file_name = os.path.basename(file_path)
            self.control_panel.update_status(f"已加载文件: {file_name}")
            
            logger.info(f"通过拖拽加载文件: {file_path}")
            
        except Exception as e:
            error_msg = f"加载文件失败: {str(e)}"
            QMessageBox.critical(self, "错误", error_msg)
            logger.error(error_msg)
    
    def _on_mode_changed(self, mode):
        """模式切换处理"""
        if mode == "file":
            self.file_panel.setVisible(True)
            self.editor_panel.setVisible(False)
            self.app_state.current_mode = AppMode.FILE
            # 显示拖拽提示
            self.drag_drop_hint.setVisible(True)
        else:
            self.file_panel.setVisible(False)
            self.editor_panel.setVisible(True)
            self.app_state.current_mode = AppMode.EDITOR
            # 隐藏拖拽提示（编辑模式下不需要）
            self.drag_drop_hint.setVisible(False)
    
    def _on_menu_open_file(self):
        """菜单打开文件"""
        self.file_panel.open_file_dialog()
    
    def _on_file_selected(self, file_path):
        """文件选择处理"""
        self.app_state.current_file = file_path
    
    def _on_editor_content_changed(self, content):
        """编辑器内容变化处理"""
        self.app_state.editor_content = content
    
    def _on_hotkey_start(self):
        """热键开始粘贴"""
        if not self.control_panel.can_start():
            # 如果已经开始，忽略热键
            return
        
        logger.info("热键触发开始粘贴")
        self._start_paste()
    
    def _on_hotkey_stop(self):
        """热键停止粘贴"""
        if not self.control_panel.can_stop():
            # 如果已经停止，忽略热键
            return
        
        logger.info("热键触发停止粘贴")
        self._stop_paste()
    
    def _start_paste(self):
        """开始粘贴"""
        # 验证内容
        if self.app_state.current_mode == AppMode.FILE:
            if not self.app_state.current_file:
                QMessageBox.warning(self, "错误", "请先选择文本文件")
                return
            content_source = self.app_state.current_file
        else:
            content = self.editor_panel.get_content().strip()
            if not content:
                QMessageBox.warning(self, "错误", "请输入要粘贴的文本内容")
                return
            
            # 创建临时文件
            try:
                temp_file = tempfile.NamedTemporaryFile(
                    mode='w', encoding='utf-8', 
                    suffix='.txt', delete=False
                )
                temp_file.write(content)
                temp_file.close()
                content_source = temp_file.name
                self.temp_files.append(temp_file.name)  # 记录临时文件以便后续清理
            except Exception as e:
                QMessageBox.critical(self, "错误", f"创建临时文件失败: {str(e)}")
                return
        
        # 更新UI状态
        self.control_panel.set_running_state(True)
        self.file_panel.set_enabled(False)
        self.editor_panel.set_enabled(False)
        
        # 在工作线程中运行粘贴引擎
        self.worker_thread = QThread()
        self.paste_engine.moveToThread(self.worker_thread)
        
        # 连接线程信号
        self.worker_thread.started.connect(
            lambda: self.paste_engine.start_paste(content_source)
        )
        
        # 启动线程
        self.worker_thread.start()
    
    def _stop_paste(self):
        """停止粘贴"""
        self.paste_engine.stop_paste()
        self._cleanup_after_paste()
    
    def _on_progress_updated(self, progress, message):
        """进度更新"""
        self.control_panel.update_progress(progress, message)
    
    def _on_status_changed(self, message):
        """状态变化"""
        self.control_panel.update_status(message)
    
    def _on_paste_finished(self):
        """粘贴完成"""
        self._cleanup_after_paste()
        self.control_panel.update_status("操作完成")
    
    def _on_paste_error(self, error_msg):
        """粘贴错误"""
        QMessageBox.critical(self, "错误", error_msg)
        self._cleanup_after_paste()
    
    def _cleanup_after_paste(self):
        """粘贴后清理"""
        # 清理工作线程
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait(1000)  # 等待1秒
            self.worker_thread = None
        
        # 清理临时文件
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception as e:
                logger.warning(f"删除临时文件失败: {e}")
        self.temp_files.clear()
        
        # 恢复UI状态
        self.control_panel.set_running_state(False)
        self.file_panel.set_enabled(True)
        self.editor_panel.set_enabled(True)
    
    def _open_settings(self):
        """打开设置"""
        current_settings = {
            'paste_delay_ms': getattr(self.paste_engine, 'delay_ms', 10),
            'hotkeys_enabled': self.app_state.settings.hotkeys_enabled,
            'start_hotkey': self.app_state.settings.start_hotkey,
            'stop_hotkey': self.app_state.settings.stop_hotkey
        }
        
        dialog = SettingsDialog(self, current_settings)
        
        if dialog.exec_():
            new_settings = dialog.get_settings()
            
            # 应用新的延迟设置
            new_delay = new_settings.get('paste_delay_ms', 10)
            if hasattr(self.paste_engine, 'set_delay'):
                self.paste_engine.set_delay(new_delay)
            self.app_state.settings.paste_delay_ms = new_delay
            
            # 应用热键设置
            hotkeys_enabled = new_settings.get('hotkeys_enabled', True)
            start_hotkey = new_settings.get('start_hotkey', 'ctrl+shift+p')
            stop_hotkey = new_settings.get('stop_hotkey', 'ctrl+shift+s')
            
            # 更新热键设置
            self.app_state.settings.hotkeys_enabled = hotkeys_enabled
            self.app_state.settings.start_hotkey = start_hotkey
            self.app_state.settings.stop_hotkey = stop_hotkey
            
            # 重新设置热键
            if hotkeys_enabled:
                success = self.hotkey_service.update_hotkeys(start_hotkey, stop_hotkey)
                if not success:
                    QMessageBox.warning(self, "热键更新失败", "无法注册新的热键设置")
            else:
                self.hotkey_service.unregister_hotkeys()
            
            # 更新所有热键相关的显示
            self._update_hotkey_status()
            self._update_title_hotkey_info()
            
            QMessageBox.information(self, "成功", "设置已保存！")
    
    def _show_about(self):
        """显示关于信息"""
        QMessageBox.about(self, "关于 EXPaste", 
                         "EXPaste v0.1.1\n\n"
                         "现代化自动粘贴工具\n"
                         "支持文件模式和编辑模式输入\n\n"
                         "新功能：支持拖拽文件到窗口")
    
    def closeEvent(self, event):
        """关闭事件"""
        if self.worker_thread and self.worker_thread.isRunning():
            self._stop_paste()
        
        # 注销热键
        self.hotkey_service.unregister_hotkeys()
        
        # 清理临时文件
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception:
                pass
        
        event.accept()