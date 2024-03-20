from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from ..models import Genre
from ..serializers import GenreResposneSerialize

class ListCreateGenre(APIView):
    
    @extend_schema(
        responses=GenreResposneSerialize
    )
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreResposneSerialize(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        