import keyboard
from PyQt5.QtCore import QObject, pyqtSignal
import logging

logger = logging.getLogger(__name__)

class HotkeyService(QObject):
    """热键服务 - 负责全局热键注册和管理"""
    
    start_paste_requested = pyqtSignal()
    stop_paste_requested = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.start_hotkey = "ctrl+shift+p"
        self.stop_hotkey = "ctrl+shift+s"
        self._registered = False
        self._hotkeys = {}
    
    def register_hotkeys(self, start_hotkey=None, stop_hotkey=None):
        """注册热键"""
        # 先清除已注册的热键
        self.unregister_hotkeys()
        
        # 更新热键设置
        if start_hotkey:
            self.start_hotkey = self._normalize_hotkey(start_hotkey)
        if stop_hotkey:
            self.stop_hotkey = self._normalize_hotkey(stop_hotkey)
        
        try:
            # 注册开始热键
            self._hotkeys['start'] = keyboard.add_hotkey(
                self.start_hotkey, 
                self._on_start_requested
            )
            
            # 注册停止热键
            self._hotkeys['stop'] = keyboard.add_hotkey(
                self.stop_hotkey, 
                self._on_stop_requested
            )
            
            self._registered = True
            logger.info(f"热键注册成功: 开始={self.start_hotkey}, 停止={self.stop_hotkey}")
            return True
            
        except Exception as e:
            logger.error(f"热键注册失败: {e}")
            self.unregister_hotkeys()
            return False
    
    def unregister_hotkeys(self):
        """注销所有热键"""
        try:
            for hotkey_id in self._hotkeys.values():
                keyboard.remove_hotkey(hotkey_id)
            self._hotkeys.clear()
            self._registered = False
            logger.info("热键已注销")
        except Exception as e:
            logger.error(f"热键注销失败: {e}")
    
    def update_hotkeys(self, start_hotkey, stop_hotkey):
        """更新热键设置"""
        return self.register_hotkeys(start_hotkey, stop_hotkey)
    
    def _on_start_requested(self):
        """开始热键回调"""
        logger.info("开始热键触发")
        self.start_paste_requested.emit()
    
    def _on_stop_requested(self):
        """停止热键回调"""
        logger.info("停止热键触发")
        self.stop_paste_requested.emit()
    
    def _normalize_hotkey(self, hotkey_str):
        """标准化热键格式"""
        if not hotkey_str:
            return ""
        
        # 转换为小写，替换空格和特殊字符
        normalized = hotkey_str.lower().replace(' ', '+')
        # 确保常见的修饰键格式正确
        replacements = {
            'ctrl': 'ctrl',
            'control': 'ctrl',
            'alt': 'alt',
            'shift': 'shift',
            'windows': 'win',
            'cmd': 'command',
            ' ': '+'
        }
        
        for old, new in replacements.items():
            normalized = normalized.replace(old, new)
        
        return normalized
    
    def get_current_hotkeys(self):
        """获取当前热键设置"""
        return {
            'start': self.start_hotkey,
            'stop': self.stop_hotkey
        }
    
    def is_registered(self):
        """检查热键是否已注册"""
        return self._registered