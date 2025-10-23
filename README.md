# Париж: индивидуальный почерк ар-деко

Лендинг для программы путешествия в Париж (январь 2026).

## Архитектура

**Data-Driven Single Page Application**

```
content.js         ← весь текст (единственный источник правды)
index.html         ← HTML shell + рендеринг
og-image.jpg       ← социальные сети
```

### Преимущества

1. **Чистое разделение** — контент отделён от представления
2. **Нет build step** — редактируешь `content.js`, сразу видишь результат
3. **Единый источник правды** — весь текст в одном месте
4. **Валидируемая структура** — JavaScript объект вместо хрупкого парсинга
5. **Простое обновление** — меняешь `content.js` → деплой → готово

## Редактирование контента

Открой `content.js` и измени нужные поля:

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

### Три основных файла кампании:

1. **[SOURCE_MATERIALS.md](SOURCE_MATERIALS.md)** — структурированная аналитика исходников  
   Ключевые моменты, концепции, выжимки из всех материалов
   
   **[SOURCE_MATERIALS_RAW.md](SOURCE_MATERIALS_RAW.md)** — полный архив (369 КБ)  
   Все транскрипты и рабочие документы без сокращений (5265 строк)

2. **[WEBSITE_CONTENT.md](WEBSITE_CONTENT.md)** — текст посадочной  
   Весь контент сайта, эволюция формулировок, история обсуждений

3. **[CAMPAIGN_AESTHETICS.md](CAMPAIGN_AESTHETICS.md)** — визуальная система  
   Эстетика кампании, преемственность с parisinseptember.ru, гайд для всех каналов

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
