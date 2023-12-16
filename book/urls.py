from django.urls import path
from book.views import show_books, to_read, reading, finished_reading, create_review_flutter, wishlist_flutter, show_review_json

app_name = 'book'

urlpatterns = [
    path('<int:book_id>/', show_books, name='show_books'),
    path('to-read/<int:book_id>/<int:user_id>/', to_read, name='to_read'),
    path('reading/<int:book_id>/<int:user_id>/', reading, name='reading'),
    path('finished-reading/<int:book_id>/<int:user_id>/', finished_reading, name='finished_reading'),
    path('create-review/', create_review_flutter, name='create_review_flutter'),
    path('wishlist/<int:book_id>/', wishlist_flutter, name='wishlist_flutter'),
    path('show-review-json/<int:book_id>/', show_review_json, name='show_review_json'),
]