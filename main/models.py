from django.db import models
from django.contrib.auth.models import User
from dataset.models import Book

# Create your models here.

# create database taking all the data from the database inside the dataset folder
class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " " + self.book.title