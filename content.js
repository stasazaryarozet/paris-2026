const CONTENT = {
  hero: {
    title: "Индивидуальный почерк ар-деко.<br><span class=\"hero-accent\">100&nbsp;лет</span>.",
    subtitle: "4&nbsp;дня с&nbsp;кураторами.<br>Фактуры, материалы, атмосфера.<br>То, что не&nbsp;видно в&nbsp;публикациях.",
    dates: "15–18+ января 2026",
    group: "до&nbsp;12 человек",
    price: "1 550&nbsp;€"
  },
  meta: {
    title: "Индивидуальный почерк ар-деко. 100&nbsp;лет&nbsp;— 4&nbsp;дня в&nbsp;Париже (январь 2026)",
    description: "4&nbsp;дня в&nbsp;Париже. Фактуры, материалы, атмосфера. Ольга и Наталья. Галереи, отели, шоу-румы. Малые группы.",
    keywords: "Paris Art Deco, ар-деко Париж, Palais de Tokyo, Nolinski, Galerie Vallois, Maison Louis Carré",
    ogTitle: "Индивидуальный почерк ар-деко. 100&nbsp;лет",
    ogDescription: "4&nbsp;дня. Фактуры, материалы, атмосфера. То, что не&nbsp;видно в&nbsp;публикациях.",
    ogImage: "https://www.parisinjanuary.ru/og-image.jpg",
    url: "https://www.parisinjanuary.ru"
  },
  program: {
    intro: [
      "Денье, Легре (Legré), Эйлин Грей, Аалто. У&nbsp;каждого свой почерк.",
      "В&nbsp;интерьерах видны соотношения фактур, тонкости цвета, работа с&nbsp;материалами. В&nbsp;публикациях этого нет.",
      {
        type: "highlight",
        text: "Парижские дизайнеры смешивают новое со&nbsp;старым. Интерьер без предметов с&nbsp;историей выглядит неживо."
      }
    ]
  },
  days: [
    {
      number: "ДЕНЬ I",
      date: "15 января",
      title: "Правый берег",
      theme: "",
      locations: [
        {
          name: "Прантан (Printemps)",
          description: "Переход от&nbsp;Нуво к&nbsp;Деко. Материалы, металл, цвет."
        },
        {
          name: "Нолински (Nolinski)",
          description: "Денье: острая геометрия, парижский шик."
        },
        {
          name: "Легре (Legré)",
          description: "Шоу-рум как дом. Дорогие материалы."
        },
        {
          name: "Музей",
          description: "Выбор Натальи."
        }
      ]
    },
    {
      number: "ДЕНЬ II",
      date: "16 января",
      title: "Левый берег",
      theme: "",
      locations: [
        {
          name: "Сен-Жермен (Saint-Germain)",
          description: "Квартал антикваров. Лак, хром, фанеровка."
        },
        {
          name: "Галерея Валлуа (Galerie Vallois)",
          description: "Встреча с&nbsp;владелицей. 20–30-е."
        },
        {
          name: "Эйлин Грей (Eileen Gray)",
          description: "Наблюдение за&nbsp;поведением человека. Эргономика через заботу."
        },
        {
          name: "Пале-де-Токио + Трокадеро (Palais de Tokyo + Trocadéro)",
          description: "Выставка 1937&nbsp;года. Ар-деко."
        }
      ]
    },
    {
      number: "ДЕНЬ III",
      date: "17 января",
      title: "Мезон-э-Обже (Maison & Objet)",
      theme: "",
      locations: [
        {
          name: "Мезон-э-Обже (Maison & Objet)",
          description: "Главная выставка дизайна. Тренды, имена."
        },
        {
          name: "Вечер: маршрут 1925",
          description: "Трасса выставки, давшей имя стилю."
        }
      ]
    },
    {
      number: "ДЕНЬ IV",
      date: "18+ января",
      title: "Аалто: тепло в&nbsp;модернизме",
      theme: "",
      locations: [
        {
          name: "Мезон Луи Карре (Maison Louis Carré, 1956–59)",
          description: "Дерево, объём, свет. Тепло в&nbsp;модернизме."
        },
        {
          name: "Парк",
          description: "Ландшафт&nbsp;— продолжение архитектуры."
        },
        {
          name: "Вечер",
          description: "Разговор о&nbsp;четырёх днях."
        }
      ]
    },
    {
      number: "ДЕНЬ V",
      date: "19 января (опционально)",
      title: "Продолжение",
      theme: "",
      locations: [
        {
          name: "Маршрут от&nbsp;Ольги и Натальи",
          description: "Места, которые не&nbsp;успели. Авторский гайд."
        }
      ]
    }
  ],
  curators: [
    {
      name: "Ольга Розет",
      role: "Дизайнер, декоратор, искусствовед",
      bio: [
        "30+ лет в&nbsp;дизайне интерьеров и кураторской работе",
        "Куратор программ в&nbsp;Высшей Британской школе дизайна",
        "Авторские путешествия с&nbsp;2008&nbsp;года",
        "Материалы, геометрия, история стиля",
        "Диалог, а не&nbsp;лекция",
        "Показывает то, что работает"
      ]
    },
    {
      name: "Наталья Логинова",
      role: "Автор дизайн-туров",
      bio: [
        "Журналист ТК «Культура» (до&nbsp;переезда)",
        "Главный редактор журнала «Московское наследие» (до&nbsp;переезда)",
        "Живёт в&nbsp;Париже",
        "Авторские туры по&nbsp;дизайну и архитектуре",
        "Истории людей и мест"
      ]
    }
  ],
  inclusions: [
    {
      icon: "+",
      title: "Кураторы 4&nbsp;дня",
      description: "Материалы, чат"
    },
    {
      icon: "±",
      title: "Входы и встречи",
      description: "Часть включена, часть&nbsp;— отдельно"
    },
    {
      icon: "−",
      title: "Отдельно",
      description: "Перелет, проживание, питание"
    },
    {
      icon: "€",
      title: "Стоимость",
      description: "",
      price: "1 550&nbsp;€"
    }
  ]
};
