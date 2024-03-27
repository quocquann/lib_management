from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.ListBook.as_view(), name="books"),
    path("books/create", views.CreateBook.as_view(), name="create-book"),
    path("requests", views.ListRequest.as_view(), name="requests"),
    path("borrows", views.ListBorrow.as_view(), name="borrows"),
]
