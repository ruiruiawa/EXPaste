STYLES = {
    "main_window": """
        QMainWindow {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                stop: 0 #667eea, stop: 0.5 #764ba2, stop: 1 #f093fb);
        }
    """,
    
    "central_widget": """
        QWidget {
            background: transparent;
        }
    """,
    
    "title_label": """
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: white;
            padding: 15px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(255,255,255,0.2), stop:1 rgba(255,255,255,0.1));
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.3);
        }
    """,
    
    "normal_label": """
        QLabel {
            color: white;
            font-size: 14px;
            font-weight: 500;
            padding: 8px 12px;
        }
    """,
    
    "combo_box": """
        QComboBox {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #ffffff, stop:1 #f8f9fa);
            border: 2px solid rgba(255,255,255,0.5);
            border-radius: 8px;
            padding: 8px 12px;
            color: #2c3e50;
            font-size: 14px;
            min-width: 180px;
        }
        QComboBox:hover {
            border: 2px solid #667eea;
        }
        QComboBox:focus {
            border: 2px solid #667eea;
            background: white;
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #667eea;
            width: 0px;
            height: 0px;
        }
        QComboBox QAbstractItemView {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            selection-background-color: #667eea;
            outline: none;
        }
    """,
    
    "button_primary": """
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #667eea, stop:1 #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #768efa, stop:1 #865bb2);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #566eda, stop:1 #663b92);
        }
        QPushButton:disabled {
            background: #cccccc;
            color: #666666;
        }
    """,
    
    "button_secondary": """
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #ffffff, stop:1 #f8f9fa);
            color: #2c3e50;
            border: 2px solid rgba(255,255,255,0.6);
            border-radius: 8px;
            padding: 10px 20px;
            min-width: 100px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #f8f9fa, stop:1 #e9ecef);
            border: 2px solid rgba(255,255,255,0.8);
        }
        QPushButton:pressed {
            background: #e9ecef;
        }
        QPushButton:disabled {
            background: #f0f0f0;
            color: #999999;
        }
    """,
    
    "button_success": """
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #28a745, stop:1 #20c997);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #38b755, stop:1 #30d9a7);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #189735, stop:1 #10b987);
        }
    """,
    
    "button_warning": """
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #dc3545, stop:1 #fd7e14);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 100px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #ec4555, stop:1 #ff8e24);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #cc2535, stop:1 #ed6e04);
        }
    """,
    
    "progress_bar": """
        QProgressBar {
            border: 1px solid rgba(255,255,255,0.3);
            background: rgba(255,255,255,0.1);
            border-radius: 5px;
            height: 8px;
            text-align: center;
        }
        QProgressBar::chunk {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #667eea, stop:1 #764ba2);
            border-radius: 5px;
        }
    """,
    
    "text_edit": """
        QTextEdit {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 12px;
            color: #2c3e50;
        }
        QTextEdit:focus {
            border: 1px solid #667eea;
        }
    """,
    
    "line_edit": """
        QLineEdit {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px 12px;
            color: #2c3e50;
            font-size: 13px;
        }
        QLineEdit:focus {
            border: 1px solid #667eea;
        }
    """,
    
    "spin_box": """
        QSpinBox {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px 12px;
            color: #2c3e50;
            font-size: 13px;
        }
        QSpinBox:focus {
            border: 1px solid #667eea;
        }
        QSpinBox::up-button, QSpinBox::down-button {
            background: transparent;
            border: none;
            width: 20px;
        }
    """,
    
    "group_box": """
        QGroupBox {
            font-weight: bold;
            color: white;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 8px;
            margin-top: 10px;
            padding-top: 10px;
            background: rgba(255,255,255,0.1);
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 8px 0 8px;
            color: white;
        }
    """,
    
    "card": """
        QWidget {
            background: rgba(255,255,255,0.1);
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.2);
        }
    """,
    
    "card_highlight": """
        QWidget {
            background: rgba(255,255,255,0.2);
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.4);
        }
    """,
    
    "status_success": """
        QLabel {
            color: #28a745;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_warning": """
        QLabel {
            color: #ffc107;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_error": """
        QLabel {
            color: #dc3545;
            font-size: 12px;
            font-weight: bold;
        }
    """,
    
    "status_info": """
        QLabel {
            color: #17a2b8;
            font-size: 12px;
        }
    """,
    
    "status_normal": """
        QLabel {
            color: rgba(255,255,255,0.8);
            font-size: 12px;
        }
    """,
    
    "menu_bar": """
        QMenuBar {
            background-color: rgba(255,255,255,0.1);
            border-bottom: 1px solid rgba(255,255,255,0.2);
            padding: 5px;
        }
        QMenuBar::item {
            padding: 4px 8px;
            background: transparent;
            border-radius: 4px;
            color: white;
        }
        QMenuBar::item:selected {
            background: rgba(255,255,255,0.2);
            color: white;
        }
        QMenuBar::item:pressed {
            background: rgba(255,255,255,0.3);
            color: white;
        }
    """,
    
    "menu": """
        QMenu {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px;
        }
        QMenu::item {
            padding: 6px 20px 6px 20px;
            border-radius: 4px;
            color: #2c3e50;
        }
        QMenu::item:selected {
            background-color: #667eea;
            color: white;
        }
        QMenu::separator {
            height: 1px;
            background: #ddd;
            margin: 5px 0px 5px 0px;
        }
    """,
    
    "dialog": """
        QDialog {
            background: white;
            border-radius: 8px;
        }
    """,
    
    "dialog_header": """
        QWidget {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #667eea, stop:1 #764ba2);
            border-bottom: 1px solid #ddd;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
    """,
    
    "tab_widget": """
        QTabWidget::pane {
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 8px;
            background: rgba(255,255,255,0.1);
        }
        QTabWidget::tab-bar {
            alignment: center;
        }
        QTabBar::tab {
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.3);
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 8px 16px;
            margin-right: 2px;
            color: white;
        }
        QTabBar::tab:selected {
            background: rgba(255,255,255,0.3);
            border-color: rgba(255,255,255,0.5);
            color: white;
            font-weight: bold;
        }
        QTabBar::tab:hover:!selected {
            background: rgba(255,255,255,0.25);
        }
    """,
    
    "check_box": """
        QCheckBox {
            color: white;
            spacing: 8px;
        }
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border-radius: 3px;
            border: 1px solid rgba(255,255,255,0.5);
            background: rgba(255,255,255,0.1);
        }
        QCheckBox::indicator:checked {
            background: #667eea;
            border: 1px solid rgba(255,255,255,0.7);
        }
        QCheckBox::indicator:hover {
            border: 1px solid rgba(255,255,255,0.8);
        }
    """,
    
    "radio_button": """
        QRadioButton {
            color: white;
            spacing: 8px;
        }
        QRadioButton::indicator {
            width: 16px;
            height: 16px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.5);
            background: rgba(255,255,255,0.1);
        }
        QRadioButton::indicator:checked {
            background: #667eea;
            border: 1px solid rgba(255,255,255,0.7);
        }
        QRadioButton::indicator:hover {
            border: 1px solid rgba(255,255,255,0.8);
        }
    """,
    
    "scroll_bar": """
        QScrollBar:vertical {
            background: rgba(255,255,255,0.1);
            width: 12px;
            margin: 0px;
            border-radius: 6px;
        }
        QScrollBar::handle:vertical {
            background: rgba(102,126,234,0.5);
            border-radius: 6px;
            min-height: 20px;
        }
        QScrollBar::handle:vertical:hover {
            background: rgba(102,126,234,0.7);
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        QScrollBar:horizontal {
            background: rgba(255,255,255,0.1);
            height: 12px;
            margin: 0px;
            border-radius: 6px;
        }
        QScrollBar::handle:horizontal {
            background: rgba(102,126,234,0.5);
            border-radius: 6px;
            min-width: 20px;
        }
        QScrollBar::handle:horizontal:hover {
            background: rgba(102,126,234,0.7);
        }
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
        }
    """,
    
    "tool_tip": """
        QToolTip {
            background-color: #2c3e50;
            color: #ecf0f1;
            border: 1px solid #34495e;
            border-radius: 4px;
            padding: 4px 8px;
        }
    """,
    
    "drag_hint": """
        QLabel {
            background: rgba(255,255,255,0.1);
            border: 2px dashed rgba(255,255,255,0.5);
            border-radius: 8px;
            padding: 10px;
            color: rgba(255,255,255,0.9);
            font-size: 12px;
            text-align: center;
        }
    """,
    
    "drag_hint_active": """
        QLabel {
            background: rgba(102,126,234,0.2);
            border: 2px dashed #667eea;
            border-radius: 8px;
            padding: 10px;
            color: white;
            font-size: 12px;
            text-align: center;
            font-weight: bold;
        }
    """,
    
    "separator": """
        QFrame {
            background: rgba(255,255,255,0.3);
            border: none;
            height: 1px;
            margin: 8px 0px;
        }
    """,
    
    "badge_success": """
        QLabel {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #28a745, stop:1 #20c997);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "badge_warning": """
        QLabel {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #dc3545, stop:1 #fd7e14);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "badge_info": """
        QLabel {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #667eea, stop:1 #764ba2);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        }
    """,
    
    "input_group": """
        QWidget {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 8px;
            padding: 8px;
        }
    """,
    
    "elevated_card": """
        QWidget {
            background: rgba(255,255,255,0.15);
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.3);
        }
    """,
    
    "floating_panel": """
        QWidget {
            background: rgba(255,255,255,0.2);
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.4);
        }
    """
}