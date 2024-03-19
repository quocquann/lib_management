from rest_framework import serializers


class BookResponseSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField("get_id")
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.CharField(max_length=5000)
    describe = serializers.CharField(max_length=5000)

    def get_id(self, instance):
        return instance.pk



class BookRequestSerilizer(serializers.Serializer):
    isbn = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=5000)
    image = serializers.ImageField()
    # TODO: dosth
