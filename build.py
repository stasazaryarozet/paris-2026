#!/usr/bin/env python3
"""
Генерирует content.js из WEBSITE_CONTENT.md
Единственный источник правды: WEBSITE_CONTENT.md
"""

import re
import json
from pathlib import Path

def parse_frontmatter(content):
    """Извлекает YAML frontmatter"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}, content
    
    fm_text = match.group(1)
    body = content[match.end():]
    
    meta = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            meta[key.strip()] = value.strip().strip('"')
    
    return meta, body

def parse_content(md_path):
    """Полный парсинг WEBSITE_CONTENT.md"""
    content = Path(md_path).read_text(encoding='utf-8')
    meta, body = parse_frontmatter(content)
    
    data = {}
    
    # Meta
    data['meta'] = {
        'title': meta.get('title', ''),
        'description': meta.get('description', ''),
        'keywords': meta.get('keywords', ''),
        'ogTitle': meta.get('og_title', ''),
        'ogDescription': meta.get('og_description', ''),
        'ogImage': meta.get('og_image', ''),
        'url': meta.get('og_url', '')
    }
    
    # Hero
    hero_match = re.search(r'^# (.+?)\n\n\*\*Subtitle:\*\*(.+?)\*\*Dates:\*\* (.+?)\n\*\*Group:\*\* (.+?)\n\*\*Price:\*\* (.+?)(?:\n|---)', body, re.DOTALL)
    if hero_match:
        title_raw = hero_match.group(1).strip()
        # Конвертируем <span class="hero-accent">100 лет</span> в HTML для JS
        title_html = title_raw.replace('<span class="hero-accent">', '<span style="font-size: 1.3em; font-weight: 800;">')
        title_html = title_html.replace('</span>', '</span>')
        
        subtitle_raw = hero_match.group(2).strip()
        subtitle_html = subtitle_raw.replace('\n', '<br>')
        
        data['hero'] = {
            'title': title_html,
            'subtitle': subtitle_html,
            'dates': hero_match.group(3).strip(),
            'group': hero_match.group(4).strip(),
            'price': hero_match.group(5).strip()
        }
    
    # Program intro
    data['program'] = {'intro': []}
    prog_match = re.search(r'## Программа\n\n(.+?)---', body, re.DOTALL)
    if prog_match:
        intro_text = prog_match.group(1).strip()
        for para in intro_text.split('\n\n'):
            para = para.strip()
            if para.startswith('>'):
                # Highlight
                text = para.strip('> ').strip('*').strip()
                data['program']['intro'].append({
                    'type': 'highlight',
                    'text': text
                })
            elif para:
                data['program']['intro'].append(para)
    
    # Days
    data['days'] = []
    day_pattern = r'## (ДЕНЬ [IVX]+) • (.+?)\n### (.+?)\n\*\*Тема:\*\* (.+?)\n\n(.*?)(?=\n---|\n## [КЧ]|$)'
    
    for match in re.finditer(day_pattern, body, re.DOTALL):
        day_num, date, title, theme, locations_text = match.groups()
        
        locations = []
        location_pattern = r'\*\*(.+?)\*\*\s*\n(.+?)(?=\n\*\*|\n---|\n## |$)'
        for loc_match in re.finditer(location_pattern, locations_text, re.DOTALL):
            name, desc = loc_match.groups()
            # Убираем лишние переводы строк, но сохраняем bullet points
            desc_clean = desc.strip().replace('\n\n', '\n')
            locations.append({
                'name': name.strip(),
                'description': desc_clean
            })
        
        day_data = {
            'number': day_num,
            'date': date.strip(),
            'title': title.strip(),
            'theme': theme.strip(),
            'locations': locations
        }
        
        # Проверяем на evening
        evening_match = re.search(r'\*\*Вечер:\*\* (.+?)(?=\n|$)', locations_text)
        if evening_match:
            day_data['evening'] = evening_match.group(1).strip()
        
        data['days'].append(day_data)
    
    # Curators
    data['curators'] = []
    curators_section = re.search(r'## Кураторы\n\n(.+?)---', body, re.DOTALL)
    if curators_section:
        curator_pattern = r'### (.+?)\n\*\*(.+?)\*\*\n\n(.*?)(?=\n### |---)'
        for match in re.finditer(curator_pattern, curators_section.group(1), re.DOTALL):
            name, role, bio_text = match.groups()
            bio = [line.strip('• ').strip() for line in bio_text.strip().split('\n') if line.strip()]
            data['curators'].append({
                'name': name.strip(),
                'role': role.strip(),
                'bio': bio
            })
    
    # Inclusions
    data['inclusions'] = []
    incl_section = re.search(r'## Что включено\n\n(.+?)$', body, re.DOTALL)
    if incl_section:
        incl_pattern = r'\*\*([✓✗💶]) (.+?)\*\*\s*\n(.+?)(?=\n\*\*|$)'
        for match in re.finditer(incl_pattern, incl_section.group(1), re.DOTALL):
            icon, title, desc = match.groups()
            
            inc_data = {
                'icon': icon.strip(),
                'title': title.strip(),
                'description': desc.strip()
            }
            
            # Проверяем на цену
            if '💶' in icon:
                price_match = re.search(r'Стоимость: (.+)', title)
                if price_match:
                    inc_data['price'] = price_match.group(1).strip()
                    inc_data['title'] = 'Стоимость'
            
            data['inclusions'].append(inc_data)
    
    return data

def generate_content_js(data):
    """Генерирует content.js из данных"""
    
    js = "const CONTENT = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    return js

def main():
    print("🔨 Генерация content.js из WEBSITE_CONTENT.md...")
    
    data = parse_content('WEBSITE_CONTENT.md')
    js = generate_content_js(data)
    
    Path('content.js').write_text(js, encoding='utf-8')
    
    print("✅ content.js обновлён из WEBSITE_CONTENT.md")
    print("   • Источник правды: WEBSITE_CONTENT.md")
    print("   • content.js — автогенерируется, не редактировать вручную")
    print("   • index.html использует content.js для рендеринга")

if __name__ == '__main__':
    main()
