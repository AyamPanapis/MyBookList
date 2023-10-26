from django.shortcuts import render
import requests
from categories.models import Book

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = "AIzaSyBI3X3uNtQjYLQcrf-q9Bb-bk74SG0CTbw"


def show_books(request):
    categories = ['Fiction', 'History', 'Science', 'Art', 'Economics', 'Philosophy']
    book_all = {}
    for category in categories:
        books_data = fetch_books(category)
        books = []
        for book_data in books_data:
            volume_info = book_data['volumeInfo']
            book = Book(
                title=volume_info.get('title', ''),
                authors=','.join(volume_info.get('authors', [])),
                publisher=volume_info.get('publisher', ''),
                description=volume_info.get('description', ''),
                image_link=volume_info.get('imageLinks', {}).get('thumbnail', ''),
                category=category
            )
            books.append(book)
        book_all[category] = books
    return render(request, 'categories.html', {'book_all': book_all})

def fetch_books(category, max_results=40):
    params = {
        'q': f"subject:{category}",
        'maxResults': max_results,
        'key': API_KEY
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()['items']
    return []