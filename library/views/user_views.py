from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from ..serializers import UserResponseSerializer


class RetrieveUser(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(responses=UserResponseSerializer)
    def get(self, request):
        serializer = UserResponseSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
