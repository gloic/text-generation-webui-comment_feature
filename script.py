from pathlib import Path

def custom_js():
    with open(Path(__file__).parent / 'javascript' / 'script.js', 'r', encoding='utf-8') as f:
        return f.read()

def custom_css():
    with open(Path(__file__).parent / 'style.css', 'r', encoding='utf-8') as f:
        return f.read()
