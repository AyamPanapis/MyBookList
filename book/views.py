from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from dataset.models import Book
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
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
