from datetime import date
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from ..serializers import BorrowResponseSerializer
from ..models import Borrow, BookCopy, DetailBorrow, Book
from ..utils.contants import BORROW_STATUS_BORROW
from rest_framework.pagination import PageNumberPagination


class ListBorrow(ListAPIView):

    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    queryset = Borrow.objects.all()
    serializer_class=BorrowResponseSerializer
    

    @extend_schema(responses=BorrowResponseSerializer)
    def get(self, request):
        borrows = self.paginate_queryset(Borrow.objects.filter(user=request.user).order_by("-pk"))
        for borrow in borrows:
            copy_ids = DetailBorrow.objects.filter(borrow=borrow).values_list(
                "copy", flat=True
            )
            book_ids = BookCopy.objects.filter(pk__in=copy_ids).values_list("book", flat=True)
            books = Book.objects.filter(pk__in=book_ids)
            borrow.books = books
            if (borrow.return_date < date.today() and borrow.status==BORROW_STATUS_BORROW) or (borrow.actual_return_date and borrow.actual_return_date > borrow.return_date):
                borrow.overdue = True
            else:
                borrow.overdue= False
        serializer = BorrowResponseSerializer(borrows, many=True)
        self.pagination_class.page_size = 5
        return self.paginator.get_paginated_response(serializer.data)