AUDIT FOR SONNET 4.5 — paris-2026 — v1 (2025-10-24)

Контекст
- Минимальный стек: статический SPA (HTML/CSS/JS), контент → WEBSITE_CONTENT.md → build.py → content.js → index.html.
- Типографика RU реализована (build.py), автогенерация и тесты есть, pre-commit запускает сборку/проверки.
- Хостинг GitHub Pages + CNAME, форма Formspree, цель — быстрое, надёжное, без зависимостей.
- PROPOSAL v7: «обойтись без», TDD, тесты после каждого изменения, архитектурная простота.

Основные риски (P0 → P2)
P0 (критично)
- Мета-теги и <title> заполняются JS на клиенте → боты/OG-краулеры видят пусто.
- Цвет .day-title на desktop: белый текст на белом фоне → нечитаемо.
- Тесты используют node -c (нет такой опции у Node) → ложные падения.
- Несогласованность Formspree ID (код: xvgwnvkb; документ: mqaadgzr) → риск потери заявок.
- «Вечер» в днях не подхватывается как отдельное поле, если оформлен как обычная локация.

P1 (высокий)
- Нет canonical, robots.txt, sitemap.xml, JSON-LD (Event/Tour).
- Нет honeypot и темы письма в форме; нет политики конфиденциальности/ссылки.
- Дублирование smooth-scroll (CSS + JS); нет preconnect к Google Fonts.
- Pre-commit не валидирует изменения в HTML/CSS.

P2 (средний)
- A11y аккордеона можно усилить (aria-controls/id). Нет prefers-reduced-motion.
- Плавающий CTA без учёта safe-area на iOS может перекрывать контент.
- Глобальное * { max-width: 100% } потенциально даёт сайд-эффекты.

План внедрения (минимальными средствами)
Wave 0 — безинфраструктурные правки (<30 мин)
- Статически проставить <title>, meta, OG/Twitter в <head> (остается JS-оверрайд).
- .day-title: задать тёмный цвет на desktop, оставить белый на mobile.
- A11y: aria-controls/id для аккордеонов.
- Форма: honeypot, _subject; зафиксировать единый Formspree ID.

Wave 1 — гигиена платформы
- Тесты: заменить node -c на node --check; fallback на node -e.
- Pre-commit: включить триггер для index.html/style.css (гонять тесты при их изменении).
- Добавить canonical, JSON-LD, preconnect.
- Добавить robots.txt и sitemap.xml; добавить 404.html (простая).

Wave 2 — улучшения без новых зависимостей (опционально)
- prefers-reduced-motion для анимаций; throttle/RAF уже есть.
- Минимизировать JS smooth-scroll (оставить CSS или JS, но не оба).
- Безопасность: /.well-known/security.txt; CSP недоступен полноценно на GH Pages.
- Аналитика (опционально): Plausible/GA; если N/A — пропустить.

Готовые правки (диффы)

1) index.html — статические мета‑теги в <head>, JSON‑LD, preconnect
— Вставить/обновить внутри <head> до подключений стилей/скриптов.

