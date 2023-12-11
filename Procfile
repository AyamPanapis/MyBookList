release: django-admin migrate --noinput && && python manage.py insertdata
web: gunicorn MyBookList.wsgi:application