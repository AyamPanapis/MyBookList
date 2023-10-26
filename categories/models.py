from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField()
    image_link = models.URLField()
    category = models.CharField(max_length=200)
