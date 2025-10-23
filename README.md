# Париж: индивидуальный почерк ар-деко

Лендинг для программы путешествия в Париж (январь 2026).

## Архитектура

**Single Source of Truth: Markdown → Автогенерация → SPA**

```
WEBSITE_CONTENT.md  ← единственный источник правды (редактируй здесь)
       ↓
   build.py         ← автогенерация
       ↓
   content.js       ← сгенерированный файл (не редактируй)
       ↓
   index.html       ← SPA рендеринг
```

### Преимущества

1. **Один источник правды** — редактируешь только `WEBSITE_CONTENT.md`
2. **Markdown** — универсальный, читаемый, легко редактируемый
3. **Автогенерация** — `content.js` создаётся автоматически
4. **Git-friendly** — понятные диффы в MD
5. **Нет дублирования** — минимальная избыточность

## Редактирование контента

1. Открой `WEBSITE_CONTENT.md`
2. Измени нужные секции
3. Запусти `python3 build.py`
4. Готово — `content.js` обновлён, сайт работает

Не редактируй `content.js` вручную — все изменения будут потеряны при следующем запуске `build.py`.

```javascript
const CONTENT = {
  hero: { title: "...", subtitle: "...", ... },
  days: [ { title: "...", locations: [...] } ],
  curators: [ { name: "...", bio: [...] } ],
  inclusions: [ { title: "...", description: "..." } ]
};
```

Сохрани файл. Готово.

## 📚 Ключевые документы проекта

### Документация кампании:

1. **[SOURCE_MATERIALS.md](SOURCE_MATERIALS.md)** — структурированная аналитика исходников  
   Ключевые моменты, концепции, выжимки из всех материалов
   
   **[SOURCE_MATERIALS_RAW.md](SOURCE_MATERIALS_RAW.md)** — полный архив (369 КБ)  
   Все транскрипты и рабочие документы без сокращений (5265 строк)

2. **[CAMPAIGN_AESTHETICS.md](CAMPAIGN_AESTHETICS.md)** — визуальная система  
   Эстетика кампании, преемственность с parisinseptember.ru, гайд для всех каналов

3. **[ERROR_PREVENTION.md](ERROR_PREVENTION.md)** — ⚠️ предотвращение ошибок  
   Как избегать критических ошибок, контрольные списки, извлечённые уроки

### Архив всех кампаний:

4. **[CAMPAIGNS_LEGACY.md](CAMPAIGNS_LEGACY.md)** — легаси-архив  
   База знаний всех дизайн-путешествий: September 2025, January 2026 и будущих. Функциональная информация, результаты, lessons learned, полные текстовые исходники.

---

## 🌐 Живой сайт

- **Production:** https://parisinjanuary.ru
- **Backup:** https://stasazaryarozet.github.io/paris-2026

Автоматический деплой через GitHub Actions при пуше в `main`.

## 📦 Восстановление версии

Быстрое восстановление стабильного состояния:

```bash
./restore.sh
```

**UUID текущей версии:** `b4bc2807-793a-4bc2-930f-646a904f9513`

См. также: [RESTORE.md](RESTORE.md) | [QUICKREF.txt](QUICKREF.txt)

## Инструменты

- **Хостинг**: GitHub Pages (кастомный домен + HTTPS)
- **Домен**: parisinjanuary.ru (DNS настроен через 4 A-записи)
- **CI/CD**: GitHub Actions (автоматический деплой)
- **Формы**: Formspree (отправка на email)
- **Транскрипция**: Whisper API (локально через `.venv`)

## Git workflow

```bash
# Текущая версия (work in progress)
git checkout main

# Стабильная версия (v1 snapshot)
git checkout wip-v1

# Переключение одной командой
./switch.sh
```

## Файлы

```
content.js              ← РЕДАКТИРУЙ ЗДЕСЬ
index.html              ← HTML shell (не трогай без нужды)
og-image.jpg            ← OG image для соцсетей

source_materials/       ← аудио записи
transcripts/            ← текстовые транскрипты
tools/                  ← скрипты транскрипции

content.md              ← архив (старая архитектура)
build.py                ← архив (старая архитектура)
template.html           ← архив (старая архитектура)
index.html.backup       ← бэкап предыдущей версии
```

## Транскрипция новых записей

```bash
source .venv/bin/activate
python3 tools/transcribe.py "source_materials/New Recording XX.m4a"
```

Скрипт создаст `transcripts/New Recording XX.txt`.

---

**Последнее обновление:** 23 октября 2025  
**Стабильная версия:** v1.0-production-b4bc2807  
**GitHub Release:** [v1.0-production-b4bc2807](https://github.com/stasazaryarozet/paris-2026/releases/tag/v1.0-production-b4bc2807)
