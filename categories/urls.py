from django.urls import path
from categories.views import books_by_category,show_category,get_book_json,get_book_json_all,show_all

app_name = 'categories'

urlpatterns = [
    path('', show_category, name='show-category'),
    path('<str:category_name>/',books_by_category, name='books_by_category'),
    path('<str:category_name>/books_json/', get_book_json, name='get_book_json'),
    path('all/', show_all, name='show_all'),
    path('all/books_json_all/', get_book_json_all, name='get_book_json_all'),
]