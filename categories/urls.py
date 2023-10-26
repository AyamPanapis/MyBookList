from django.urls import path
from categories.views import show_books

app_name = 'categories'

urlpatterns = [
    path('', show_books, name='show-books'),
]