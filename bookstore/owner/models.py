from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=10)
    copies=models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.book_name