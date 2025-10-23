#!/bin/bash
# One-command deploy: всё в одной команде
# Использование: ./deploy.sh "commit message"

set -e

MESSAGE="${1:-content: update}"

echo "🚀 ONE-COMMAND DEPLOY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Build
echo "1/4 Build..."
python3 build.py

# 2. Test
echo "2/4 Test..."
python3 test_comprehensive.py

# 3. Commit
echo "3/4 Commit..."
git add -A
git commit -m "$MESSAGE" || echo "Нет изменений для коммита"

# 4. Push
echo "4/4 Push..."
git push origin main

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Деплой завершён!"
echo "   Проверь: https://parisinjanuary.ru (через 1-2 минуты)"

