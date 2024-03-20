from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema
from ..serializers import PublisherResponseSerializer
from ..models import Publisher


class ListPublisher(ListAPIView):

    serializer_class = PublisherResponseSerializer
    queryset = Publisher.objects.all()

    @extend_schema(responses=PublisherResponseSerializer)
    def get(self, request):
        return super().get(self, request)
