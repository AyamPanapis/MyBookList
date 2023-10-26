from django.shortcuts import render
import requests
from dataset.models import Book
from django.core.management.base import BaseCommand, CommandError

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = "AIzaSyBI3X3uNtQjYLQcrf-q9Bb-bk74SG0CTbw"

class Command(BaseCommand):

    help = 'Fetch and insert books from Google Books API to the database'

    def fetch_books(self, category, max_results=20):
        params = {
            'q': f"subject:{category}",
            'maxResults': max_results,
            'key': API_KEY,
            'langRestrict': 'en',
            'printType': 'books'
        }
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code == 200:
            return response.json().get('items', [])
        return []

    def save_books_to_database(self, category, books_data):
        for book_data in books_data:
            volume_info = book_data['volumeInfo']
            book = Book(
                title=volume_info.get('title', ''),
                author=','.join(volume_info.get('authors', [])),
                publisher=volume_info.get('publisher', ''),
                description=volume_info.get('description', ''),
                image_link=volume_info.get('imageLinks', {}).get('thumbnail', ''),
                categories=category
            )
            book.save()


    
    def handle(self, *args, **options):
            categories = ['Fiction', 'History', 'Science', 'Art', 'Economics', 'Philosophy']
            for category in categories:
                books_data = self.fetch_books(category)
                self.save_books_to_database(category, books_data)
                self.stdout.write(self.style.SUCCESS(f'Successfully inserted books for category: {category}'))