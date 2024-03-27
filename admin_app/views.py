from django.shortcuts import render
from library.models import Book
from django.views.generic import ListView

# Create your views here.


def index(request):
    return render(request, "admin_app/index.html")


class ListBook(ListView):
    model = Book
    queryset = Book.objects.all().prefetch_related()
    context_object_name="book_list"
    template_name="admin_app/book_list.html"