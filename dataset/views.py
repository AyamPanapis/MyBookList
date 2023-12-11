from django.shortcuts import render
from django.http import HttpResponse
from dataset.models import Book
from django.core import serializers

# Create your views here.
def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

