import re
import sys

def compress_css(css_content):
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove newlines and multiple spaces
    css_content = re.sub(r'\s+', ' ', css_content)
    # Remove space around :, {, }, ;
    css_content = re.sub(r'\s*([:;{}])\s*', r'\1', css_content)
    # Remove trailing semicolon before }
    css_content = re.sub(r';}', '}', css_content)
    return css_content.strip()

if __name__ == "__main__":
    css_content = sys.stdin.read()
    compressed_content = compress_css(css_content)
    sys.stdout.write(compressed_content)
