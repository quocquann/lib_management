from rest_framework import serializers
from rest_framework.validators import ValidationError
import datetime
from ..models import Review
from ..serializers import BookResponseSerializer

class ReviewResponseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment_text', 'user']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data