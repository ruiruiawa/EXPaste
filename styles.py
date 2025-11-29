"""
完整的样式定义 - 为所有UI元素提供统一的样式
"""

STYLES = {
    # 主窗口和容器样式
    "main_window": """
        QMainWindow {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                                     stop: 0 #e6f0ff, stop: 1 #d1e3ff);
        }
    """,
    
    "central_widget": """
        QWidget {
            background: transparent;
        }
    """,
    
    "card": """
        QWidget {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.5);
        }
    """,
    
    "card_highlight": """
        QWidget {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 12px;
            border: 1px solid rgba(74, 144, 226, 0.3);
            border-left: 2px solid rgba(0, 0, 0, 0.1);
            border-top: 2px solid rgba(0, 0, 0, 0.1);
        }
    """,
    
    # 文本和标签样式
    "title_label": """
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #1a2c4c;
            padding: 10px;
        }
    """,
    
    "subtitle_label": """
        QLabel {
            font-size: 14px;
            color: #4a5a7a;
            padding: 5px;
        }
    """,
    
    "normal_label": """
        QLabel {
            color: #4a5a7a;
            font-size: 13px;
            padding: 2px;
        }
    """,
    
    "status_label": """
        QLabel {
            color: #6b7b9c;
            font-size: 12px;
            padding: 4px;
        }
    """,
    
    "status_success": """
        QLabel {
            color: #27ae60;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_warning": """
        QLabel {
            color: #f39c12;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_error": """
        QLabel {
            color: #e74c3c;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_info": """
        QLabel {
            color: #3498db;
            font-size: 12px;
        }
    """,
    
    "status_normal": """
        QLabel {
            color: #7f8c8d;
            font-size: 12px;
        }
    """,
    
    # 按钮样式
    "button_primary": """
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #4a90e2, stop: 1 #357abd);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #5a9ae2, stop: 1 #458acd);
            border-bottom: 2px solid rgba(0, 0, 0, 0.3);
        }
        QPushButton:pressed {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #3a7abc, stop: 1 #2a6aac);
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            margin-top: 1px;
        }
        QPushButton:disabled {
            background: #cccccc;
            color: #666666;
            border-bottom: none;
        }
    """,
    
    "button_secondary": """
        QPushButton {
            background: rgba(255, 255, 255, 0.9);
            color: #4a5a7a;
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 10px;
            padding: 10px 20px;
            min-width: 100px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.1);
        }
        QPushButton:hover {
            background: rgba(255, 255, 255, 1);
            border-color: rgba(160, 174, 192, 0.6);
            border-bottom: 2px solid rgba(0, 0, 0, 0.15);
        }
        QPushButton:pressed {
            background: rgba(240, 240, 240, 1);
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            margin-top: 1px;
        }
        QPushButton:disabled {
            background: #f0f0f0;
            color: #999999;
            border-color: #dddddd;
            border-bottom: none;
        }
    """,
    
    "button_success": """
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #2ecc71, stop: 1 #27ae60);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #3ecc81, stop: 1 #37ae70);
            border-bottom: 2px solid rgba(0, 0, 0, 0.3);
        }
        QPushButton:pressed {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #1ecc61, stop: 1 #17ae50);
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            margin-top: 1px;
        }
        QPushButton:disabled {
            background: #cccccc;
            color: #666666;
            border-bottom: none;
        }
    """,
    
    "button_warning": """
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #e74c3c, stop: 1 #c0392b);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
            border-bottom: 2px solid rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #f75c4c, stop: 1 #d0493b);
            border-bottom: 2px solid rgba(0, 0, 0, 0.3);
        }
        QPushButton:pressed {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #d73c2c, stop: 1 #b0291b);
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            margin-top: 1px;
        }
        QPushButton:disabled {
            background: #cccccc;
            color: #666666;
            border-bottom: none;
        }
    """,
    
    "button_small": """
        QPushButton {
            background: rgba(255, 255, 255, 0.9);
            color: #4a5a7a;
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 12px;
            min-width: 80px;
        }
        QPushButton:hover {
            background: rgba(255, 255, 255, 1);
            border-color: rgba(160, 174, 192, 0.6);
        }
        QPushButton:pressed {
            background: rgba(240, 240, 240, 1);
        }
        QPushButton:disabled {
            background: #f0f0f0;
            color: #999999;
            border-color: #dddddd;
        }
    """,
    
    # 输入控件样式
    "combo_box": """
        QComboBox {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 10px;
            padding: 8px 12px;
            color: #2d3c5c;
            font-size: 13px;
            min-width: 180px;
        }
        QComboBox:focus {
            border-color:rgba(74, 144, 226, 0.8)};
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #4a5a7a;
            width: 0px;
            height: 0px;
        }
        QComboBox QAbstractItemView {
            background: white;
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 5px;
            selection-background-color: #4a90e2;
            outline: none;
        }
    """,
    
    "text_edit": """
        QTextEdit {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 10px;
            padding: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 12px;
            color: #4a5a7a;
        }
        QTextEdit:focus {
            border-color: #4a90e2;
            background: rgba(255, 255, 255, 0.95);
        }
        QTextEdit:disabled {
            background: rgba(248, 249, 250, 0.7);
            color: #6c757d;
        }
    """,
    
    "line_edit": """
        QLineEdit {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 8px;
            padding: 8px 12px;
            color: #2d3c5c;
            font-size: 13px;
        }
        QLineEdit:focus {
            border-color: #4a90e2;
            background: rgba(255, 255, 255, 0.95);
        }
        QLineEdit:disabled {
            background: rgba(248, 249, 250, 0.7);
            color: #6c757d;
        }
    """,
    
    "spin_box": """
        QSpinBox {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 8px;
            padding: 8px 12px;
            color: #2d3c5c;
            font-size: 13px;
        }
        QSpinBox:focus {
            border-color: #4a90e2;
            background: rgba(255, 255, 255, 0.95);
        }
        QSpinBox:disabled {
            background: rgba(248, 249, 250, 0.7);
            color: #6c757d;
        }
        QSpinBox::up-button, QSpinBox::down-button {
            background: transparent;
            border: none;
            width: 20px;
        }
    """,
    
    "progress_bar": """
        QProgressBar {
            border: none;
            background: rgba(237, 245, 255, 0.8);
            border-radius: 10px;
            height: 6px;
            text-align: center;
        }
        QProgressBar::chunk {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #4a90e2, stop: 1 #357abd);
            border-radius: 10px;
        }
    """,
    
    # 菜单和对话框样式
    "menu_bar": """
        QMenuBar {
            background-color: rgba(255, 255, 255, 0.8);
            border-bottom: 1px solid rgba(209, 227, 255, 0.8);
            padding: 5px;
        }
        QMenuBar::item {
            padding: 4px 8px;
            background: transparent;
            border-radius: 4px;
            color: #4a5a7a;
        }
        QMenuBar::item:selected {
            background: #4a90e2;
            color: white;
        }
        QMenuBar::item:pressed {
            background: #357abd;
            color: white;
        }
    """,
    
    "menu": """
        QMenu {
            background-color: white;
            border: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 6px;
            padding: 5px;
        }
        QMenu::item {
            padding: 6px 20px 6px 20px;
            border-radius: 4px;
            color: #2d3c5c;
        }
        QMenu::item:selected {
            background-color: #4a90e2;
            color: white;
        }
        QMenu::separator {
            height: 1px;
            background: rgba(0, 0, 0, 0.1);
            margin: 5px 0px 5px 0px;
        }
    """,
    
    "dialog": """
        QDialog {
            background: white;
            border-radius: 10px;
        }
    """,
    
    "dialog_header": """
        QWidget {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #f8f9fa, stop: 1 #e9ecef);
            border-bottom: 2px solid #dee2e6;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }
    """,
    
    # 特殊组件样式
    "drag_hint": """
        QLabel {
            background: rgba(255, 255, 255, 0.7);
            border: 2px dashed #4a90e2;
            border-radius: 8px;
            padding: 10px;
            color: #4a5a7a;
            font-size: 12px;
            text-align: center;
        }
    """,
    
    "drag_hint_active": """
        QLabel {
            background: rgba(74, 144, 226, 0.1);
            border: 2px dashed #4a90e2;
            border-radius: 8px;
            padding: 10px;
            color: #4a90e2;
            font-size: 12px;
            text-align: center;
            font-weight: bold;
        }
    """,
    
    "badge_success": """
        QLabel {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #2ecc71, stop: 1 #27ae60);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "badge_warning": """
        QLabel {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #e74c3c, stop: 1 #c0392b);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "badge_info": """
        QLabel {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                                     stop: 0 #3498db, stop: 1 #2980b9);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "separator": """
        QFrame {
            background: rgba(209, 227, 255, 0.5);
            border: none;
            height: 1px;
            margin: 8px 0px;
        }
    """,
    
    "group_box": """
        QGroupBox {
            font-weight: bold;
            color: #2d3748;
            border: 1px solid rgba(209, 227, 255, 0.8);
            border-radius: 8px;
            margin-top: 10px;
            padding-top: 10px;
            background: rgba(255, 255, 255, 0.6);
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            color: #4a5a7a;
        }
    """
    
}