from django.db import models
from .genre import Genre
from .author import Author
from .publisher import Publisher
from .user import User


class Book(models.Model):
    isbn = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=5000)
    image = models.ImageField(upload_to="images", null=None, blank=None)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
