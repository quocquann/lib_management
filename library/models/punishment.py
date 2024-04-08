from django.db import models
from .borrow import Borrow


class Punishment(models.Model):
    reason = models.CharField(max_length=5000)
    fine = models.IntegerField()
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.borrow)
