from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from dataset.models import Book
from user_profile.models import UserProfile
from book.models import WishList
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

@login_required(login_url='/auth/login/')
def show_profile(request, id):
    user = request.user
    date_joined_wib = user.date_joined.astimezone(timezone.get_current_timezone())

    planned_to_read_book_ids = WishList.objects.filter(user=user, book_list=0).values_list('book', flat=True)
    reading_book_ids = WishList.objects.filter(user=user, book_list=1).values_list('book', flat=True)
    completed_book_ids = WishList.objects.filter(user=user, book_list=2).values_list('book', flat=True)

    planned_to_read_books = Book.objects.filter(id__in=planned_to_read_book_ids)
    reading_books = Book.objects.filter(id__in=reading_book_ids)
    completed_books = Book.objects.filter(id__in=completed_book_ids)

    # Count the total number of books in each section
    planned_count = planned_to_read_books.count()
    reading_count = reading_books.count()
    completed_count = completed_books.count()

    context = {
        'username': user.username,
        'date_joined': date_joined_wib,
        'planned_to_read_books': planned_to_read_books,
        'reading_books': reading_books,
        'completed_books': completed_books,
        'planned_count': planned_count,
        'reading_count': reading_count,
        'completed_count': completed_count,
    }
    return render(request, 'profile.html', context)

def get_planned_json(request):
    user = request.user

    planned_to_read_book_ids = WishList.objects.filter(user=user, book_list=0).values_list('book', flat=True)

    planned_to_read_books = Book.objects.filter(id__in=planned_to_read_book_ids)
    return HttpResponse(serializers.serialize('json', planned_to_read_books), content_type="application/json")

def get_reading_json(request):
    user = request.user

    reading_book_ids = WishList.objects.filter(user=user, book_list=1).values_list('book', flat=True)

    reading_books = Book.objects.filter(id__in=reading_book_ids)
    return HttpResponse(serializers.serialize('json', reading_books), content_type="application/json")


def get_completed_json(request):
    user = request.user

    completed_book_ids = WishList.objects.filter(user=user, book_list=2).values_list('book', flat=True)

    completed_books = Book.objects.filter(id__in=completed_book_ids)
    return HttpResponse(serializers.serialize('json', completed_books),content_type="application/json")

@csrf_exempt
def get_planned_json_flutter(request):
    user = request.user
    planned_to_read_book_ids = WishList.objects.filter(user=user.pk,book_list=0).values_list('book', flat=True)

    planned_to_read_books = Book.objects.filter(id__in=planned_to_read_book_ids)
    return HttpResponse(serializers.serialize('json', planned_to_read_books), content_type="application/json")

@csrf_exempt
def get_reading_json_flutter(request):
    user = request.user
    reading_book_ids = WishList.objects.filter(user=user.pk,book_list=1).values_list('book', flat=True)

    reading_books = Book.objects.filter(id__in=reading_book_ids)
    return HttpResponse(serializers.serialize('json', reading_books), content_type="application/json")

@csrf_exempt
def get_completed_json_flutter(request):
    user = request.user
    completed_book_ids = WishList.objects.filter(user=user.pk,book_list=2).values_list('book', flat=True)

    completed_books = Book.objects.filter(id__in=completed_book_ids)
    return HttpResponse(serializers.serialize('json', completed_books),content_type="application/json")



