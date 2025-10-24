# АУДИТ ЭРГОНОМИКИ — paris-2026

**Дата:** 24 октября 2025  
**Приоритеты:** 1. Эргономика, 2. Функциональность, 3. Объективная красота

---

## 1. ЭРГОНОМИКА

### 1.1 Интерактивные элементы

#### ✅ Кнопки (btn)
- ✅ `:hover` — визуальная обратная связь (transform, цвет, тень)
- ✅ `:focus-visible` — outline для клавиатурной навигации
- ✅ `cursor: pointer`
- ✅ Transition для плавности (0.3s cubic-bezier)
- ✅ Достаточный размер (padding: 1rem 2.5rem)
- **Оценка: 10/10**

#### ⚠️ Аккордеоны дней (.day-header)
- ❌ Нет `:hover` состояния
- ❌ Нет `:focus` состояния для клавиатурной навигации
- ✅ `cursor: pointer`
- ✅ Клавиатурная навигация работает (Enter/Space)
- ❌ Нет визуальной индикации фокуса
- **Оценка: 5/10**
- **КРИТИЧНАЯ ПРОБЛЕМА:** Пользователь не видит, на каком элементе фокус

#### ⚠️ Форма
- ✅ Inputs корректно стилизованы
- ❌ Нет `:focus` состояния для inputs
- ❌ Нет `:hover` для inputs
- ❌ Checkbox не имеет визуальной обратной связи
- ✅ Submit button — как .btn-primary (есть hover)
- **Оценка: 6/10**
- **ПРОБЛЕМА:** Inputs не показывают активное состояние

#### ✅ Floating CTA
- ❌ Нет `:hover` состояния (было убрано по запросу пользователя)
- ✅ Полупрозрачная (rgba 0.4)
- ✅ Appear/disappear плавно
- ✅ Позиция удобна (12rem от низа на desktop, 5rem на mobile)
- **Оценка: 7/10**
- **Замечание:** Отсутствие hover — осознанный выбор, но снижает эргономику

#### ✅ Модальное окно
- ✅ Закрытие по Esc
- ✅ Закрытие по клику на backdrop
- ✅ Button "Закрыть" имеет hover
- ✅ body.overflow блокируется
- ✅ Плавное появление/исчезновение
- **Оценка: 10/10**

