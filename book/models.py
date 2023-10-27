from django.db import models
from django.db.models import Avg
from dataset.models import Book
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    comment = models.TextField()
    pub_date = models.DateTimeField('date published')
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)


    def __str__(self):
        return f'{self.user_name} - {self.book.title}'
    
class WishList(models.Model):
    book = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_list = models.IntegerField()
