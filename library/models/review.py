from django.db import models
from .book import Book
from .user import User


class Review(models.Model):
    rating = models.IntegerField()
    comment_text = models.CharField(max_length=5000)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "(" + str(self.pk) +")" + "Review" + " - " + str(self.book)