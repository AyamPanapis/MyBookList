from django.shortcuts import render
import requests
from categories.models import Category
from dataset.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

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


def get_book_json(request,category_name):
    book = Book.objects.filter(categories=category_name)
    data = serializers.serialize('json', book)
    return HttpResponse(data, content_type='application/json')

def show_all(request):
    books = Book.objects.all()
    return render(request,'all.html',{'books':books})

def get_book_json_all(request):
    book = Book.objects.all()
    data = serializers.serialize('json', book)
    return HttpResponse(serializers.serialize('json', book))


