from django.db import models
from .book import Book
from ..utils.contants import BOOK_COPY_STATUS


class BookCopy(models.Model):
    status = models.CharField(choices=BOOK_COPY_STATUS, default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
