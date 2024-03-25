from django.db import models
from . import User, Borrow

class Request(models.Model):
    status = models.CharField(max_length=100, default='pending')
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=100)
    reject_reason = models.TextField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE, null=True)
    
    
    