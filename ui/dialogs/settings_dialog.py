from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QGroupBox, QCheckBox, QLabel,
                            QFormLayout, QLineEdit, QSpinBox, QHBoxLayout, 
                            QPushButton, QMessageBox, QWidget)
from PyQt5.QtCore import Qt
from utils.helpers import validate_hotkey

class SettingsDialog(QDialog):
    """设置对话框"""
    
    def __init__(self, parent=None, current_settings=None):
        super().__init__(parent)
        self.current_settings = current_settings or {}
        self.settings = {}
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("设置")
        self.setFixedSize(450, 550)
        
        layout = QVBoxLayout(self)
        
        # 基本设置
        basic_group = QGroupBox("基本设置")
        basic_layout = QFormLayout()
        
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(1, 1000)
        self.delay_spin.setSuffix(" 毫秒/字符")
        self.delay_spin.setToolTip("设置每个字符输入的间隔时间，值越小速度越快")
        
        basic_layout.addRow("输入间隔:", self.delay_spin)
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
        # 热键设置
        hotkey_group = QGroupBox("热键设置")
        hotkey_layout = QFormLayout()
        
        self.hotkeys_enabled_check = QCheckBox("启用全局热键")
        self.hotkeys_enabled_check.setChecked(True)
        
        self.start_hotkey_edit = QLineEdit()
        self.start_hotkey_edit.setPlaceholderText("例如: ctrl+shift+p")
        
        self.stop_hotkey_edit = QLineEdit()
        self.stop_hotkey_edit.setPlaceholderText("例如: ctrl+shift+s")
        
        hotkey_info = QLabel("注意：热键可能会与其他程序冲突，请选择不常用的组合")
        hotkey_info.setStyleSheet("color: #666; font-size: 11px;")
        hotkey_info.setWordWrap(True)
        
        hotkey_layout.addRow(self.hotkeys_enabled_check)
        hotkey_layout.addRow("开始粘贴热键:", self.start_hotkey_edit)
        hotkey_layout.addRow("停止粘贴热键:", self.stop_hotkey_edit)
        hotkey_layout.addRow(hotkey_info)
        
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        # 按钮
        button_layout = QHBoxLayout()
        self.save_btn = QPushButton("保存")
        self.save_btn.clicked.connect(self._save_settings)
        
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.cancel_btn)
        layout.addLayout(button_layout)
        
        self._load_current_settings()
    
    def _load_current_settings(self):
        """加载当前设置"""
        if self.current_settings:
            self.delay_spin.setValue(self.current_settings.get('paste_delay_ms', 10))
            self.hotkeys_enabled_check.setChecked(self.current_settings.get('hotkeys_enabled', True))
            self.start_hotkey_edit.setText(self.current_settings.get('start_hotkey', 'ctrl+shift+p'))
            self.stop_hotkey_edit.setText(self.current_settings.get('stop_hotkey', 'ctrl+shift+s'))
    
    def _save_settings(self):
        """保存设置"""
        try:
            # 验证热键格式
            start_hotkey = self.start_hotkey_edit.text().strip()
            stop_hotkey = self.stop_hotkey_edit.text().strip()
            
            if self.hotkeys_enabled_check.isChecked():
                if start_hotkey and not validate_hotkey(start_hotkey):
                    QMessageBox.warning(self, "错误", "开始热键格式不正确")
                    return
                
                if stop_hotkey and not validate_hotkey(stop_hotkey):
                    QMessageBox.warning(self, "错误", "停止热键格式不正确")
                    return
                
                if start_hotkey == stop_hotkey:
                    QMessageBox.warning(self, "错误", "开始和停止热键不能相同")
                    return
            
            self.settings = {
                'paste_delay_ms': self.delay_spin.value(),
                'hotkeys_enabled': self.hotkeys_enabled_check.isChecked(),
                'start_hotkey': start_hotkey,
                'stop_hotkey': stop_hotkey
            }
            
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存设置失败: {str(e)}")
    
    def get_settings(self):
        """获取设置"""
        return self.settings