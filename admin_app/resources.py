from import_export import resources
from library.models import Book, DetailBorrow


class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class DetailBorrowResource(resources.ModelResource):
    class Meta:
        model = DetailBorrow