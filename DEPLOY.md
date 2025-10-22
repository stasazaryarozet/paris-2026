# Деплой (глобально доступный)

## Вариант 1: GitHub Pages (рекомендуется)

### Шаг 1: Закрыть Cursor и открыть терминал
```bash
cd /Users/azaryarozet/Library/Mobile\ Documents/com~apple~CloudDocs/Projects/paris-2026
```

### Шаг 2: Закоммитить изменения
```bash
git add -A
git commit -m "feat: GitHub Pages setup"
git push origin main
```

### Шаг 3: Настроить GitHub Pages
1. Открой https://github.com/azaryarozet/paris-2026/settings/pages
2. Source: **GitHub Actions**
3. Сохрани

### Шаг 4: Проверка
Через 1-2 минуты сайт будет доступен:
- **https://azaryarozet.github.io/paris-2026/**

---

## Вариант 2: Vercel (drag & drop)

1. Открой https://vercel.com/new
2. Перетащи папку проекта
3. Deploy
4. Готово!

---

## Вариант 3: Cloudflare Pages

1. Открой https://dash.cloudflare.com/
2. Pages → Create a project
3. Upload assets → перетащи папку
4. Deploy

---

## После деплоя: Подключить домен

### GitHub Pages
Settings → Pages → Custom domain → `parisinjanuary.ru`

### DNS записи (у регистратора)
```
CNAME www azaryarozet.github.io
A @ 185.199.108.153
A @ 185.199.109.153
A @ 185.199.110.153
A @ 185.199.111.153
```

---

**Рекомендация:** GitHub Pages — самый простой и надёжный вариант.

