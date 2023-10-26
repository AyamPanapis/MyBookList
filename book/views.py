from django.shortcuts import render
import requests

# Create your views here.
def show_books(request, id):
    bookID = str(id)
    key = "AIzaSyBI3X3uNtQjYLQcrf-q9Bb-bk74SG0CTbw"

    queries = {'key':key}

    r = requests.get(f'https://www.googleapis.com/books/v1/volumes/{bookID}', params=queries)

    data = r.json()
    book = data
    book_dict = {
        'title': book['volumeInfo']['title'],
        'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
        'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
        'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
        'description': book['volumeInfo']['description'] if 'description' in book['volumeInfo'] else "No description available.",
        'categories': ", ".join(book['volumeInfo']['categories']) if 'categories' in book['volumeInfo'] else 'No categories available.',
    }
    return render(request, 'book.html', {'book':book_dict})



