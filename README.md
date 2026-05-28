# Flea Market

Простий додаток для купівлі-продажу речей. Платформа, де кожен може бути як покупцем, так і продавцем.

## Getting Started

Це інструкція для встановлення та запуску проекту локально.

### Prerequisites

- Python 3.12+
- pip (менеджер пакетів Python)
- Git

### Installation

1. Клонуй репозиторій

```bash
git clone <repository-url>
cd flea_market
```

2. Створи віртуальне середовище

```bash
python -m venv .venv
source .venv/bin/activate  # На Windows: .venv\Scripts\activate
```

3. Встанови залежності

```bash
pip install -r requirements.txt
```

4. Застосуй міграції

```bash
python manage.py migrate
```

5. Створи суперюзера (для адмін панелі)

```bash
python manage.py createsuperuser
```

6. Запусти сервер розробки

```bash
python manage.py runserver
```

Додаток буде доступний на http://127.0.0.1:8000/

## Usage

Можно використати вхід тестовим користувачем:

login: admin
password: admin

### Для покупців

1. Зареєструйся на платформі
2. Переглянь список усіх товарів
3. Використовуй пошук по назві або фільтрацію по категоріях
4. Додавай цікаві товари до вішліста
5. Купуй товари, які тебе цікавлять

### Для продавців

1. Залогінься в свій аккаунт
2. Перейди на "Sell something"
3. Заповни деталі товару (назва, опис, ціна, категорія)
4. Опублікуй оголошення
5. Чекай на покупців

### Адміністрування

Адмін панель доступна на http://127.0.0.1:8000/admin/

Тут ти можеш:
- Керувати користувачами
- Переглядати та видаляти оголошення
- Керувати категоріями
- Переглядати завершені угоди

## Features

- Управління профілем користувача
- Створення, редагування та видалення оголошень
- Пошук та фільтрація товарів по категоріях
- Система вишліста (додавання товарів до улюблених)
- Система покупок (Deal) для відстеження проданих товарів
- Email верифікація при реєстрації
-响應ний дизайн на базі Bootstrap 4

## Project Structure

```
flea_market/
├── core/                    # Основні налаштування Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # Управління користувачами
│   ├── models.py           # User модель
│   ├── views.py            # Реєстрація, активація
│   ├── forms.py
│   ├── urls.py
│   └── services/           # Бізнес-логіка
│       ├── user_service.py
│       ├── email_service.py
│       ├── activation_token_service.py
│       └── errors.py
├── market/                  # Основна функціональність
│   ├── models.py           # Item, Category, Deal
│   ├── views.py            # Представлення
│   ├── forms.py            # Форми
│   ├── urls.py
│   └── admin.py            # Адмін конфігурація
├── templates/               # HTML шаблони
├── static/                  # CSS, JS, зображення
└── manage.py
```

## Technology Stack

- Django 6.0.5
- Python 3.12
- SQLite3 (розробка) / PostgreSQL (production)
- Bootstrap 4.5
- django-crispy-forms

## Deployment

Проект налаштований для развертування на Render.

1. Подели репо на GitHub
2. Создай новий сервіс на Render
3. Підключи GitHub репо
4. Налаштуй environment variables в Render
5. Deploy

## Contact

Email: eyelja@gmail.com

Маєш питання або пропозиції? Відкрий Issue в репозиторії.

## License

This project is open source and available under the MIT License.