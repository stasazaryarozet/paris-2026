import os
from pathlib import Path

# Paths
BASE_DIR = Path("/Users/azaryarozet/Library/Mobile Documents/com~apple~CloudDocs/○/olga/design-travels/PARIS-2026")
HANDOUTS_SRC = BASE_DIR / "program/handouts"
OUTPUT_DIR = BASE_DIR / "handouts"

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} • Paris 2026 Handouts</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <nav class="nav-links no-print">
            <a href="index.html">← Список дней</a>
            <a href="day1.html">День I</a>
            <a href="day2.html">День II</a>
            <a href="day3.html">День III</a>
            <a href="day4.html">День IV</a>
            <a href="javascript:window.print()" style="margin-left: auto; color: #c41e3a;">Печать [PDF]</a>
        </nav>
        
        <article class="handout-content">
            {content}
        </article>

        <footer class="footer">
            <p>Ольга Розет & Наталья Логинова • Профессиональная программа по дизайну • Париж 2026</p>
        </footer>
    </div>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handouts • Paris 2026</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container" style="text-align: center;">
        <h1>PARIS 2026</h1>
        <h2 style="font-weight: 300; color: #666;">Handouts / Материалы</h2>
        <p style="margin: 40px 0;">Профессиональные конспекты и задачи по дням программы</p>
        
        <div style="display: grid; gap: 20px; max-width: 400px; margin: 0 auto;">
            <a href="day1.html" class="day-link">ДЕНЬ I • 15 января</a>
            <a href="day2.html" class="day-link">ДЕНЬ II • 16 января</a>
            <a href="day3.html" class="day-link">ДЕНЬ III • 17 января</a>
            <a href="day4.html" class="day-link">ДЕНЬ IV • 18 января</a>
        </div>

        <style>
            .day-link {
                display: block;
                padding: 20px;
                border: 1px solid #eee;
                text-decoration: none;
                color: #1a1a1a;
                border-radius: 8px;
                transition: all 0.3s ease;
                font-weight: 600;
            }
            .day-link:hover {
                background: #fcfcfc;
                border-color: #c41e3a;
                color: #c41e3a;
                transform: translateY(-2px);
            }
        </style>

        <footer class="footer">
            <p>Ольга Розет & Наталья Логинова • Париж 2026</p>
        </footer>
    </div>
</body>
</html>
"""

import re

def simple_markdown(text):
    # Headers
    text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Horizontal Rule
    text = re.sub(r'^---$', r'<hr>', text, flags=re.MULTILINE)
    
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # Lists (Simplified)
    text = re.sub(r'^\* (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^- (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    # Wrap loose <li>s in <ul>
    # This is a bit hacky but works for the current structure
    text = re.sub(r'(<li>.*</li>(\n<li>.*</li>)*)', r'<ul>\1</ul>', text)

    # Paragraphs (Loose lines to <p>)
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        if not line.strip(): continue
        if not line.startswith('<'):
            new_lines.append(f'<p>{line}</p>')
        else:
            new_lines.append(line)
    
    return '\n'.join(new_lines)

def process_handouts():
    # Files mapping
    files = {
        "DAY_I.md": "day1.html",
        "DAY_II.md": "day2.html",
        "DAY_III.md": "day3.html",
        "DAY_IV.md": "day4.html"
    }
    
    for md_file, html_file in files.items():
        src_path = HANDOUTS_SRC / md_file
        if not src_path.exists(): continue
        
        with open(src_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        title = "Handout"
        if md_content.startswith("# "):
            title = md_content.split('\n')[0].replace('# ', '').strip()
            
        html_content = simple_markdown(md_content)
        
        # Post-process for task box
        if '<h3>ЗАДАЧА ДНЯ</h3>' in html_content:
            parts = html_content.split('<h3>ЗАДАЧА ДНЯ</h3>')
            main_part = parts[0]
            rest = parts[1]
            task_content = rest.split('<hr>')[0] if '<hr>' in rest else rest
            after_task = rest.replace(task_content, '')
            html_content = main_part + '<div class="task-box"><h3>ЗАДАЧА ДНЯ</h3>' + task_content + '</div>' + after_task

        final_html = TEMPLATE.format(title=title, content=html_content)
        
        with open(OUTPUT_DIR / html_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"Generated {html_file}")

    # Index file
    with open(OUTPUT_DIR / "index.html", 'w', encoding='utf-8') as f:
        f.write(INDEX_TEMPLATE)
    print("Generated index.html")

if __name__ == "__main__":
    process_handouts()
