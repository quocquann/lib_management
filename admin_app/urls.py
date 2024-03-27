from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("books", views.ListBook.as_view(), name="books")
]