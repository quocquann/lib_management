from django.shortcuts import render
from django.urls import reverse_lazy
from library.models import Book, Request, Borrow, User
from django.views.generic import ListView, CreateView, UpdateView
from .forms import BookForm

# Create your views here.


def index(request):
    return render(request, "admin_app/index.html")


class ListBook(ListView):
    model = Book
    queryset = Book.objects.all().prefetch_related().order_by("-pk")
    paginate_by = 10
    context_object_name="book_list"
    template_name="admin_app/book_list.html"


class CreateBook(CreateView):
    model = Book
    template_name = "admin_app/book_form.html"
    form_class = BookForm
    success_url=reverse_lazy("books")
    
class UpdateBook(UpdateView):
    model = Book
    template_name = "admin_app/book_form.html"
    form_class = BookForm
    success_url=reverse_lazy("books")

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
    
    
class CreateBorrow(CreateView):
    model = Borrow
    template_name="admin_app/borrow_form.html"
    # TODO: Form or field 
    success_url=reverse_lazy("borrows")
    
class ListUser(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name="user_list"
    template_name="admin_app/user_list.html"
