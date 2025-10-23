#!/bin/bash
# Быстрое восстановление состояния проекта

set -e

TAG="v1.0-production-b4bc2807"
UUID="b4bc2807-793a-4bc2-930f-646a904f9513"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Восстановление состояния проекта"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Версия:    $TAG"
echo "UUID:      $UUID"
echo "Описание:  Production release с parisinjanuary.ru"
echo "Дата:      $(git log -1 --format=%ai $TAG 2>/dev/null || echo 'неизвестно')"
echo ""

# Проверяем незакоммиченные изменения
if [[ -n $(git status -s) ]]; then
    echo "⚠️  У вас есть незакоммиченные изменения:"
    git status -s
    echo ""
    read -p "Продолжить? Изменения будут сохранены в stash (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git stash push -m "Auto-stash перед восстановлением $TAG"
        echo "✅ Изменения сохранены в stash"
    else
        echo "❌ Отменено"
        exit 1
    fi
fi

echo "🔄 Восстановление состояния..."
git fetch origin tag $TAG --no-tags 2>/dev/null || echo "  (тег уже есть локально)"
git checkout $TAG

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Успешно восстановлено состояние $TAG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Для возврата к работе над веткой main:"
echo "  git checkout main"
echo ""
echo "Для восстановления stash (если был):"
echo "  git stash pop"
echo ""

