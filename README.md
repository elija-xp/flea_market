# Flea Market

A simple buy-and-sell application. A platform where anyone can be both a buyer and a seller.

**Live Demo:** [flea-market-t0eu.onrender.com](https://flea-market-t0eu.onrender.com)

## Getting Started

This is a guide for installing and running the project locally.

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git

### Installation

1. Clone the repository

```bash
git clone <repository-url>
cd flea_market
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create a superuser (for the admin panel)

```bash
python manage.py createsuperuser
```

6. Start the development server

```bash
python manage.py runserver
```

The app will be available at http://127.0.0.1:8000/

## Usage

You can log in with the test user credentials:

login: admin
password: admin

### For Buyers

1. Register on the platform
2. Browse the list of all items
3. Use search by name or filter by category
4. Add interesting items to your wishlist
5. Purchase the items you want

### For Sellers

1. Log in to your account
2. Go to "Sell something"
3. Fill in the item details (name, description, price, category)
4. Publish your listing
5. Wait for buyers

### Administration

The admin panel is available at http://127.0.0.1:8000/admin/

Here you can:
- Manage users
- View and delete listings
- Manage categories
- View completed deals

## Features

- User profile management
- Create, edit, and delete listings
- Search and filter items by category
- Wishlist system (save items to favourites)
- Purchase system (Deal) for tracking sold items
- Email verification on registration
- Responsive design built with Bootstrap 4

## Project Structure

```
flea_market/
├── core/                    # Core Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # User management
│   ├── models.py           # User model
│   ├── views.py            # Registration, activation
│   ├── forms.py
│   ├── urls.py
│   └── services/           # Business logic
│       ├── user_service.py
│       ├── email_service.py
│       ├── activation_token_service.py
│       └── errors.py
├── market/                  # Core functionality
│   ├── models.py           # Item, Category, Deal
│   ├── views.py            # Views
│   ├── forms.py            # Forms
│   ├── urls.py
│   └── admin.py            # Admin configuration
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
└── manage.py
```

## Technology Stack

- Django 6.0.5
- Python 3.12
- SQLite3 (development) / PostgreSQL (production)
- Bootstrap 4.5
- django-crispy-forms

## Deployment

The project is configured for deployment on Render.

1. Push the repo to GitHub
2. Create a new service on Render
3. Connect the GitHub repo
4. Configure environment variables in Render
5. Deploy

## Contact

Email: eyelja@gmail.com

Have questions or suggestions? Open an Issue in the repository.

## License

This project is open source and available under the MIT License.
