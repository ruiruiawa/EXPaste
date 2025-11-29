import os
import re

def resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        base_path = os.path.abspath(".")
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def validate_hotkey(hotkey):
    """验证热键格式"""
    if not hotkey:
        return False
    
    # 简单的热键格式验证
    parts = hotkey.lower().split('+')
    if len(parts) < 2:
        return False
    
    # 检查每个部分是否有效
    valid_modifiers = {'ctrl', 'control', 'alt', 'shift', 'win', 'windows', 'cmd', 'command'}
    key_part = parts[-1]
    
    # 最后一个部分应该是普通按键
    if len(key_part) != 1 and key_part not in {'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'}:
        # 检查是否是功能键
        if not key_part.startswith('f') or not key_part[1:].isdigit():
            return False
    
    # 前面的部分应该是修饰键
    for modifier in parts[:-1]:
        if modifier not in valid_modifiers:
            return False
    
    return True

def format_hotkey_display(hotkey):
    """格式化热键显示"""
    if not hotkey:
        return "未设置"
    
    parts = hotkey.split('+')
    formatted_parts = []
    
    for part in parts:
        if part in {'ctrl', 'control'}:
            formatted_parts.append('Ctrl')
        elif part == 'alt':
            formatted_parts.append('Alt')
        elif part == 'shift':
            formatted_parts.append('Shift')
        elif part == 'win':
            formatted_parts.append('Win')
        else:
            # 普通按键大写显示
            formatted_parts.append(part.upper())
    
    return '+'.join(formatted_parts)