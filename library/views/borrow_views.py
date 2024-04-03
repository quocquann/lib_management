from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from ..serializers import BorrowResponseSerializer
from ..models import Borrow, BookCopy, DetailBorrow, Book
from ..utils.contants import BORROW_STATUS_BORROW


class ListBorrow(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(responses=BorrowResponseSerializer)
    def get(self, request):
        borrows = Borrow.objects.filter(user=request.user)
        for borrow in borrows:
            copy_ids = DetailBorrow.objects.filter(borrow=borrow).values_list(
                "copy", flat=True
            )
            book_ids = BookCopy.objects.filter(pk__in=copy_ids).values_list("book", flat=True)
            books = Book.objects.filter(pk__in=book_ids)
            borrow.books = books
            if ((borrow.return_date < date.today()) or (borrow.actual_return_date and borrow.actual_return_date > borrow.return_date)) and borrow.status==BORROW_STATUS_BORROW:
                borrow.overdue = True
            else:
                borrow.overdue= False
        serializer = BorrowResponseSerializer(borrows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
