from rest_framework import serializers
from rest_framework.validators import ValidationError
import datetime
from ..models import Request, DetailRequest, Book, BookCopy
from ..serializers import BookResponseSerializer

class RequestSerializer(serializers.Serializer):
    book_ids = serializers.ListField(child=serializers.IntegerField())
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    type = serializers.CharField()
    borrow_id = serializers.IntegerField()
    
    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise ValidationError("Invalid date - start date in past")
        return value
    
    def validate_end_date(self, value):
        if value < datetime.date.today():
            raise ValidationError("Invalid date - end date in past")
        return value
    
    def validate_book_ids(self, value):
        for id in value:
            book = Book.objects.get(pk=id)
            available = BookCopy.objects.filter(book=book).count()
            if available <= 0:
                raise ValidationError("Invalid book - book is not available")
               
    def create(self, validated_data):
        book_ids = validated_data.pop('book_ids', [])
        user = self.context.get('user')
        
        request = Request.objects.create(**validated_data, user=user)  

        for book_id in book_ids:
            book = Book.objects.get(id=book_id)
            DetailRequest.objects.create(book=book, request=request)
        
        request.book_ids = book_ids
        return request

class RequestResponseSerializer(serializers.ModelSerializer):
    
    books = serializers.ListField(child=BookResponseSerializer())
    
    class Meta:
        model = Request
        fields = ['id', 'start_date', 'end_date', 'status', 'type', 'reject_reason', 'books', 'borrow']