from django.db import models
from . import User, Borrow
from ..utils.contants import REQUEST_STATUS, DEFAULT_REQUEST_STATUS, REQUEST_TYPE, DEFAULT_REQUEST_TYPE

class Request(models.Model):
    status = models.CharField(max_length=100, choices=REQUEST_STATUS, default=DEFAULT_REQUEST_STATUS)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=100, choices=REQUEST_TYPE, default=DEFAULT_REQUEST_TYPE)
    reject_reason = models.TextField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.pk)