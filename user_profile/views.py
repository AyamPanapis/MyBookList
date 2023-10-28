from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from dataset.models import Book
from user_profile.models import UserProfile
from book.models import WishList
from django.http import JsonResponse

@login_required
def show_profile(request):
    user = request.user
    date_joined_wib = user.date_joined.astimezone(timezone.get_current_timezone())

    planned_to_read_book_ids = WishList.objects.filter(user=user, book_list=0).values_list('book', flat=True)
    reading_book_ids = WishList.objects.filter(user=user, book_list=1).values_list('book', flat=True)
    completed_book_ids = WishList.objects.filter(user=user, book_list=2).values_list('book', flat=True)

    planned_to_read_books = Book.objects.filter(id__in=planned_to_read_book_ids)
    reading_books = Book.objects.filter(id__in=reading_book_ids)
    completed_books = Book.objects.filter(id__in=completed_book_ids)

    context = {
        'username': user.username,
        'date_joined': date_joined_wib,
        'planned_to_read_books': planned_to_read_books,
        'reading_books': reading_books,
        'completed_books': completed_books,
    }
    return render(request, 'profile.html', context)

