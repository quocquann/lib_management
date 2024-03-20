from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from ..serializers import PublisherResponseSerializer
from ..models import Publisher

class ListCreatePublisher(APIView):
    
    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherResponseSerializer(publishers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)