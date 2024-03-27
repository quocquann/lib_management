from django import forms
from library.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["isbn", "title", "image", "describe", "genre", "author", "publisher"]
        widgets = {"genre": forms.Select(attrs={"class": "form_control"})}
