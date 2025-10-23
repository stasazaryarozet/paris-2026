# 📦 Восстановление состояния проекта

Этот проект сохранён в стабильном состоянии с уникальным идентификатором.

---

## 🔖 Информация о версии

- **Тег:** `v1.0-production-b4bc2807`
- **UUID:** `b4bc2807-793a-4bc2-930f-646a904f9513`
- **Описание:** Production release с полностью настроенным доменом `parisinjanuary.ru` и финальными правками от Ольги
- **Дата:** 23 октября 2025

---

## ⚡ Быстрое восстановление

### Одна команда:
```bash
./restore.sh
```

### Или вручную:
```bash
git fetch origin tag v1.0-production-b4bc2807 --no-tags
git checkout v1.0-production-b4bc2807
```

---

## 🔄 Возврат к работе

После просмотра версии вернитесь к основной ветке:
```bash
git checkout main
```

---

## 📋 Что включено в эту версию

### Контент
- ✅ Все правки от Ольги применены
- ✅ Финальный текст программы
- ✅ Правильные даты и названия
- ✅ Data-Driven SPA архитектура

### Инфраструктура
- ✅ Домен `parisinjanuary.ru` полностью настроен
- ✅ HTTPS с принудительным редиректом
- ✅ GitHub Pages деплой через Actions
- ✅ DNS настроен (4 A-записи)

### Файлы
- `index.html` — HTML shell
- `content.js` — весь контент в одном месте
- `CNAME` — настройка кастомного домена
- `.github/workflows/deploy.yml` — автодеплой

---

## 🌐 Живой сайт

- **Production:** https://parisinjanuary.ru
- **Backup:** https://stasazaryarozet.github.io/paris-2026

---

## 🔗 GitHub Release

Тег доступен в GitHub:
```
https://github.com/stasazaryarozet/paris-2026/releases/tag/v1.0-production-b4bc2807
```

---

## 💡 Использование UUID

UUID служит для однозначной идентификации этого snapshot'а:
- При обсуждениях можно ссылаться на короткую версию: `b4bc2807`
- Полный UUID: `b4bc2807-793a-4bc2-930f-646a904f9513`
- Git тег: `v1.0-production-b4bc2807`

---

## 📊 Статистика проекта на момент сохранения

```bash
# Просмотр коммитов до этой версии
git log v1.0-production-b4bc2807 --oneline

# Просмотр файлов в версии
git ls-tree -r v1.0-production-b4bc2807 --name-only

# Сравнение с текущим состоянием
git diff v1.0-production-b4bc2807..HEAD
```

