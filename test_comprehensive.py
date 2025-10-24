#!/usr/bin/env python3
"""
Комплексное тестирование всего стека снизу вверх (bottom-up)
Уровень 1: WEBSITE_CONTENT.md (источник)
Уровень 2: build.py (парсинг и генерация)
Уровень 3: content.js (промежуточный результат)
Уровень 4: index.html (интеграция)
Уровень 5: Браузер (рендеринг)
Уровень 6: Форма (функциональность)
"""

import subprocess
import json
import re
from pathlib import Path
import sys

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")

def print_info(text):
    print(f"{Colors.BLUE}→ {text}{Colors.RESET}")

errors = []

# ============================================================================
# УРОВЕНЬ 1: WEBSITE_CONTENT.MD (ИСТОЧНИК ДАННЫХ)
# ============================================================================

print_header("УРОВЕНЬ 1: WEBSITE_CONTENT.MD")

print_info("Проверка существования файла...")
if not Path('WEBSITE_CONTENT.md').exists():
    print_error("WEBSITE_CONTENT.md не найден!")
    errors.append("Level 1: Source file missing")
    sys.exit(1)
print_success("Файл существует")

print_info("Проверка структуры Markdown...")
content_md = Path('WEBSITE_CONTENT.md').read_text(encoding='utf-8')

# Frontmatter
if not re.match(r'^---\n.*?---\n', content_md, re.DOTALL):
    print_error("Отсутствует YAML frontmatter")
    errors.append("Level 1: No frontmatter")
else:
    print_success("YAML frontmatter присутствует")

# Критические секции
required_sections = [
    (r'# Индивидуальный почерк ар-деко', 'Hero заголовок'),
    (r'\*\*Subtitle:\*\*', 'Hero subtitle'),
    (r'\*\*Dates:\*\*', 'Hero dates'),
    (r'## Программа', 'Программа секция'),
    (r'## ДЕНЬ I', 'День 1'),
    (r'## ДЕНЬ II', 'День 2'),
    (r'## ДЕНЬ III', 'День 3'),
    (r'## ДЕНЬ IV', 'День 4'),
    (r'## ДЕНЬ V', 'День 5'),
    (r'## Кураторы', 'Кураторы секция'),
    (r'### Ольга', 'Куратор Ольга'),
    (r'### Наталья', 'Куратор Наталья'),
    (r'## Что включено', 'Что включено')
]

print_info("Проверка обязательных секций...")
for pattern, name in required_sections:
    if re.search(pattern, content_md):
        print_success(f"{name}")
    else:
        print_error(f"{name} отсутствует")
        errors.append(f"Level 1: Missing {name}")

# Критический контент проверяется в Level 3 (после типографики)

# ============================================================================
# УРОВЕНЬ 2: BUILD.PY (ПАРСИНГ И ГЕНЕРАЦИЯ)
# ============================================================================

print_header("УРОВЕНЬ 2: BUILD.PY")

print_info("Проверка существования build.py...")
if not Path('build.py').exists():
    print_error("build.py не найден!")
    errors.append("Level 2: build.py missing")
    sys.exit(1)
print_success("build.py существует")

print_info("Проверка синтаксиса Python...")
result = subprocess.run(['python3', '-m', 'py_compile', 'build.py'], capture_output=True, text=True)
if result.returncode != 0:
    print_error(f"Синтаксическая ошибка: {result.stderr}")
    errors.append("Level 2: Python syntax error")
else:
    print_success("Синтаксис Python валиден")

print_info("Запуск build.py...")
result = subprocess.run(['python3', 'build.py'], capture_output=True, text=True)
if result.returncode != 0:
    print_error(f"build.py завершился с ошибкой:\n{result.stderr}")
    errors.append("Level 2: build.py execution failed")
    sys.exit(1)
print_success("build.py выполнен успешно")

# Проверка вывода
if '✅' in result.stdout:
    print_success(f"Генерация успешна")
else:
    print_warning("Нет подтверждения успешной генерации")

# ============================================================================
# УРОВЕНЬ 3: CONTENT.JS (ПРОМЕЖУТОЧНЫЙ РЕЗУЛЬТАТ)
# ============================================================================

print_header("УРОВЕНЬ 3: CONTENT.JS")

print_info("Проверка существования content.js...")
if not Path('content.js').exists():
    print_error("content.js не найден!")
    errors.append("Level 3: content.js missing")
    sys.exit(1)
