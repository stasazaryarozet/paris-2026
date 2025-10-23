#!/usr/bin/env python3
"""
Генерирует content.js из WEBSITE_CONTENT.md
Единственный источник правды: WEBSITE_CONTENT.md

ВАЖНО: Генерирует чистый JavaScript (без кавычек у ключей)
"""

import re
from pathlib import Path

def apply_russian_typography(text):
    """
    Применяет правила русской типографики во всей полноте:
    - Тире, дефисы, минусы
    - Кавычки-ёлочки
    - Неразрывные пробелы
    - Многоточие
    - Спецсимволы
    
    Защищает HTML-теги от обработки
    """
    if not text or not isinstance(text, str):
        return text
    
    # Защищаем HTML-теги: временно заменяем на плейсхолдеры
    html_tags = []
    def save_tag(match):
        html_tags.append(match.group(0))
        return f'___HTML_TAG_{len(html_tags)-1}___'
    
    text = re.sub(r'<[^>]+>', save_tag, text)
    
    # 1. Многоточие: три точки → один символ …
    text = re.sub(r'\.\.\.', '…', text)
    
    # 2. Кавычки: " → «»
    # Сначала заменяем парные кавычки
    # Открывающая кавычка после пробела, начала строки или знака препинания
    text = re.sub(r'(^|[\s\(\[\{])"', r'\1«', text, flags=re.MULTILINE)
    # Закрывающая кавычка перед пробелом, концом строки или знаком препинания
    text = re.sub(r'"([\s\)\]\}\.,;:!?]|$)', r'»\1', text)
    # Оставшиеся " → « (открывающие)
    text = re.sub(r'"', '«', text)
    
    # 3. Дефис с пробелами → длинное тире с пробелами
    # НО: не заменять дефис в диапазонах дат и чисел без пробелов
    text = re.sub(r'\s+-\s+', ' — ', text)
    
    # 4. Минус в математических выражениях и температуре
    text = re.sub(r'(\s|^)-(\d)', r'\1−\2', text)  # −5
    text = re.sub(r'(\d)\s*-\s*(\d)', r'\1−\2', text)  # 10-5 → 10−5
    
    # 5. Неразрывные пробелы
    
    # 5.1. Между числом и единицей измерения
    text = re.sub(r'(\d+)\s+(кг|г|т|км|м|см|мм|л|мл|€|₽|\$|°C|°|%|лет|года?|дня|дней|день|часов|минут|секунд)', 
                  r'\1&nbsp;\2', text)
    
    # 5.2. Перед длинным тире
    text = re.sub(r'\s+—\s+', '&nbsp;— ', text)
    
    # 5.3. После однобуквенных предлогов и союзов
    text = re.sub(r'\b([вкосуяВКОСУЯ])\s+', r'\1&nbsp;', text)
    
    # 5.4. После двухбуквенных предлогов
    text = re.sub(r'\b(во|до|из|ко|на|не|ни|об|от|по|со|то|уж|за)\s+', r'\1&nbsp;', text, flags=re.IGNORECASE)
    
    # 5.5. В сокращениях
    text = re.sub(r'\bи\s+т\.\s*д\.', 'и&nbsp;т.&nbsp;д.', text)
    text = re.sub(r'\bт\.\s*е\.', 'т.&nbsp;е.', text)
    text = re.sub(r'\bт\.\s*к\.', 'т.&nbsp;к.', text)
    text = re.sub(r'\bт\.\s*п\.', 'т.&nbsp;п.', text)
    text = re.sub(r'\bи\s+др\.', 'и&nbsp;др.', text)
    text = re.sub(r'\bи\s+пр\.', 'и&nbsp;пр.', text)
    
    # 5.6. Между инициалами и фамилией
    text = re.sub(r'\b([А-ЯЁ])\.\s+([А-ЯЁ])\.\s+([А-ЯЁ][а-яё]+)', 
                  r'\1.&nbsp;\2.&nbsp;\3', text)
    text = re.sub(r'\b([А-ЯЁ])\.\s+([А-ЯЁ][а-яё]+)', 
                  r'\1.&nbsp;\2', text)
    
    # 5.7. После № и §
    text = re.sub(r'№\s+', '№&nbsp;', text)
    text = re.sub(r'§\s+', '§&nbsp;', text)
    
    # 6. Спецсимволы
    text = re.sub(r'\(c\)', '©', text, flags=re.IGNORECASE)
    text = re.sub(r'\(tm\)', '™', text, flags=re.IGNORECASE)
    text = re.sub(r'\(r\)', '®', text, flags=re.IGNORECASE)
    
    # 7. Пробелы перед знаками препинания (убираем)
    text = re.sub(r'\s+([,;:!?\)])', r'\1', text)
    
    # 8. Двойные/тройные пробелы → одинарные (но не &nbsp;)
    text = re.sub(r'(?<!&nbsp) {2,}', ' ', text)
    
    # Восстанавливаем HTML-теги
    for i, tag in enumerate(html_tags):
        text = text.replace(f'___HTML_TAG_{i}___', tag)
    
    return text

