from rest_framework import serializers
from ..models import Book


class BookResponseSerializer(serializers.ModelSerializer):
    # id = serializers.SerializerMethodField("get_id")
    # isbn = serializers.CharField(max_length=15)
    # title = serializers.CharField(max_length=5000)
    # image = serializers.ImageField()

    # def get_id(self, instance):
    #     return instance.pk

    class Meta:
        models = Book
        fields = "__all__"


class BookRequestSerilizer(serializers.Serializer):
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.ImageField()
    # TODO: dosth
