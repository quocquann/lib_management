from django.db import models
from .book import Book
from ..utils.contants import BOOK_COPY_STATUS


class BookCopy(models.Model):
    status = models.CharField(choices=BOOK_COPY_STATUS, default=0, max_length=5000)
    condition = models.CharField(max_length=5000, null=True, blank=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return "(" + str(self.pk) +")"+ self.book.title