print_success("content.js существует")

content_js = Path('content.js').read_text(encoding='utf-8')

print_info("Проверка синтаксиса JavaScript...")
result = subprocess.run(['node', '--check', 'content.js'], capture_output=True, text=True)
if result.returncode != 0:
    # Fallback
    fb = subprocess.run(['node', '-e', 'require("./content.js");'], capture_output=True, text=True)
    if fb.returncode != 0:
        print_error(f"Синтаксическая ошибка JS: {result.stderr or fb.stderr}")
        errors.append("Level 3: JS syntax error")
    else:
        print_success("Синтаксис JavaScript валиден (fallback)")
else:
    print_success("Синтаксис JavaScript валиден")

print_info("Проверка структуры объекта CONTENT...")
if 'const CONTENT = {' in content_js:
    print_success("Объект CONTENT объявлен")
else:
    print_error("Объект CONTENT не найден")
    errors.append("Level 3: CONTENT object missing")

# Проверка чистого JS (без JSON кавычек)
if '"hero":' in content_js or '"meta":' in content_js:
    print_error("КРИТИЧНО: Ключи в кавычках (JSON вместо JS)")
    errors.append("Level 3: JSON keys instead of JS")
else:
    print_success("Чистый JS синтаксис (ключи без кавычек)")

# Проверка полноты данных
print_info("Проверка полноты данных в content.js...")
js_checks = [
    ('hero:', 'Hero секция'),
    ('meta:', 'Meta секция'),
    ('program:', 'Program секция'),
    ('days:', 'Days массив'),
    ('curators:', 'Curators массив'),
    ('inclusions:', 'Inclusions массив'),
    ('Розет', 'Куратор Ольга'),
    ('Логинова', 'Куратор Наталья'),
    ('ДЕНЬ I', 'День 1'),
    ('ДЕНЬ V', 'День 5'),
    ('100&nbsp;лет', 'Акцент на юбилее')  # С типографикой
]

for check, name in js_checks:
    if check in content_js:
        print_success(name)
    else:
        print_error(f"{name} отсутствует")
        errors.append(f"Level 3: Missing {name}")

# Проверка размера
file_size = len(content_js)
print_info(f"Размер content.js: {file_size} байт")
if file_size < 4000:
    print_error("Файл слишком маленький (возможна потеря данных)")
    errors.append("Level 3: File too small")
elif file_size > 50000:
    print_warning("Файл очень большой (возможна избыточность)")
else:
    print_success("Размер в норме")

# ============================================================================
# УРОВЕНЬ 4: INDEX.HTML (ИНТЕГРАЦИЯ)
# ============================================================================

print_header("УРОВЕНЬ 4: INDEX.HTML")

print_info("Проверка существования index.html...")
if not Path('index.html').exists():
    print_error("index.html не найден!")
    errors.append("Level 4: index.html missing")
    sys.exit(1)
print_success("index.html существует")

index_html = Path('index.html').read_text(encoding='utf-8')

print_info("Проверка подключения content.js...")
if 'script src="content.js"' in index_html or 'script src=\\"content.js\\"' in index_html:
    print_success("content.js подключен")
else:
    print_error("content.js не подключен!")
    errors.append("Level 4: content.js not linked")

print_info("Проверка рендеринг функции...")
if 'render()' in index_html or 'CONTENT.' in index_html:
    print_success("Рендеринг настроен")
else:
    print_error("Рендеринг функция не найдена")
    errors.append("Level 4: No render function")

print_info("Проверка DOM элементов...")
dom_elements = [
    ('hero-title', 'Hero заголовок'),
    ('hero-subtitle', 'Hero подзаголовок'),  
    ('days-container', 'Контейнер дней'),
    ('bookingForm', 'Форма бронирования')
]

# Дополнительная проверка: кураторы рендерятся JS, не статический контейнер
print_info("Проверка секций контента...")
content_sections = [
    ('<section.*?curators.*?>', 'Секция кураторов'),
    ('<section.*?inclusions.*?>', 'Секция inclusions')
]
for pattern, name in content_sections:
    if re.search(pattern, index_html, re.IGNORECASE | re.DOTALL):
        print_success(name)
    else:
        print_warning(f"{name} не найдена (возможно, динамический рендеринг)")


