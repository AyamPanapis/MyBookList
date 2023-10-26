from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)  
    author = models.JSONField()
    published_date = models.CharField(max_length=20)
    isbn_number = models.CharField(max_length=20, unique=True) 
    page_count = models.IntegerField(null=True, blank=True)
    cover_image = models.URLField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=20)  
    preview_link = models.URLField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
