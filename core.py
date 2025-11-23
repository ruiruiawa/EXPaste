import os
import time
import keyboard
from PyQt5.QtCore import QObject, pyqtSignal

class PasteWorker(QObject):
    progress = pyqtSignal(int, str)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    
    def __init__(self, file_path, delay=3):
        super().__init__()
        self.file_path = file_path
        self.delay = delay
        self.is_running = True
    
    def run(self):
        try:
            if not os.path.exists(self.file_path):
                self.error.emit(f"文件 '{self.file_path}' 不存在")
                return
            
            # 倒计时
            for i in range(self.delay, 0, -1):
                if not self.is_running:
                    return
                self.progress.emit(0, f"倒计时: {i}秒...")
                time.sleep(1)
            
            self.progress.emit(0, "开始输入内容...")
            
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                total_lines = len(lines)
                
                for i, line in enumerate(lines, 1):
                    if not self.is_running:
                        return
                    
                    clean_line = line.rstrip('\n\r')
                    progress = int((i / total_lines) * 100)
                    
                    self.progress.emit(progress, f"正在输入第 {i}/{total_lines} 行")
                    
                    keyboard.write(clean_line)
                    
                    if i < total_lines:
                        keyboard.press_and_release('enter')
                        time.sleep(0.1)
            
            self.progress.emit(100, "输入完成！")
            self.finished.emit()
            
        except Exception as e:
            self.error.emit(f"错误: {str(e)}")
    
    def stop(self):
        self.is_running = False


class FileManager:
    @staticmethod
    def get_file_info(file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    return {
                        'exists': True,
                        'line_count': len(lines),
                        'content_preview': ''.join(lines[:3]) + ("..." if len(lines) > 3 else "")
                    }
            except:
                return {'exists': True, 'line_count': 0, 'content_preview': '无法读取文件,可能是文件位置权限不够，请更换文件位置或用管理员权限运行程序。'}
        return {'exists': False, 'line_count': 0, 'content_preview': ''}
