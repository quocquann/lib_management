from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema
from ..models import Book
from ..serializers import BookResponseSerializer, BookRequestSerilizer


class ListCreateBook(APIView, PageNumberPagination):

    @extend_schema(responses=BookResponseSerializer)
    def get(self, request):
        books = Book.objects.all()
        result = self.paginate_queryset(books, request)
        serializer = BookResponseSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookRequestSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveBook(RetrieveAPIView):
    
    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()
    
    @extend_schema(
        responses=BookResponseSerializer
    )
    def get(self, request, pk):
        return super().get(self, request, pk)