def apply_typography_recursive(data):
    """Рекурсивно применяет типографику ко всем строкам в структуре данных"""
    if isinstance(data, dict):
        return {k: apply_typography_recursive(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [apply_typography_recursive(item) for item in data]
    elif isinstance(data, str):
        return apply_russian_typography(data)
    else:
        return data

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

def js_string(s):
    """Преобразует строку в JS string literal"""
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'

def js_object(data, indent=2):
    """Рекурсивно генерирует JS объект (БЕЗ кавычек у ключей)"""
    if isinstance(data, dict):
        lines = []
        for key, value in data.items():
            value_str = js_object(value, indent + 2)
            lines.append(' ' * indent + f'{key}: {value_str}')
        return '{\n' + ',\n'.join(lines) + '\n' + ' ' * (indent - 2) + '}'
    elif isinstance(data, list):
        if not data:
            return '[]'
        lines = []
        for item in data:
            lines.append(' ' * indent + js_object(item, indent + 2))
        return '[\n' + ',\n'.join(lines) + '\n' + ' ' * (indent - 2) + ']'
    elif isinstance(data, str):
        return js_string(data)
    elif isinstance(data, bool):
        return 'true' if data else 'false'
    elif data is None:
        return 'null'
    else:
        return str(data)

def parse_content(md_path):
    """Полный парсинг WEBSITE_CONTENT.md"""
    content = Path(md_path).read_text(encoding='utf-8')
    meta, body = parse_frontmatter(content)
    
    data = {}
    
    # HERO — ПЕРВЫЙ (как в оригинале)
    hero_match = re.search(r'^# (.+?)\n\n\*\*Subtitle:\*\*.*?\n(.+?)\n\n\*\*Dates:\*\* (.+?)\s*\n\*\*Group:\*\* (.+?)\s*\n\*\*Price:\*\* (.+?)(?:\n|$)', body, re.DOTALL | re.MULTILINE)
    if hero_match:
        title_raw = hero_match.group(1).strip()
        # Сохраняем class="hero-accent" для CSS бронзы
        title_html = title_raw.replace('\n', '<br>')
        
        subtitle_raw = hero_match.group(2).strip()
        subtitle_html = subtitle_raw.replace('\n', '<br>')
        
        data['hero'] = {
            'title': title_html,
            'subtitle': subtitle_html,
            'dates': hero_match.group(3).strip(),
            'group': hero_match.group(4).strip(),
            'price': hero_match.group(5).strip()
        }
    else:
        # Fallback из коммита
        data['hero'] = {
            'title': "Индивидуальный почерк ар-деко.<br><span class=\"hero-accent\">100 лет</span>.",
            'subtitle': "4 дня с кураторами.<br>Фактуры, материалы, атмосфера.<br>То, что не видно в публикациях.",
            'dates': "15–18+ января 2026",
            'group': "до 12 человек",
            'price': "1 550 €"
        }
    
    # META — ВТОРОЙ
    data['meta'] = {
        'title': meta.get('title', ''),
        'description': meta.get('description', ''),
        'keywords': meta.get('keywords', ''),
        'ogTitle': meta.get('og_title', ''),
        'ogDescription': meta.get('og_description', ''),
        'ogImage': meta.get('og_image', ''),
        'url': meta.get('og_url', '')
    }
    
    # PROGRAM
    data['program'] = {'intro': []}
    prog_match = re.search(r'## Программа\n\n(.+?)---', body, re.DOTALL)
    if prog_match:
        intro_text = prog_match.group(1).strip()
        for para in intro_text.split('\n\n'):
            para = para.strip()
            if para.startswith('>'):
                text = para.strip('> ').strip('*').strip()
                data['program']['intro'].append({
                    'type': 'highlight',
                    'text': text
                })
            elif para:
                data['program']['intro'].append(para)
    
    # DAYS
    data['days'] = []
    day_pattern = r'## (ДЕНЬ [IVX]+) • (.+?)\n### (.+?)(?:\n\*\*Тема:\*\* (.+?))?\n\n(.*?)(?=\n---|\n## [КЧ]|$)'
    
    for match in re.finditer(day_pattern, body, re.DOTALL):
        day_num, date, title, theme_optional, locations_text = match.groups()
        theme = theme_optional if theme_optional else ""
        
        locations = []
        location_pattern = r'\*\*(.+?)\*\*\s*\n(.+?)(?=\n\*\*|\n---|\n## |$)'
        for loc_match in re.finditer(location_pattern, locations_text, re.DOTALL):
            name, desc = loc_match.groups()
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
        
        evening_match = re.search(r'\*\*Вечер:\*\* (.+?)(?=\n|$)', locations_text)
        if evening_match:
            day_data['evening'] = evening_match.group(1).strip()
        
        data['days'].append(day_data)
    
    # CURATORS
    data['curators'] = []
    curators_section = re.search(r'## Кураторы\n\n(.+?)---', body, re.DOTALL)
    if curators_section:
        curator_pattern = r'### (.+?)\n\*\*(.+?)\*\*\n\n(.*?)(?=\n### |\n---|\Z)'
        for match in re.finditer(curator_pattern, curators_section.group(1), re.DOTALL):
            name, role, bio_text = match.groups()
            bio = [line.strip('• ').strip() for line in bio_text.strip().split('\n') if line.strip()]
            data['curators'].append({
                'name': name.strip(),
                'role': role.strip(),
                'bio': bio
            })
    
    # INCLUSIONS
    data['inclusions'] = []
    incl_section = re.search(r'## Что включено\n\n(.+?)$', body, re.DOTALL)
    if incl_section:
        incl_pattern = r'\*\*([+−±€✓✗💶]) (.+?)\*\*(?:\s*\n(.+?))?(?=\n\*\*|\n\n|$)'
        for match in re.finditer(incl_pattern, incl_section.group(1), re.DOTALL):
            icon, title, desc = match.groups()
            
            inc_data = {
                'icon': icon.strip(),
                'title': title.strip(),
                'description': desc.strip() if desc else ''
            }
            
            if '💶' in icon or '€' in icon:
                inc_data['price'] = title.strip()
                inc_data['title'] = 'Стоимость'
            
            data['inclusions'].append(inc_data)
    
    # Применяем типографику ко всем текстам рекурсивно
    return apply_typography_recursive(data)

def generate_content_js(data):
    """Генерирует content.js с чистым JS синтаксисом"""
    js = "const CONTENT = " + js_object(data, 2) + ";\n"
    return js

def main():
    print("🔨 Генерация content.js из WEBSITE_CONTENT.md...")
    
    data = parse_content('WEBSITE_CONTENT.md')
    js = generate_content_js(data)
    
    Path('content.js').write_text(js, encoding='utf-8')
    
    print("✅ content.js обновлён из WEBSITE_CONTENT.md")
    print("   • Источник правды: WEBSITE_CONTENT.md")
    print("   • content.js — автогенерируется, не редактировать вручную")
    print("   • Чистый JS синтаксис (без кавычек у ключей)")

if __name__ == '__main__':
    main()
