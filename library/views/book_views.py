from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..models import Book, BookCopy, DetailBorrow
from ..serializers import BookResponseSerializer, MostBorrowBookSerializer
from django.db.models import Count


class ListBook(ListAPIView):

    serializer_class = BookResponseSerializer
    pagination_class = PageNumberPagination
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["author", "genre", "publisher"]
    search_fields = ["title", "author__name", "genre__name", "publisher__name"]
    ordering_fields = ["pk", "title"]

    @extend_schema(
        responses=BookResponseSerializer,
        parameters=[
            OpenApiParameter(name="author", type=str, required=False),
            OpenApiParameter(name="genre", type=str, required=False),
            OpenApiParameter(name="publisher", type=str, required=False),
        ],
    )
    def get(self, request):
        self.paginator.page_size = 20
        return super().get(self, request)


class RetrieveBook(RetrieveAPIView):

    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()

    @extend_schema(
        responses=BookResponseSerializer
    )
    def get(self, request, pk):
        return super().get(self, request, pk)
    
class ListMostBorrowBook(ListAPIView):
    
    serializer_class = [BookResponseSerializer]
    queryset = Book.objects.all()
    
    @extend_schema(
        responses=BookResponseSerializer
    )
    def get(self, request):
        mostBorrowBookIds = DetailBorrow.objects.values("copy__book").annotate(count=Count("copy__book")).order_by("-count")[:5]
        books = []
        for b in mostBorrowBookIds:
            book = Book.objects.get(pk=b['copy__book'])
            book.borrowCount = b['count']
            books.append(book)
        serializer = MostBorrowBookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ListRelateBook(APIView):
    
    @extend_schema(
        responses=BookResponseSerializer
    )
    def get(self, request, pk):
        get_object_or_404(Book, pk=pk)
        rules = cache.get("association_rules")
        if rules is None:
            return Response({
                "message": "cannot get relate book"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        relate = list(rules[rules["antecedents"].apply(lambda x: pk in x)]["consequents"].apply(lambda x: list(x)))
        copy_ids = [item for sublist in relate for item in sublist]
        book_ids = BookCopy.objects.filter(pk__in=copy_ids).values_list("book", flat=True)
        books = Book.objects.filter(pk__in=book_ids)[:5]
        serializer = BookResponseSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)