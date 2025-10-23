# Париж: индивидуальный почерк ар-деко

Лендинг для программы путешествия в Париж (январь 2026).

## Архитектура

**Single Source of Truth: Markdown → Автогенерация → SPA**

```
WEBSITE_CONTENT.md  ← единственный источник правды (редактируй здесь)
       ↓
   build.py         ← автогенерация + русская типографика
       ↓
   content.js       ← сгенерированный файл (не редактируй)
       ↓
   index.html       ← SPA рендеринг
```

## Редактирование контента

1. Открой `WEBSITE_CONTENT.md`
2. Измени нужные секции
3. Запусти `python3 build.py` (или коммит запустит автоматически)
4. Готово — `content.js` обновлён, сайт работает

Не редактируй `content.js` вручную — все изменения будут потеряны при следующем запуске `build.py`.

## 📚 Ключевые документы

1. **[WEBSITE_CONTENT.md](WEBSITE_CONTENT.md)** — источник правды для сайта
2. **[SOURCE_MATERIALS.md](SOURCE_MATERIALS.md)** — все исходники кампании
3. **[CAMPAIGNS_LEGACY.md](CAMPAIGNS_LEGACY.md)** — легаси всех кампаний
4. **[OPERATIONAL_MODEL_PROPOSAL_v7.md](OPERATIONAL_MODEL_PROPOSAL_v7.md)** — операционная модель AI-агента

## 🌐 Живой сайт

- **Production:** https://parisinjanuary.ru
- **Backup:** https://stasazaryarozet.github.io/paris-2026

Автоматический деплой через GitHub Actions при пуше в `main`.

## Инструменты

- **Хостинг**: GitHub Pages (кастомный домен + HTTPS)
- **Домен**: parisinjanuary.ru (DNS через 4 A-записи)
- **CI/CD**: GitHub Actions (автодеплой)
- **Формы**: Formspree (отправка на email)
- **Pre-commit**: Автогенерация content.js + тесты

## Файлы

```
WEBSITE_CONTENT.md     ← РЕДАКТИРУЙ ЗДЕСЬ
build.py               ← автогенерация (запускается автоматически)
content.js             ← сгенерированный (не трогай)
index.html             ← HTML shell
style.css              ← стили
og-image.jpg           ← OG image для соцсетей

source_materials/      ← аудио записи
transcripts/           ← текстовые транскрипты
tools/                 ← утилиты (транскрипция, merge)
```

## Транскрипция новых записей

```bash
source .venv/bin/activate
python3 tools/transcribe.py "source_materials/New Recording XX.m4a"
```

---

**Последнее обновление:** 23 октября 2025
