# Подключение домена parisinjanuary.ru

## Шаг 1: DNS записи (у регистратора домена)

Добавь в настройках DNS домена `parisinjanuary.ru`:

### Вариант A: CNAME (рекомендуется)
```
CNAME @ na-west1-c.surge.sh
CNAME www na-west1-c.surge.sh
```

### Вариант B: A-записи (если CNAME для @ не поддерживается)
```
A @ 138.197.235.123
A www 138.197.235.123
```

**Дополнительные IP Surge.sh** (для геораспределения):
- US West: 138.197.235.123
- EU (London): 46.101.67.123
- EU (Frankfurt): 138.68.112.220
- Asia (Singapore): 139.59.195.30

## Шаг 2: Деплой с кастомным доменом

```bash
surge --project . --domain parisinjanuary.ru
```

## Проверка

После настройки DNS (может занять до 24 часов):
```bash
dig parisinjanuary.ru
curl -I https://parisinjanuary.ru
```

## Альтернатива: мультидомен

Можно добавить несколько доменов в файл `CNAME`:
```
parisinjanuary.ru
www.parisinjanuary.ru
```

Затем деплой:
```bash
surge --project . --domain parisinjanuary.ru
```

## SSL сертификат

Surge.sh автоматически выпустит Let's Encrypt сертификат для домена.

---

**Текущий рабочий адрес:** https://paris-art-deco-2026.surge.sh

