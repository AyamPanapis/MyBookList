from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)  # ISBN number as a unique identifier
    cover_url = models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return self.title