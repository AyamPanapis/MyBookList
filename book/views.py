from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from dataset.models import Book
from .models import Review, WishList
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.db.models import Avg

@login_required
def show_books(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    print(type(book))
    reviews = Review.objects.filter(book_id=book_id).order_by('-pub_date')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.user_name = request.user.username
            new_review.pub_date = datetime.datetime.now()
            new_review.save()
            return HttpResponseRedirect(f"/book/{book_id}/")
    else:
        form = ReviewForm()

    average_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 2)  # Assuming 'rating' is the field in your Review model.
    if average_rating is None:
        average_rating = "No ratings yet"

    context = {'book': book, 'reviews': reviews, 'form': form, 'average_rating': average_rating}
    return render(request, 'book.html', context)

@login_required
def to_read(request, book_id, user_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    try:
        wishlist = WishList.objects.get(book=book.pk, user=user)
        wishlist.book_list = 0
        wishlist.save()
    except WishList.DoesNotExist:
        WishList.objects.create(book=book.pk, user=user, book_list=0)
    return HttpResponse(b"TO_READ", status=201)

@login_required
def reading(request, book_id, user_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    try:
        wishlist = WishList.objects.get(book=book.pk, user=user)
        wishlist.book_list = 1
        wishlist.save()
    except WishList.DoesNotExist:
        WishList.objects.create(book=book.pk, user=user, book_list=1)
    return HttpResponse(b"READING", status=201)

@login_required
def finished_reading(request, book_id, user_id):
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)
    try:
        wishlist = WishList.objects.get(book=book.pk, user=user)
        wishlist.book_list = 2
        wishlist.save()
    except WishList.DoesNotExist:
        WishList.objects.create(book=book.pk, user=user, book_list=2)
    return HttpResponse(b"FINISH", status=201)


    