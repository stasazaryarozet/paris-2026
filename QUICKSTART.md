# Быстрый старт

## Изменить текст

1. Открой `content.js`
2. Измени нужное поле
3. Сохрани
4. Открой `index.html` в браузере — увидишь изменения

## Развернуть на сайте

```bash
surge --project . --domain paris-art-deco-2026.surge.sh
```

## Примеры правок

### Изменить заголовок
```javascript
hero: {
  title: "Новый заголовок",
  ...
}
```

### Добавить локацию в день
```javascript
days: [
  {
    number: "ДЕНЬ I",
    locations: [
      { name: "Новое место", description: "Описание" }
    ]
  }
]
```

### Изменить цену
```javascript
hero: {
  price: "1 600 €"
}

inclusions: [
  {
    icon: "💶",
    title: "Стоимость",
    price: "1 600 €",
    description: "Депозит: 0 €"
  }
]
```

Все изменения сразу видны локально, деплой занимает 10 секунд.

