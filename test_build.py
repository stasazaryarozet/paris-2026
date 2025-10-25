#!/usr/bin/env python3
"""
Тесты для build.py — автоматическая валидация генерации content.js
Запуск: python3 test_build.py
"""

import subprocess
import json
import re
from pathlib import Path

def test_build():
    """Полная валидация build.py"""
    
    print("🧪 ТЕСТИРОВАНИЕ BUILD.PY\n")
    errors = []
    
    # 1. Генерация
    print("1. Запуск build.py...")
    result = subprocess.run(['python3', 'build.py'], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"❌ build.py завершился с ошибкой: {result.stderr}")
        return errors
    print("   ✅ Генерация завершена")
    
    # 2. Синтаксис JS
    print("2. Проверка синтаксиса JavaScript...")
    result = subprocess.run(['node', '--check', 'content.js'], capture_output=True, text=True)
    if result.returncode != 0:
        # Fallback: выполнить файл под Node
        fallback = subprocess.run(['node', '-e', 'require("./content.js");'], capture_output=True, text=True)
        if fallback.returncode != 0:
            errors.append(f"❌ Синтаксическая ошибка в content.js: {result.stderr or fallback.stderr}")
            return errors
    print("   ✅ Синтаксис валиден")
    
    # 3. Чтение content.js
    print("3. Парсинг content.js...")
    content_js = Path('content.js').read_text(encoding='utf-8')
    
    # Проверка на JSON вместо JS
    if '"hero":' in content_js or '"meta":' in content_js:
        errors.append("❌ КРИТИЧНО: Ключи в кавычках (JSON вместо JS)")
    else:
        print("   ✅ Чистый JS синтаксис (без кавычек у ключей)")
    
    # 4. Структура CONTENT
    print("4. Проверка структуры данных...")
    
    required_keys = ['hero', 'meta', 'program', 'days', 'curators', 'inclusions']
    for key in required_keys:
        if f'{key}:' not in content_js:
            errors.append(f"❌ Отсутствует секция: {key}")
        else:
            print(f"   ✅ {key} секция присутствует")
    
    # 5. Hero
    print("5. Проверка hero секции...")
    hero_fields = ['title:', 'subtitle:', 'dates:', 'group:', 'price:']
    for field in hero_fields:
        if field not in content_js[:500]:  # Hero в начале
            errors.append(f"❌ Hero: отсутствует {field}")
        else:
            print(f"   ✅ Hero.{field.strip(':')} есть")
    
    # 6. Дни
    print("6. Проверка дней программы...")
    days_count = content_js.count('number: "ДЕНЬ')
    if days_count < 4:
        errors.append(f"❌ Найдено только {days_count} дней (ожидается 4)")
    else:
        print(f"   ✅ {days_count} дней найдено")
    
    for day in ['ДЕНЬ I', 'ДЕНЬ II', 'ДЕНЬ III', 'ДЕНЬ IV']:
        if day not in content_js:
            errors.append(f"❌ Отсутствует: {day}")
    
    # 7. Кураторы (КРИТИЧНО!)
    print("7. Проверка кураторов...")
    curators = ['Розет', 'Логинова']
    for curator in curators:
        if curator not in content_js:
            errors.append(f"❌ КРИТИЧНО: Куратор {curator} отсутствует!")
        else:
            print(f"   ✅ {curator} присутствует")
    
    # 8. Inclusions
    print("8. Проверка inclusions...")
    inclusions_count = content_js.count('icon:')
    if inclusions_count < 3:
        errors.append(f"❌ Найдено только {inclusions_count} inclusions (ожидается 3+)")
    else:
        print(f"   ✅ {inclusions_count} inclusions найдено")
    
    # 9. Критические элементы
    print("9. Проверка критических элементов контента...")
    critical_content = [
        '100&nbsp;лет',  # С типографикой
        '15–18+ января 2026',
        '1 550&nbsp;€',  # Типографика между числом и единицей
        'Palais de Tokyo',
        'Maison Louis Carré',
        'Eileen Gray'
    ]
    for item in critical_content:
        if item not in content_js:
            errors.append(f"⚠️  Отсутствует важный элемент: {item}")
    
    print(f"   ✅ Критические элементы проверены")
    
    # 10. Размер файла
    print("10. Проверка размера content.js...")
    file_size = len(content_js)
    if file_size < 4000:
        errors.append(f"❌ content.js слишком маленький ({file_size} байт, ожидается >4000)")
    else:
        print(f"   ✅ Размер: {file_size} байт")
    
    # Итог
    print("\n" + "="*60)
    if errors:
        print("❌ ТЕСТЫ ПРОВАЛЕНЫ\n")
        for error in errors:
            print(error)
        return False
    else:
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ")
        print("   content.js готов к деплою")
        return True

if __name__ == '__main__':
    success = test_build()
    exit(0 if success else 1)

