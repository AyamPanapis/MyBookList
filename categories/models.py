from django.db import models
from dataset.models import Book

class Category(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.categories