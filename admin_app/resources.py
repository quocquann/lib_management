from import_export import resources
from library.models import Book


class BookResource(resources.ModelResource):

    class Meta:
        model = Book
