from rest_framework import serializers


class BookResponseSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField("get_id")
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.CharField(max_length=5000)
    describe = serializers.CharField(max_length=5000)
    author = serializers.CharField(max_length=500)
    genre = serializers.CharField(max_length=500)
    publisher = serializers.CharField(max_length=500)

    def get_id(self, instance):
        return instance.pk
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = instance.author.name
        data['genre'] = instance.genre.name
        data['publisher'] = instance.publisher.name
        return data



class BookRequestSerilizer(serializers.Serializer):
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.ImageField()
    # TODO: dosth
