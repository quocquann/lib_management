from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..serializers import RequestSerializer, RequestResponseSerializer
from ..models import Request, DetailRequest, Book
from django.shortcuts import get_object_or_404
from ..permissions import CanDeleteRequest
from rest_framework.pagination import PageNumberPagination

class ListCreateRequest(APIView):
    
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        request=RequestSerializer
    )
    def post(self, request):    
        serializer = RequestSerializer(data=request.data, context={
            'user': request.user
        }, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses=RequestResponseSerializer,
        parameters=[
            OpenApiParameter(name='page', type=int, required=False)
        ]
    )
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        requests =  paginator.paginate_queryset(Request.objects.filter(user=request.user).order_by("-pk"), request)
        for req in requests:
            book_ids = DetailRequest.objects.filter(request=req).values_list('book', flat=True)
            books = Book.objects.filter(pk__in=book_ids)
            req.books = books
        serializer = RequestResponseSerializer(requests, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    
class DeleteRequest(APIView):
    
    permission_classes = [IsAuthenticated, CanDeleteRequest]
    
    @extend_schema(
        responses=RequestResponseSerializer
    )
    def delete(self, request, pk):
        request = get_object_or_404(Request, pk=pk)
        if request.status == 'pending':
            id = request.pk
            request.delete()
            return Response({"id" : id}, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "can not delete this request"
            }, status=status.HTTP_400_BAD_REQUEST)
            
