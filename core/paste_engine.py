import os
import tempfile
import time
import keyboard
import logging
from PyQt5.QtCore import QObject, pyqtSignal, QThread

logger = logging.getLogger(__name__)

class PasteEngine(QObject):
    """粘贴引擎 - 负责粘贴操作和状态管理"""
    
    progress_updated = pyqtSignal(int, str)  # 进度, 消息
    status_changed = pyqtSignal(str)         # 状态消息
    started = pyqtSignal()                   # 开始信号
    finished = pyqtSignal()                   # 完成信号
    error_occurred = pyqtSignal(str)        # 错误信号
    
    def __init__(self, delay_ms=10):
        super().__init__()
        self.delay_ms = delay_ms
        self._is_running = False
        self._current_thread = None
        self._temp_files = []
    
    def start_paste(self, content_source, mode):
        """开始粘贴操作"""
        if self._is_running:
            self.error_occurred.emit("已有粘贴任务在进行中")
            return False
        
        # 验证内容
        if mode == "file":
            if not content_source or not os.path.exists(content_source):
                self.error_occurred.emit("请先选择有效的文本文件")
                return False
        else:
            if not content_source.strip():
                self.error_occurred.emit("请输入要粘贴的文本内容")
                return False
            
            # 创建临时文件
            try:
                content_source = self._create_temp_file(content_source)
            except Exception as e:
                self.error_occurred.emit(f"创建临时文件失败: {str(e)}")
                return False
        
        # 在工作线程中执行
        self._is_running = True
        self.started.emit()
        
        self._current_thread = QThread()
        worker = PasteWorker(content_source, self.delay_ms)
        worker.moveToThread(self._current_thread)
        
        # 连接信号
        worker.progress_updated.connect(self.progress_updated)
        worker.status_changed.connect(self.status_changed)
        worker.finished.connect(self._on_worker_finished)
        worker.error_occurred.connect(self.error_occurred)
        
        self._current_thread.started.connect(worker.run)
        self._current_thread.start()
        
        return True
    
    def stop_paste(self):
        """停止粘贴"""
        self._is_running = False
        self._cleanup()
        self.finished.emit()
    
    def _create_temp_file(self, content):
        """为编辑器内容创建临时文件"""
        temp_file = tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', suffix='.txt', delete=False
        )
        temp_file.write(content)
        temp_file.close()
        self._temp_files.append(temp_file.name)
        return temp_file.name
    
    def _on_worker_finished(self):
        """工作线程完成"""
        self._is_running = False
        self._cleanup()
        self.finished.emit()
    
    def _cleanup(self):
        """清理资源"""
        if self._current_thread and self._current_thread.isRunning():
            self._current_thread.quit()
            self._current_thread.wait(1000)
            self._current_thread = None
        
        # 清理临时文件
        for temp_file in self._temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception as e:
                logger.warning(f"删除临时文件失败: {e}")
        self._temp_files.clear()
    
    def is_running(self):
        """检查是否正在运行"""
        return self._is_running
    
    def set_delay(self, delay_ms):
        """设置延迟"""
        self.delay_ms = delay_ms


class PasteWorker(QObject):
    """粘贴工作线程"""
    
    progress_updated = pyqtSignal(int, str)
    status_changed = pyqtSignal(str)
    finished = pyqtSignal()
    error_occurred = pyqtSignal(str)
    
    def __init__(self, file_path, delay_ms):
        super().__init__()
        self.file_path = file_path
        self.delay_ms = delay_ms
        self._is_running = True
    
    def run(self):
        """执行粘贴操作"""
        try:
            if not os.path.exists(self.file_path):
                self.error_occurred.emit(f"文件 '{self.file_path}' 不存在")
                return
            
            # 倒计时
            for i in range(3, 0, -1):
                if not self._is_running:
                    return
                self.status_changed.emit(f"倒计时: {i}秒...")
                time.sleep(1)
            
            self.status_changed.emit("开始输入内容...")
            
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                total_lines = len(lines)
                
                for i, line in enumerate(lines, 1):
                    if not self._is_running:
                        return
                    
                    clean_line = line.rstrip('\n\r')
                    progress = int((i / total_lines) * 100)
                    
                    self.progress_updated.emit(progress, f"正在输入第 {i}/{total_lines} 行")
                    
                    keyboard.write(clean_line)
                    
                    if i < total_lines:
                        keyboard.press_and_release('enter')
                        time.sleep(self.delay_ms / 1000.0)
            
            if self._is_running:
                self.progress_updated.emit(100, "输入完成！")
                self.finished.emit()
                
        except Exception as e:
            self.error_occurred.emit(f"粘贴错误: {str(e)}")
        finally:
            self._is_running = False
    
    def stop(self):
        """停止工作"""
        self._is_running = False