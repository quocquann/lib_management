from django.db import models
from .book_copy import BookCopy
from .borrow import Borrow


class DetailBorrow(models.Model):
    status = models.CharField(max_lenth=5000)

    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
