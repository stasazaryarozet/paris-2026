#!/bin/bash
# Git pre-commit hook для автоматической валидации
# Установка: ln -s ../../pre-commit.sh .git/hooks/pre-commit

echo "🔍 Pre-commit валидация..."

# Проверяем, изменялись ли критичные файлы
if git diff --cached --name-only | grep -qE '(WEBSITE_CONTENT.md|build.py|content.js|index.html|style.css)'; then
    echo "   Обнаружены изменения в критичных файлах"
    
    # Если изменился WEBSITE_CONTENT.md, регенерируем content.js
    if git diff --cached --name-only | grep -q 'WEBSITE_CONTENT.md'; then
        echo "   → Регенерирую content.js..."
        python3 build.py || exit 1
        git add content.js
    fi
    
    # Запускаем тесты
    echo "   → Запуск тестов..."
    python3 test_build.py || {
        echo ""
        echo "❌ КОММИТ ОТКЛОНЁН: тесты не прошли"
        echo "   Исправь ошибки и попробуй снова"
        exit 1
    }
fi

echo "✅ Валидация пройдена"
exit 0

