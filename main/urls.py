from django.urls import path
from main.views import show_main, result, get_random_books_json



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('result/', result, name='result'),
    path('get-product/', get_random_books_json, name='get_random_books_json'),
]