#### ✅ Back to top
- ❌ Проверка нужна — есть ли hover/focus?
- ✅ Работает корректно (#top)
- **Оценка: ?/10**

### 1.2 Touch Targets (размеры кликабельных элементов)

#### ⚠️ Проблемы
- Floating CTA на mobile (5rem от низа) — может быть перекрыто системными UI (iOS safe-area)
- Кнопки форм — достаточны (padding 1rem 2.5rem)
- День-header — высота нужна проверка (mobile)

### 1.3 Читаемость

#### ✅ Отлично
- Иерархия заголовков (h1 → h2 → h3)
- Размер шрифта: 18px (desktop), 16px (mobile)
- line-height: 1.7 — комфортно
- Контраст: белый на темном / темный на белом — WCAG AAA
- .day-title: адаптивный цвет (темный/белый)

### 1.4 Навигация

#### ✅ Хорошо
- Smooth scroll работает
- Anchor links корректны (#booking, #program, #top)
- prefers-reduced-motion учитывается

#### ⚠️ Улучшения
- Нет breadcrumbs (но для one-page сайта не критично)
- Нет "skip to content" link для screen readers

---

## 2. ФУНКЦИОНАЛЬНОСТЬ

### 2.1 Критичные функции

#### ✅ Форма бронирования
- ✅ AJAX отправка (fetch API)
- ✅ Обработка ошибок (try/catch)
- ✅ Feedback пользователю (modal "Спасибо")
- ✅ Honeypot защита (_honey)
- ✅ HTML5 валидация (required fields)
- ✅ Button disabled во время отправки
- ✅ Текст кнопки меняется ("Отправка...")
- **Функциональность: 100%**

#### ✅ Аккордеоны дней
- ✅ Toggle работает (click)
- ✅ Клавиатура работает (Enter/Space)
- ✅ Закрывает другие при открытии (accordion behavior)
- ✅ aria-expanded обновляется
- **Функциональность: 100%**

#### ✅ Floating CTA
- ✅ Показывается после hero
- ✅ Скрывается при достижении booking
- ✅ Throttling через requestAnimationFrame (оптимизация)
- **Функциональность: 100%**

#### ✅ Динамический контент
- ✅ content.js загружается
- ✅ Рендеринг работает корректно
- ✅ Типографика применяется
- ✅ Нет ошибок в консоли (после исправления P0)
- **Функциональность: 100%**

### 2.2 Граничные случаи

#### ⚠️ Потенциальные проблемы
- Формa: что если Formspree недоступен? — есть fallback alert
- Модальное окно: что если JS отключён? — форма всё равно отправится (fallback на Formspree redirect)
- Content.js не загрузился? — сайт пустой (нет graceful degradation)

### 2.3 Производительность

#### ✅ Отлично
- requestAnimationFrame для scroll events
- Минимум re-renders
- Статический контент
- 4763 байт content.js
- Нет memory leaks (проверка нужна в долгосрочной перспективе)

---

## 3. ОБЪЕКТИВНАЯ КРАСОТА

### 3.1 Визуальная гармония

#### ✅ Цветовая палитра
- Midnight Blue (#1A2332) — элегантно
- Chrome (#C0C0C0) — ар-деко
- Accent Red (#E31B1B) — акцент
- Bronze gradient (hero accent) — роскошно
- **Гармония: 10/10**

#### ✅ Типографика
- Cormorant Garamond (serif) — изящество
- Montserrat (sans-serif) — современность
- Контраст serif/sans-serif — профессионально
- Oldstyle numbers — утончённость
- **Типография: 10/10**

#### ✅ Пространство (whitespace)
- Padding секций: адекватный
- margin-bottom: консистентный
- .container: не перегружен
- **Spacing: 9/10**

#### ⚠️ Анимации
- Transitions: 0.3s — комфортно
- cubic-bezier(0.4, 0, 0.2, 1) — плавно
- НО: Floating CTA transform может быть smoother
- **Анимации: 8/10**

### 3.2 Визуальная иерархия

#### ✅ Отлично
- Hero: доминирует (100&nbsp;лет — крупно, бронза)
- Секции: чётко разделены
- CTA кнопки: выделяются (красный, тень)
- **Иерархия: 10/10**

### 3.3 Детали

#### ✅ Превосходно
- Bronze gradient с shine animation — роскошно
- Bullet points (■) — конгруэнтны ар-деко
- Day number opacity на mobile — тонко
- Modal icon (✓) — минималистично
- **Детали: 10/10**

### 3.4 Респонсив
- ✅ Mobile-first
- ✅ clamp() для адаптивных размеров
- ✅ Grid/Flexbox корректно
- ✅ Нет horizontal scroll (overflow-x: hidden)
- **Респонсив: 10/10**

---

## КРИТИЧНЫЕ ПРОБЛЕМЫ (требуют исправления)

### P1: Эргономика интерактивных элементов

#### 1. .day-header (аккордеоны)
**Проблема:** Нет визуальной обратной связи при hover/focus

**Решение:**
```css
.day-header {
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.day-header:hover {
  background-color: rgba(192, 192, 192, 0.05);
}

.day-header:focus {
  outline: 2px solid var(--chrome);
  outline-offset: -2px;
}

.day-header:focus-visible {
  outline: 2px solid var(--chrome);
  outline-offset: -2px;
}
```

#### 2. Form inputs
**Проблема:** Нет hover/focus состояний

**Решение:**
```css
input[type="text"],
input[type="email"],
input[type="tel"] {
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

input:hover {
  border-color: var(--chrome);
}

input:focus {
  outline: none;
  border-color: var(--accent-red);
  box-shadow: 0 0 0 3px rgba(227, 27, 27, 0.1);
}

input[type="checkbox"]:focus {
  outline: 2px solid var(--chrome);
  outline-offset: 2px;
}
```

#### 3. .back-to-top
**Проблема:** Нужна проверка hover/focus

**Решение:**
```css
.back-to-top {
  transition: transform 0.2s ease, color 0.2s ease;
}

.back-to-top:hover {
  transform: translateY(-3px);
  color: var(--chrome);
}

.back-to-top:focus-visible {
  outline: 2px solid var(--chrome);
  outline-offset: 3px;
}
```

---

## РЕКОМЕНДАЦИИ (опционально)

### P2: Улучшения эргономики

1. **Touch targets на mobile**
   - Увеличить минимальный размер до 44x44px (Apple HIG)
   - Проверить safe-area на iOS для floating CTA

2. **Loading states**
   - Skeleton screens для content.js (если медленное соединение)
   - Spinner для формы (вместо только текста "Отправка...")

3. **Graceful degradation**
   - Статический fallback контент в HTML (без JS)
   - noscript предупреждение

4. **Микро-interactions**
   - Ripple effect на кнопках (Material Design inspired)
   - Subtle bounce на Floating CTA появлении

---

## ИТОГОВАЯ ОЦЕНКА

| Критерий | Оценка | Комментарий |
|----------|--------|-------------|
| **1. Эргономика** | **7.5/10** | Хорошо, но нужны hover/focus для всех интерактивных элементов |
| **2. Функциональность** | **9.5/10** | Отлично, все работает, но нет graceful degradation |
| **3. Объективная красота** | **9.5/10** | Превосходно, профессиональный визуал, ар-деко стиль |

### ПРИОРИТЕТНЫЕ ДЕЙСТВИЯ

1. **[P1] Добавить hover/focus для .day-header** — критично для эргономики
2. **[P1] Добавить hover/focus для form inputs** — критично для UX
3. **[P1] Добавить hover/focus для .back-to-top** — важно для консистентности
4. **[P2] Проверить iOS safe-area** — может перекрывать Floating CTA
5. **[P2] Skeleton/fallback для content.js** — улучшит perceived performance

---

**ВЫВОД:**

Проект имеет **высокое качество** по всем трём критериям, но **эргономика** может быть усилена через добавление визуальной обратной связи для всех интерактивных элементов. Функциональность и красота — на уровне профессионального продукта.

**Рекомендация:** Исправить P1 проблемы для достижения 9+/10 по эргономике.

