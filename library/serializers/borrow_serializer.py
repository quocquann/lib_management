from rest_framework import serializers
from ..models import Borrow, DetailBorrow, Book, BookCopy
from ..serializers import BookResponseSerializer
from ..utils.contants import BORROW_STATUS_BORROW
from datetime import date


class BorrowResponseSerializer(serializers.ModelSerializer):

    books = serializers.ListField(child=BookResponseSerializer())
    overdue = serializers.BooleanField()

    class Meta:
        model = Borrow
        fields = ["id", "borrow_date", "return_date", "status", "books", "overdue", "actual_return_date"]

