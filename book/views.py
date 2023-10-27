from django.shortcuts import render
import requests
from dataset.models import Book

# Create your views here.
def show_books(request,title):
    books = Book.objects.filter(title=title)

    context = {
        'title': title,
        'books': books,
    }

    return render(request, 'book.html', context)



