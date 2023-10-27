from django.urls import path
from book.views import show_books, to_read, reading, finished_reading

app_name = 'book'

urlpatterns = [
    path('<int:book_id>/', show_books, name='show_books'),
    path('to-read/<int:book_id>/<int:user_id>/', to_read, name='to_read'),
    path('reading/<int:book_id>/<int:user_id>/', reading, name='reading'),
    path('finished-reading/<int:book_id>/<int:user_id>/', finished_reading, name='finished_reading'),
]