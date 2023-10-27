from django.urls import path
from book.views import show_books

app_name = 'book'

urlpatterns = [
    path('<int:book_id>/', show_books, name='show_books'),
]