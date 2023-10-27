from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from dataset.models import Book
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def show_books(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    print(type(book))
    reviews = Review.objects.filter(book_id=book_id).order_by('-pub_date')
    print(reviews)

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

    context = {'book': book, 'reviews': reviews, 'form': form}
    return render(request, 'book.html', context)
