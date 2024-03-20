from rest_framework import serializers
from ..models import Genre


class GenreResposneSerialize(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
    def get_id(self, instance):
        return instance.pk