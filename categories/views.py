from django.shortcuts import render
import requests
from categories.models import Category
from dataset.models import Book

def show_category(request):
    distinct_categories = Book.objects.values_list('categories', flat=True).distinct()
    context = {
        'categories': distinct_categories
    }
    return render(request, 'categories.html', context)


def books_by_category(request, category_name):
    books = Book.objects.filter(categories=category_name)
    template_name = f'{category_name}.html'
    return render(request, template_name, {'books': books, 'category_name': category_name})
