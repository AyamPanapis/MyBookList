from django.urls import path
from book.views import show_books

app_name = 'book'

urlpatterns = [
    path('<str:id>/', show_books, name='show_books'),
    path('review/add/<str:book_id>/', add_review, name='add_review'),  # assuming book_id is a string, change to int if it's an integer
    path('review/user/<str:username>/', user_review_list, name='user_review_list'),
    path('review/user/', user_review_list, name='user_review_list_self'),
]