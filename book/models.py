from django.db import models
from dataset.models import Book

# Create your models here.

class BookShow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.title