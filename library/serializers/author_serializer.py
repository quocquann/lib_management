from rest_framework import serializers
from ..models import Author


class AuthorResponseSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    
    class Meta:
        model = Author
        fields=['id', 'name']
        
    def get_id(self, instance):
        return instance.pk