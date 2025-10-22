#!/bin/bash
# Переключение между версиями сайта

set -e

CURRENT_BRANCH=$(git branch --show-current)

show_status() {
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Текущая ветка: $CURRENT_BRANCH"
  echo "Доступные версии:"
  echo "  • main       - основная рабочая ветка"
  echo "  • wip-v1     - снимок текущей версии"
  echo "  • v1.0-wip   - тег текущей версии (WIP)"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

switch_version() {
  local target=$1
  
  # Проверка несохраненных изменений
  if [[ -n $(git status -s) ]]; then
    echo "⚠️  Есть несохраненные изменения:"
    git status -s
    echo ""
    read -p "Сохранить изменения? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
      git add -A
      read -p "Commit message: " msg
      git commit -m "$msg"
    else
      read -p "Отменить изменения и переключиться? (y/n): " -n 1 -r
      echo
      if [[ $REPLY =~ ^[Yy]$ ]]; then
        git reset --hard
      else
        echo "❌ Отменено"
        exit 1
      fi
    fi
  fi
  
  echo "🔄 Переключение на $target..."
  git checkout "$target"
  
  echo ""
  echo "✅ Переключено на $target"
  echo ""
  show_status
}

deploy() {
  echo "🚀 Деплой на surge.sh..."
  surge . paris-art-deco-2026.surge.sh
  echo ""
  echo "✅ Опубликовано: https://paris-art-deco-2026.surge.sh"
}

case "${1:-status}" in
  status)
    show_status
    ;;
  wip|snapshot)
    switch_version "wip-v1"
    ;;
  dev|main)
    switch_version "main"
    ;;
  deploy)
    deploy
    ;;
  *)
    echo "Использование: ./switch.sh [команда]"
    echo ""
    echo "Команды:"
    echo "  status       - показать текущую версию (default)"
    echo "  wip          - переключить на wip-v1 (снимок)"
    echo "  dev          - переключить на main (рабочая)"
    echo "  deploy       - деплой текущей версии"
    echo ""
    echo "Примеры:"
    echo "  ./switch.sh wip      # переключиться на снимок"
    echo "  ./switch.sh dev      # переключиться на main"
    echo "  ./switch.sh deploy   # задеплоить текущую"
    exit 1
    ;;
esac

