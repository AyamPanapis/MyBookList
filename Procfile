release: django-admin migrate --noinput && python manage.py insertdata && python manage.py tailwind start
web: gunicorn MyBookList.wsgi:application