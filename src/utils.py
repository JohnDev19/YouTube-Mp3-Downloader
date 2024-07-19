import re

def sanitize_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '_', filename)

def format_file_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
