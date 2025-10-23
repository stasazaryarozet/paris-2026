#!/bin/bash
# Автоматический push при изменении content.js

cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Projects/paris-2026

while true; do
  # Ждём изменений в content.js
  fswatch -1 content.js
  
  # Даём время на завершение записи
  sleep 1
  
  # Проверяем есть ли изменения
  if ! git diff --quiet content.js; then
    echo "🔄 Обнаружены изменения в content.js"
    git add content.js
    git commit -m "auto: update content"
    git push origin main
    echo "✅ Изменения отправлены"
  fi
done

