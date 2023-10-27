from django.db import models
from django.db.models import Avg
from dataset.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField()
    pub_date = models.DateTimeField('date published')
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)  # Changed to CASCADE for integrity
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f'{self.user_name} - {self.book.title}'  # Helpful for the admin interface