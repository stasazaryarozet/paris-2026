# Финальные шаги для глобального доступа

## Статус
✅ Код готов  
✅ GitHub Pages активирован  
✅ CNAME файл настроен на `www.parisinjanuary.ru`  
⏳ Осталось: запушить CNAME и настроить DNS

---

## Шаг 1: Закрой Cursor и открой Terminal

```bash
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Projects/paris-2026
```

## Шаг 2: Запуш CNAME (если ещё не сделано)

```bash
git add CNAME
git commit -m "feat: set custom domain www.parisinjanuary.ru"
git push origin main
```

## Шаг 3: Настрой DNS у регистратора parisinjanuary.ru

### Добавь эти записи:

```
Тип    Имя    Значение
────────────────────────────────────────────────
CNAME  www    stasazaryarozet.github.io
A      @      185.199.108.153
A      @      185.199.109.153
A      @      185.199.110.153
A      @      185.199.111.153
```

**Где настраивать:**
- Открой панель управления доменом на **reg.ru** (или где домен зарегистрирован)
- Раздел: DNS-записи / DNS settings
- Добавь записи выше
- Сохрани

## Шаг 4: Подожди распространение DNS (5-30 минут)

Проверь статус:
```bash
dig www.parisinjanuary.ru
dig parisinjanuary.ru
```

## Шаг 5: Проверь сайт

После распространения DNS:
- **www.parisinjanuary.ru** — будет работать
- **parisinjanuary.ru** — будет перенаправлять на www

---

## Текущие рабочие адреса

✅ **https://stasazaryarozet.github.io/paris-2026/** — работает сейчас  
⏳ **https://www.parisinjanuary.ru** — заработает после DNS  
⏳ **https://parisinjanuary.ru** — заработает после DNS

---

## Редактирование контента

После настройки DNS любые правки:
1. Открой `content.js`
2. Измени текст
3. Сохрани
4. В терминале:
```bash
git add content.js
git commit -m "update: ..."
git push origin main
```

Сайт обновится автоматически через 1-2 минуты.

---

## Быстрая справка

- **Исходники:** https://github.com/stasazaryarozet/paris-2026
- **GitHub Actions:** https://github.com/stasazaryarozet/paris-2026/actions
- **Контент:** `content.js` (единственный файл для редактирования)
- **Деплой:** автоматический через GitHub Actions

