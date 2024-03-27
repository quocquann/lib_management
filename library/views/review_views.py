from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..permissions import IsAuthenticatedOrReadOnlyForPost
from drf_spectacular.utils import extend_schema
from ..serializers import ReviewResponseSerializer, ReviewRequestSerializer
from ..models import Review, Book
from django.shortcuts import get_object_or_404

class ListCreateReviewByBook(APIView):

    permission_classes = [IsAuthenticatedOrReadOnlyForPost]

    @extend_schema(
        responses=ReviewResponseSerializer
    )
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = Review.objects.filter(book=book).order_by('-pk')
        serializer = ReviewResponseSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=ReviewRequestSerializer)
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = ReviewRequestSerializer(
            data=request.data, context={"user": request.user, "book": book}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
