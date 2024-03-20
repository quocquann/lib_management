from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema
from ..models import Genre
from ..serializers import GenreResposneSerialize


class ListGenre(ListAPIView):

    serializer_class = GenreResposneSerialize
    queryset = Genre.objects.all()

    @extend_schema(
        responses=GenreResposneSerialize
    )
    def get(self, request):
        return super().get(self, request)
