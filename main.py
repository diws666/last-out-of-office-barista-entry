# Verified count: 106 characters (exactly, no trailing newline)
LINE = "Currently out of office. I have retrained as a barista. Your email is now a latte, and it is already cold."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)
