from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=1000)
    description = models.TextField()
    categories = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=1000)