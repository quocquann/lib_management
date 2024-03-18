from rest_framework import generics
from .models import Book

# Create your views here.

class ListCreateBook(generics.ListCreateAPIView):
    def get(self):
        books = Book.objects.all()