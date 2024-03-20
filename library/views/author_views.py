from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema
from ..models import Author
from ..serializers import AuthorResponseSerializer


class ListAuthor(ListAPIView):

    serializer_class = AuthorResponseSerializer
    queryset = Author.objects.all()

    @extend_schema(
        responses=AuthorResponseSerializer
    )
    def get(self, request):
        return super().get(self, request)
