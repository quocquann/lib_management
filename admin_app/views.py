from django.shortcuts import render
from library.models import Book, Request, Borrow
from django.views.generic import ListView, CreateView
from .forms import BookForm

# Create your views here.


def index(request):
    return render(request, "admin_app/index.html")


class ListBook(ListView):
    model = Book
    queryset = Book.objects.all().prefetch_related()
    context_object_name="book_list"
    template_name="admin_app/book_list.html"


class CreateBook(CreateView):
    model = Book
    template_name = "admin_app/book_form.html"
    form_class = BookForm


class ListRequest(ListView):
    model = Request
    queryset = Request.objects.all().prefetch_related()
    context_object_name = "request_list"
    template_name = "admin_app/request_list.html"


class ListBorrow(ListView):
    model = Borrow
    queryset = Borrow.objects.all().prefetch_related()
    context_object_name = "borrow_list"
    template_name = "admin_app/borrow_list.html"
