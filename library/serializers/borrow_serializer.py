from rest_framework import serializers
from ..models import Borrow
from ..serializers import BookResponseSerializer


class BorrowResponseSerializer(serializers.ModelSerializer):

    books = serializers.ListField(child=BookResponseSerializer())

    class Meta:
        model = Borrow
        fields = ["id", "borrow_date", "return_date", "status", "books"]
