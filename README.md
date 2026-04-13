# Сайт визажиста (Django REST + Vue)

Одностраничный сайт в темных тонах с бэкендом на **Django + Django REST Framework** и фронтендом на **Vue 3**.

## Возможности
- Редактирование текста, прайса, контактов и фотографий через Django Admin.
- REST API для фронтенда (`/api/content/`, `/api/services/`, `/api/portfolio/`).
- Демо-данные и сгенерированные фотографии через команду `seed_demo`.

## Запуск
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Откройте:
- `http://127.0.0.1:8000/` — сайт
- `http://127.0.0.1:8000/admin/` — админка

## Что редактируется в админке
- **Контент сайта**: заголовки, описания, контакты, главные изображения.
- **Прайс-лист**: список услуг и стоимость.
- **Портфолио**: галерея фотографий.
