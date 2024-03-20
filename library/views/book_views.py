from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..models import Book
from ..serializers import BookResponseSerializer


class ListBook(ListAPIView):

    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["author", "genre", "publisher"]
    search_fields = ["title", "author__name", "genre__name", "publisher__name"]

    @extend_schema(
        responses=BookResponseSerializer,
        parameters=[
            OpenApiParameter(name="author", type=str, required=False),
            OpenApiParameter(name="genre", type=str, required=False),
            OpenApiParameter(name="publisher", type=str, required=False),
        ],
    )
    def get(self, request):
        return super().get(self, request)


class RetrieveBook(RetrieveAPIView):

    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()

    @extend_schema(
        responses=BookResponseSerializer
    )
    def get(self, request, pk):
        return super().get(self, request, pk)
