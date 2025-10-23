#!/bin/bash
# Watch-скрипт: автоматическая пересборка при изменении WEBSITE_CONTENT.md
# Использование: ./watch.sh (оставить работать в фоне)

WATCH_FILE="WEBSITE_CONTENT.md"

echo "👁️  Watching $WATCH_FILE for changes..."
echo "   Press Ctrl+C to stop"
echo ""

# Используем fswatch (установить: brew install fswatch)
if ! command -v fswatch &> /dev/null; then
    echo "❌ fswatch не установлен"
    echo "   Установка: brew install fswatch"
    exit 1
fi

fswatch -o "$WATCH_FILE" | while read f; do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚡ Изменение обнаружено: $(date '+%H:%M:%S')"
    echo ""
    
    # Build
    echo "→ Запускаю build.py..."
    python3 build.py
    
    # Test
    echo "→ Запускаю тесты..."
    python3 test_build.py
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Готово! content.js обновлён"
        echo "   Открой index.html в браузере для проверки"
    else
        echo ""
        echo "❌ Ошибка в тестах!"
    fi
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
done

