# Сайт визажиста (Django REST + Vue)

Одностраничный сайт в темных тонах с бэкендом на **Django + Django REST Framework** и фронтендом на **Vue 3**.

## Возможности
- Редактирование текста, прайса, контактов и фотографий через Django Admin.
- REST API для фронтенда (`/api/content/`, `/api/services/`, `/api/portfolio/`).
- Демо-данные и сгенерированные фотографии через команду `seed_demo`.

## Быстрый старт
> Ниже команды для Linux/macOS (zsh/bash). Если у вас нет команды `python`, используйте `python3`.

```bash
git clone <URL_ВАШЕГО_РЕПО> site
cd site
cd backend

# Проверка, что Python установлен
python3 --version

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Если команда `source .venv/bin/activate` не срабатывает — значит виртуальное окружение не создалось на предыдущем шаге.

## Где открыть сайт
- `http://127.0.0.1:8000/` — сайт
- `http://127.0.0.1:8000/admin/` — админка

## Что редактируется в админке
- **Контент сайта**: заголовки, описания, контакты, главные изображения.
- **Прайс-лист**: список услуг и стоимость.
- **Портфолио**: галерея фотографий.

## Типичные ошибки
1. `cd: no such file or directory: /workspace/site/backend`
   - Вы запускаете команду в другом окружении/пути. Проверьте сначала `pwd`, затем `ls`.
   - Нужно находиться в корне проекта, где есть папка `backend`.

2. `zsh: command not found: python` / `pip`
   - Используйте `python3` и `python3 -m pip`.
   - Установите Python 3 (macOS: `brew install python`).
