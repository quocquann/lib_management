from rest_framework import serializers
from rest_framework.validators import ValidationError
import datetime
from ..models import Request, DetailRequest, Borrow


class DetailRequestSerializer(serializers.ModelSerializer):
    
    title = serializers.CharField(max_length=5000)
    image = serializers.CharField(max_length=5000)
    author = serializers.CharField(max_length=500)
    genre = serializers.CharField(max_length=500)
    
    class Meta:
        model = DetailRequest
    