```html
<!-- static SEO/OG + preconnect + JSON-LD -->
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<title>Индивидуальный почерк ар-деко. 100&nbsp;лет — 4&nbsp;дня в&nbsp;Париже (январь 2026)</title>
<link rel="canonical" href="https://www.parisinjanuary.ru" />

<meta name="description" content="4&nbsp;дня в&nbsp;Париже. Фактуры, материалы, атмосфера. Ольга и Наталья. Галереи, отели, шоу-румы. Малые группы.">
<meta name="keywords" content="Paris Art Deco, ар-деко Париж, Palais de Tokyo, Nolinski, Galerie Vallois, Maison Louis Carré">

<meta property="og:title" content="Индивидуальный почерк ар-деко. 100&nbsp;лет">
<meta property="og:description" content="4&nbsp;дня. Фактуры, материалы, атмосфера. То, что&nbsp;не&nbsp;видно в&nbsp;публикациях.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.parisinjanuary.ru">
<meta property="og:image" content="https://www.parisinjanuary.ru/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Индивидуальный почерк ар-деко">
<meta property="og:locale" content="ru_RU">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Индивидуальный почерк ар-деко. 100&nbsp;лет">
<meta name="twitter:description" content="4&nbsp;дня. Фактуры, материалы, атмосфера. То, что&nbsp;не&nbsp;видно в&nbsp;публикациях.">
<meta name="twitter:image" content="https://www.parisinjanuary.ru/og-image.jpg">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TouristTrip",
  "name": "Индивидуальный почерк ар-деко. 100 лет — 4 дня в Париже",
  "startDate": "2026-01-15",
  "endDate": "2026-01-19",
  "image": "https://www.parisinjanuary.ru/og-image.jpg",
  "inLanguage": "ru-RU",
  "url": "https://www.parisinjanuary.ru",
  "provider": { "@type": "Organization", "name": "Ольга Розет" },
  "offers": { "@type": "Offer", "price": "1550", "priceCurrency": "EUR", "availability": "https://schema.org/InStock" }
}
</script>
```

2) index.html — A11y для аккордеонов и форма (honeypot + subject)

```diff
--- a/index.html
+++ b/index.html
@@
-      CONTENT.days.forEach((day, index) => {
+      CONTENT.days.forEach((day, index) => {
         const dayEl = document.createElement('div');
         dayEl.className = 'day';
@@
-        dayEl.innerHTML = `
-          <div class="day-header" role="button" tabindex="0" aria-expanded="false" aria-label="${day.number}: ${day.title}, ${day.date}">
+        const contentId = `day-content-${index}`;
+        dayEl.innerHTML = `
+          <div class="day-header" role="button" tabindex="0" aria-expanded="false" aria-controls="${contentId}" aria-label="${day.number}: ${day.title}, ${day.date}">
             <div class="day-header-left">
               <div class="day-number">${day.number}</div>
               <div class="day-title">${day.title}</div>
               <div class="day-date">${day.date}</div>
             </div>
             <div class="day-toggle" aria-hidden="true">▼</div>
           </div>
-          <div class="day-content">
+          <div class="day-content" id="${contentId}">
             <div class="day-theme">${day.theme}</div>
             <ul class="locations-list">
               ${locationsHTML}
             </ul>
             ${eveningHTML}
           </div>
         `;
@@
       <form id="bookingForm" action="https://formspree.io/f/xvgwnvkb" method="POST">
+        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
+        <input type="hidden" name="_subject" value="Paris January 2026 booking">
```

3) style.css — читаемость заголовка дня

```diff
--- a/style.css
+++ b/style.css
@@
 .day-title {
   font-size: 1.5rem;
   margin-bottom: 0.25rem;
-  color: #ffffff;
   font-weight: 600;
 }
