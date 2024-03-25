from django.db import models
from . import Book, Request

class DetailRequest(models.Model):
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name="detail_requests")
    
    
    