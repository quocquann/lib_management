from django.db import models
from .user import User
from ..utils.contants import BORROW_STATUS, DEFAUL_BORROW_STATUS


class Borrow(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=500, choices=BORROW_STATUS, default=DEFAUL_BORROW_STATUS)
    actual_return_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)