for elem_id, name in dom_elements:
    if elem_id in index_html:
        print_success(f"{name} ({elem_id})")
    else:
        print_error(f"{name} не найден")
        errors.append(f"Level 4: Missing DOM element {elem_id}")

# ============================================================================
# УРОВЕНЬ 5: ФОРМА (ФУНКЦИОНАЛЬНОСТЬ)
# ============================================================================

print_header("УРОВЕНЬ 5: ФОРМА БРОНИРОВАНИЯ")

print_info("Проверка конфигурации формы...")
if 'formspree.io' in index_html:
    print_success("Formspree настроен")
    # Извлечение Formspree ID
    match = re.search(r'formspree\.io/f/([a-zA-Z0-9]+)', index_html)
    if match:
        formspree_id = match.group(1)
        print_success(f"Formspree ID: {formspree_id}")
    else:
        print_warning("Не удалось извлечь Formspree ID")
else:
    print_error("Formspree не настроен")
    errors.append("Level 5: Formspree not configured")

print_info("Проверка полей формы...")
form_fields = [
    (r'name="name"', 'Поле "Имя"'),
    (r'name="contact"', 'Поле "Email или телефон" (упрощённая форма)'),
    (r'name="consent"', 'Чекбокс согласия'),
    (r'type="submit"', 'Кнопка отправки')
]

for pattern, name in form_fields:
    if re.search(pattern, index_html):
        print_success(name)
    else:
        print_error(f"{name} отсутствует")
        errors.append(f"Level 5: Missing form field {name}")

print_info("Проверка валидации...")
if 'required' in index_html:
    print_success("HTML5 валидация настроена")
else:
    print_warning("HTML5 валидация не найдена")

# ============================================================================
# УРОВЕНЬ 6: ПРОДАКШЕН (ФИНАЛЬНАЯ ПРОВЕРКА)
# ============================================================================

print_header("УРОВЕНЬ 6: ПРОДАКШЕН")

print_info("Проверка доступности сайта...")
result = subprocess.run(['curl', '-sI', 'https://parisinjanuary.ru'], capture_output=True, text=True, timeout=10)
if result.returncode == 0 and 'HTTP/2 200' in result.stdout:
    print_success("Сайт доступен (HTTP 200)")
else:
    print_error("Сайт недоступен или ошибка")
    errors.append("Level 6: Site not accessible")

print_info("Проверка content.js на продакшене...")
result = subprocess.run(['curl', '-s', 'https://parisinjanuary.ru/content.js'], capture_output=True, text=True, timeout=10)
if result.returncode == 0 and 'CONTENT' in result.stdout:
    print_success("content.js загружается на продакшене")
    
    prod_content = result.stdout
    if 'Логинова' in prod_content or 'Наталья' in prod_content:
        print_success("Куратор Наталья присутствует на продакшене")
    else:
        print_error("Куратор Наталья отсутствует на продакшене!")
        errors.append("Level 6: Natalia missing in production")
    
    if '100&nbsp;лет' in prod_content or '100 лет' in prod_content:
        print_success("'100 лет' присутствует на продакшене")
    else:
        print_error("'100 лет' отсутствует на продакшене!")
        errors.append("Level 6: '100 years' missing in production")
else:
    print_error("Не удалось загрузить content.js с продакшена")
    errors.append("Level 6: Cannot fetch content.js from production")

# ============================================================================
# ИТОГОВЫЙ ОТЧЁТ
# ============================================================================

print_header("ИТОГОВЫЙ ОТЧЁТ")

if errors:
    print(f"\n{Colors.RED}{Colors.BOLD}❌ ТЕСТИРОВАНИЕ ПРОВАЛЕНО{Colors.RESET}")
    print(f"\n{Colors.RED}Обнаружено ошибок: {len(errors)}{Colors.RESET}\n")
    for i, error in enumerate(errors, 1):
        print(f"{Colors.RED}{i}. {error}{Colors.RESET}")
    sys.exit(1)
else:
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ{Colors.RESET}")
    print(f"\n{Colors.GREEN}Проверено уровней: 6{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 1: WEBSITE_CONTENT.md ✓{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 2: build.py ✓{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 3: content.js ✓{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 4: index.html ✓{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 5: Форма бронирования ✓{Colors.RESET}")
    print(f"{Colors.GREEN}• Уровень 6: Продакшен ✓{Colors.RESET}")
    print(f"\n{Colors.BOLD}Проект готов к использованию.{Colors.RESET}\n")
    sys.exit(0)

