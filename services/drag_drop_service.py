import os
import logging
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

logger = logging.getLogger(__name__)

class DragDropService(QObject):
    """拖拽服务 - 负责处理文件拖拽功能"""
    
    drag_entered = pyqtSignal()  # 拖拽进入信号
    drag_left = pyqtSignal()     # 拖拽离开信号
    file_dropped = pyqtSignal(str)  # 文件路径
    
    def __init__(self):
        super().__init__()
    
    def handle_drag_enter(self, event: QDragEnterEvent):
        """处理拖拽进入事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls and self._is_text_file(urls[0].toLocalFile()):
                event.acceptProposedAction()
                self.drag_entered.emit()
                return True
        event.ignore()
        return False
    
    def handle_drop(self, event: QDropEvent):
        """处理拖放事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if self._is_text_file(file_path):
                    self.file_dropped.emit(file_path)
                    event.acceptProposedAction()
                    return True
        event.ignore()
        return False
    
    def _is_text_file(self, file_path):
        """检查文件是否为文本文件"""
        # 检查文件扩展名
        text_extensions = {'.txt', '.log', '.csv', '.json', '.xml', '.html', 
                          '.htm', '.md', '.ini', '.cfg', '.conf', '.py', '.js',
                          '.java', '.c', '.cpp', '.h', '.hpp', '.php', '.rb',
                          '.go', '.rs', '.swift', '.kt', '.ts', '.sh', '.bat'}
        
        _, ext = os.path.splitext(file_path)
        if ext.lower() in text_extensions:
            return True
        
        # 如果不是已知的文本扩展名，尝试检查文件内容
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # 尝试读取前几行，检查是否包含不可打印字符
                content = f.read(1024)  # 读取前1KB
                # 如果包含大量不可打印字符（非文本文件特征），则拒绝
                non_printable = sum(1 for c in content if ord(c) < 32 and c not in '\t\n\r')
                if non_printable / len(content) > 0.1:  # 如果超过10%是不可打印字符
                    return False
                return True
        except:
            return False