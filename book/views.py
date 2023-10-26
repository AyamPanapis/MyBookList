from django.shortcuts import render
import requests
####
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Book
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def show_books(request, id):
    bookID = str(id)
    key = "AIzaSyBI3X3uNtQjYLQcrf-q9Bb-bk74SG0CTbw"

    queries = {'key':key}

    r = requests.get(f'https://www.googleapis.com/books/v1/volumes/{bookID}', params=queries)

    data = r.json()
    book = data
    book_dict = {
        'title': book['volumeInfo']['title'],
        'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
        'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
        'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
        'description': book['volumeInfo']['description'] if 'description' in book['volumeInfo'] else "No description available.",
        'categories': ", ".join(book['volumeInfo']['categories']) if 'categories' in book['volumeInfo'] else 'No categories available.',
    }
    return render(request, 'book.html', {'book':book_dict})

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.book = book
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        return HttpResponseRedirect(reverse('reviews:book_detail.html', args=(book.id,)))

    return render(request, 'reviews/book_detail.html', {'book': book, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)
