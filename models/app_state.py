from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

class AppMode(Enum):
    """应用模式枚举"""
    FILE = "file"
    EDITOR = "editor"

class PasteStatus(Enum):
    """粘贴状态枚举"""
    IDLE = "idle"
    RUNNING = "running"
    STOPPED = "stopped"
    COMPLETED = "completed"

@dataclass
class AppSettings:
    """应用设置数据类"""
    paste_delay_ms: int = 10
    auto_start: bool = False
    start_hotkey: str = "ctrl+shift+p"
    stop_hotkey: str = "ctrl+shift+s"
    hotkeys_enabled: bool = True  # 新增：热键启用状态

@dataclass
class AppState:
    """应用状态数据类"""
    current_mode: AppMode = AppMode.FILE
    paste_status: PasteStatus = PasteStatus.IDLE
    current_file: Optional[str] = None
    editor_content: str = ""
    settings: AppSettings = field(default_factory=AppSettings)
    progress: int = 0
    status_message: str = "准备就绪"
    hotkey_status: str = "未注册" 