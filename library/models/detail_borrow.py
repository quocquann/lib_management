from django.db import models
from .book_copy import BookCopy
from .borrow import Borrow


class DetailBorrow(models.Model):
    note = models.CharField(max_length=5000)

    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
