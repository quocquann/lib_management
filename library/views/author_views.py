from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from ..models import Author
from ..serializers import AuthorResponseSerializer

class ListCreateAuthor(APIView):
    
    @extend_schema(
        responses=AuthorResponseSerializer
    )
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorResponseSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)