from django.db import models
from django.contrib.auth.models import User
from dataset.models import Book
# Create your models here.
class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    

