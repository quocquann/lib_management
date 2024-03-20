from rest_framework import serializers
from ..models import Publisher


class PublisherResponseSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    
    class Meta:
        model = Publisher
        fields = ['id', 'name']
        
    def get_id(self, instance):
        return instance.pk