# AlphaStack Academy - Django Website

## Pages
- `/` - Home
- `/about/` - About Us
- `/courses/` - Courses
- `/courses/java/` - Java Programming
- `/courses/python/` - Python Programming
- `/events/` - Upcoming Events
- `/benefits/` - Program Benefits
- `/contact/` - Registration / Contact

## Structure
- `academy/templates/academy/base.html` - common layout, navbar and footer
- Each section/page has its own HTML template
- `academy/static/academy/css/style.css` - shared styling
- `academy/static/academy/images/` - logo and event poster
- `academy/views.py` - page views
- `academy/urls.py` - page URLs

## Run locally

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python manage.py migrate
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

## Important
The registration form is currently a UI form only. It is ready to be connected to a Django model/database and email or WhatsApp notification later.
