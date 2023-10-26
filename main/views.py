from django.shortcuts import render
from django.shortcuts import redirect
from dataset.models import Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserBook

@login_required(login_url='auth/login/')
def show_main(request):
    context = {
        'username': request.user.username,
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
