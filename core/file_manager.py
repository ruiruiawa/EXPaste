import os

class FileManager:
    """文件管理器 - 负责文件操作"""
    
    @staticmethod
    def get_file_info(file_path):
        """获取文件信息"""
        if not file_path or not os.path.exists(file_path):
            return {'exists': False, 'line_count': 0, 'content_preview': ''}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return {
                    'exists': True,
                    'line_count': len(lines),
                    'content_preview': ''.join(lines[:3]) + ("..." if len(lines) > 3 else "")
                }
        except Exception:
            return {
                'exists': True, 
                'line_count': 0, 
                'content_preview': '无法读取文件，请检查文件权限或路径'
            }
    
    @staticmethod
    def validate_file_path(file_path):
        """验证文件路径"""
        if not file_path:
            return False, "文件路径为空"
        if not os.path.exists(file_path):
            return False, "文件不存在"
        if not os.path.isfile(file_path):
            return False, "路径不是文件"
        return True, "文件有效"