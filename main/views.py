from django.shortcuts import render
import requests
from django.shortcuts import redirect
from .forms import BookSearch

def show_main(request):
    form = BookSearch()

    context = {
        'username': request.user.username,
        'form': form,
    }
    return render(request, 'main.html', context)

def result(request):
    search = request.GET.get('search')
    key = "AIzaSyBI3X3uNtQjYLQcrf-q9Bb-bk74SG0CTbw"
    if (search == False) or (search == ""):
        return redirect('/')

    queries = {'q': search, 'key': key, 'langRestrict': 'en', 'printType': 'books'}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)
    if r.status_code != 200:
        return render(request, 'result.html', {'message': 'Sorry, there seems to be an issue with Google Books right now.'})

    data = r.json()

    if not 'items' in data:
        return render(request, 'result.html', {'message': 'Sorry, no books match that search term.'})

    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
            'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
            'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
            'info': book['volumeInfo']['infoLink'],
            'id': book['id']
        }
        books.append(book_dict)
    return render(request, 'result.html', {'books': books})
