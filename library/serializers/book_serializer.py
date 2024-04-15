from rest_framework import serializers
from ..models import Review, BookCopy
from django.db.models import Avg
from ..utils.contants import BOOK_COPY_STATUS_AVAILABLE


class BookResponseSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField("get_id")
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.CharField(max_length=5000)
    describe = serializers.CharField(max_length=5000)
    author = serializers.CharField(max_length=500)
    genre = serializers.CharField(max_length=500)
    publisher = serializers.CharField(max_length=500)
    rating = serializers.SerializerMethodField("get_rating")
    available = serializers.SerializerMethodField("get_available")

    def get_id(self, instance):
        return instance.pk
    
    def get_rating(self, instance):
        rating = Review.objects.filter(book=instance).aggregate(Avg("rating"))["rating__avg"]
        return rating
    
    def get_available(self, instance):
        available = BookCopy.objects.filter(book=instance, status=BOOK_COPY_STATUS_AVAILABLE).count()
        return available
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = instance.author.name
        data['genre'] = instance.genre.name
        data['publisher'] = instance.publisher.name
        return data



class BookRequestSerilizer(serializers.Serializer):
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.ImageField()
    # TODO: dosth
