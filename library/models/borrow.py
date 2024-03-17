from django.db import models
from .user import User


class Borrow(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=500)
    actual_return_date = models.DateField(null=True)
    reject_reason = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
