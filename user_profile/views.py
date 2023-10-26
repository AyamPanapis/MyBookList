from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from main.models import Book

@login_required
def show_profile(request):
    user = request.user
    date_joined_wib = user.date_joined.astimezone(timezone.get_current_timezone())
    read_books = get_user_books(user, '0')
    planned_books = get_user_books(user, '2')
    reading_books = get_user_books(user, '3')
    read_books_count = read_books.count()
    planned_books_count = planned_books.count()
    reading_books_count = reading_books.count()
    context = {
        'username': user.username,
        'date_joined': date_joined_wib,
        'read_books': read_books,
        'planned_books': planned_books,
        'reading_books': reading_books,
        'read_books_count': read_books_count,
        'planned_books_count': planned_books_count,
        'reading_books_count': reading_books_count,
    }
    return render(request, 'profile.html', context)
 
def get_user_books(user, status):
    return Book.objects.filter(user=user, status=status)
