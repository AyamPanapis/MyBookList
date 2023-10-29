from django.shortcuts import render
from django.shortcuts import redirect
from dataset.models import Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserBook
import random
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
# Get the total number of books in the dataset
    total_books = Book.objects.count()

    # Generate a list of 10 unique random indices to select 10 random books
    random_indices = random.sample(range(1, total_books + 1), 10)

    # Retrieve the 10 random books
    books = Book.objects.filter(pk__in=random_indices)

    context = {
        'username': request.user.username,
        'books': books,
    }
    return render(request, 'main.html', context)

def result(request):
    search = request.GET.get('search')
    if search:
        # Search for books with titles or authors similar to the search query
        books = Book.objects.filter(
            Q(title__icontains=search) | Q(author__icontains=search)
        )
    else:
        books = None 
    
    context = {
        'books': books,
    }

    return render(request, 'result.html', context)

def get_random_books_json(request):
    total_books = Book.objects.count()
    random_indices = random.sample(range(1, total_books + 1), 10)
    getbook = Book.objects.filter(pk__in=random_indices)
    data = serializers.serialize('json', getbook)
    return HttpResponse(data, content_type='application/json')