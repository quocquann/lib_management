from rest_framework import serializers
from ..models import Borrow
from ..serializers import BookResponseSerializer


class BorrowResponseSerializer(serializers.ModelSerializer):

    books = serializers.ListField(child=BookResponseSerializer())
    overdue = serializers.BooleanField()

    class Meta:
        model = Borrow
        fields = ["id", "borrow_date", "return_date", "status", "books", "overdue", "actual_return_date"]
