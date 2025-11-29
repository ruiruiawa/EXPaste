import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from styles import STYLES

def main():
    """应用主入口"""
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyleSheet("\n".join(STYLES.values()))
    
    # 创建主窗口
    window = MainWindow()
    window.show()
    
    # 运行应用
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()