# Инструкция по деплою

## 1. Создать OG-изображение (1200×630px)

### Промпт для Midjourney/DALL-E:
```
Minimalist art deco poster design, 1200x630px, 
bold geometric composition, red #E31B1B and chrome silver #C0C0C0,
text "Париж: индивидуальный почерк ар-деко" in elegant serif font,
"15–18 января 2026" in smaller text,
clean white background, stepped geometric elements,
chrome metallic lines as accents, high contrast, modern editorial style,
--ar 1200:630
```

Сохранить как `og-image.jpg` в корне проекта.

## 2. Настроить форму

1. Зарегистрироваться на https://formspree.io (бесплатно)
2. Создать новую форму
3. Скопировать Form ID
4. В `index.html` заменить `YOUR_FORM_ID` на реальный ID (строка 1004)

## 3. Настроить домен

В `index.html` заменить (строки 16, 17, 27):
- `https://paris-art-deco-2026.com` → реальный URL

## 4. Деплой на Netlify (бесплатно)

1. Открыть https://app.netlify.com/drop
2. Перетащить папку проекта (содержащую `index.html` и `og-image.jpg`)
3. Получить URL вида `https://randomname.netlify.app`
4. Вернуться в шаг 3, вставить этот URL

## 5. Проверить шаринг

Открыть:
- https://www.opengraph.xyz
- Вставить URL
- Проверить превью для Facebook, Twitter, LinkedIn, WhatsApp

## 6. Опционально: собственный домен

В Netlify → Domain settings → Add custom domain



