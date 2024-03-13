from django.db import models


class Genre(models.Model):
    name = models.models.CharField(max_length=500)
