from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from ..serializers import ReviewResponseSerializer
from ..models import Review

class ListCreateReviewByBook(APIView):
    
    @extend_schema(
        responses=ReviewResponseSerializer
    )
    def get(self, request, pk):
        reviews = Review.objects.filter(book__pk=pk)
        serializer = ReviewResponseSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
