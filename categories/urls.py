from django.urls import path
from categories.views import books_by_category,show_category

app_name = 'categories'

urlpatterns = [
    path('', show_category, name='show-category'),
    path('<str:category_name>/',books_by_category, name='books_by_category'),
]