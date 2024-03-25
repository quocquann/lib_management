from django.db import models
from .book_copy import BookCopy
from .borrow import Borrow


class DetailBorrow(models.Model):
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
