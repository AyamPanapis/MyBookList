from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)