@@
+@media (min-width: 768px) {
+  .day-title { color: var(--midnight-blue); }
+}
+@media (max-width: 767px) {
+  .day-title { color: #ffffff; }
+}
```

4) build.py — извлечь «Вечер» как отдельное поле, если он оформлен как локация

```diff
--- a/build.py
+++ b/build.py
@@
         locations = []
         location_pattern = r'\*\*(.+?)\*\*\s*\n(.+?)(?=\n\*\*|\n---|\n## |$)'
         for loc_match in re.finditer(location_pattern, locations_text, re.DOTALL):
             name, desc = loc_match.groups()
             desc_clean = desc.strip().replace('\n\n', '\n')
             locations.append({
                 'name': name.strip(),
                 'description': desc_clean
             })
@@
         day_data = {
             'number': day_num,
             'date': date.strip(),
             'title': title.strip(),
             'theme': theme.strip(),
             'locations': locations
         }
@@
-        evening_match = re.search(r'\*\*Вечер:\*\* (.+?)(?=\n|$)', locations_text)
-        if evening_match:
-            day_data['evening'] = evening_match.group(1).strip()
+        # Extract "Вечер" if it came as a location item
+        evening_idx = next((i for i, x in enumerate(locations) if x['name'].strip().lower().startswith('вечер')), None)
+        if evening_idx is not None:
+            day_data['evening'] = locations[evening_idx]['description']
+            del locations[evening_idx]
```

5) test_build.py — валидный синтакс‑чек JS

```diff
--- a/test_build.py
+++ b/test_build.py
@@
-    print("2. Проверка синтаксиса JavaScript...")
-    result = subprocess.run(['node', '-c', 'content.js'], capture_output=True, text=True)
-    if result.returncode != 0:
-        errors.append(f"❌ Синтаксическая ошибка в content.js: {result.stderr}")
-        return errors
-    print("   ✅ Синтаксис валиден")
+    print("2. Проверка синтаксиса JavaScript...")
+    result = subprocess.run(['node', '--check', 'content.js'], capture_output=True, text=True)
+    if result.returncode != 0:
+        # fallback: выполнить файл под Node (ожидается, что синтаксис валиден)
+        fallback = subprocess.run(['node', '-e', 'require("./content.js");'], capture_output=True, text=True)
+        if fallback.returncode != 0:
+            errors.append(f"❌ Синтаксическая ошибка в content.js: {result.stderr or fallback.stderr}")
+            return errors
+    print("   ✅ Синтаксис валиден")
```

6) test_comprehensive.py — то же

```diff
--- a/test_comprehensive.py
+++ b/test_comprehensive.py
@@
-print_info("Проверка синтаксиса JavaScript...")
-result = subprocess.run(['node', '-c', 'content.js'], capture_output=True, text=True)
-if result.returncode != 0:
-    print_error(f"Синтаксическая ошибка JS: {result.stderr}")
-    errors.append("Level 3: JS syntax error")
-else:
-    print_success("Синтаксис JavaScript валиден")
+print_info("Проверка синтаксиса JavaScript...")
+result = subprocess.run(['node', '--check', 'content.js'], capture_output=True, text=True)
+if result.returncode != 0:
+    # fallback
+    fb = subprocess.run(['node', '-e', 'require("./content.js");'], capture_output=True, text=True)
+    if fb.returncode != 0:
+        print_error(f"Синтаксическая ошибка JS: {result.stderr or fb.stderr}")
+        errors.append("Level 3: JS syntax error")
+    else:
+        print_success("Синтаксис JavaScript валиден (fallback)")
+else:
+    print_success("Синтаксис JavaScript валиден")
```

7) pre-commit.sh — валидировать HTML/CSS изменения

```diff
--- a/pre-commit.sh
+++ b/pre-commit.sh
@@
-# Проверяем, изменялись ли критичные файлы
-if git diff --cached --name-only | grep -qE '(WEBSITE_CONTENT.md|build.py|content.js)'; then
+# Проверяем, изменялись ли критичные файлы
+if git diff --cached --name-only | grep -qE '(WEBSITE_CONTENT.md|build.py|content.js|index.html|style.css)'; then
```

8) robots.txt и sitemap.xml — добавить в корень (GitHub Pages отдаст статикой)

robots.txt
```text
User-agent: *
Allow: /
Sitemap: https://www.parisinjanuary.ru/sitemap.xml
```

sitemap.xml (минимум)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.parisinjanuary.ru/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.parisinjanuary.ru/content.js</loc>
    <changefreq>weekly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://www.parisinjanuary.ru/style.css</loc>
    <changefreq>weekly</changefreq>
    <priority>0.3</priority>
  </url>
}</urlset>
```

QA чек‑лист (после внедрения)
- OG/Twitter превью корректны в Facebook Sharing Debugger и Twitter Card Validator.
- Google Rich Results Test видит JSON‑LD.
- Светлая/тёмная подложка .day-header: заголовок читаем.
- Клавиатурная навигация по дням работает; aria-expanded toggles.
- Форма: honeypot блокирует ботов; заявки доходят (проверить ID).
- Тесты проходят локально и в CI; pre-commit отлавливает правки HTML/CSS.

Definition of Done
- P0 устранены. P1 внедрены, если не требуют новых сервисов/зависимостей.
- Ноль новых зависимостей. Изменения обратимы. Тесты зелёные.


