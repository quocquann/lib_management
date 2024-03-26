from rest_framework import serializers
from ..models import Review

class ReviewResponseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment_text', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data


class ReviewRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["rating", "comment_text"]

    def create(self, validated_data):
        validated_data["user"] = self.context.get("user")
        validated_data["book"] = self.context.get("book")
        review = Review.objects.create(**validated_data)
        return review
