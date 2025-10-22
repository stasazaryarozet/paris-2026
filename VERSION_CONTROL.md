# Управление версиями

## Текущее состояние

```
main      - основная рабочая ветка (текущая)
wip-v1    - снимок текущей версии
v1.0-wip  - тег текущей версии (Work In Progress)
```

## Быстрое переключение

```bash
./switch.sh status    # показать текущую версию
./switch.sh wip       # переключиться на снимок wip-v1
./switch.sh dev       # вернуться на main
./switch.sh deploy    # задеплоить текущую версию
```

## Рабочий процесс

### 1. Сохранить текущее состояние как снимок

```bash
git add -A
git commit -m "feat: описание изменений"
git branch wip-v2    # или любое другое имя
git tag v2.0-wip
```

### 2. Экспериментировать на main

```bash
# Работаем на main
# Делаем изменения
```

### 3. Откатиться к снимку

```bash
./switch.sh wip
# или
git checkout wip-v1
```

### 4. Опубликовать изменения

```bash
./switch.sh deploy
# или
surge . paris-art-deco-2026.surge.sh
```

## Структура

- **main** - всегда рабочая ветка, можно смело экспериментировать
- **wip-vX** - снимки стабильных состояний (не обязательно production-ready)
- **vX.Y-wip** - теги для быстрого доступа к конкретным версиям

## Продакшн

Текущая версия на продакшене: **main (latest)**

URL: https://paris-art-deco-2026.surge.sh

Формы: formspree.io/f/xvgwnvkb



