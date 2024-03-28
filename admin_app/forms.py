from django import forms
from library.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["isbn", "title", "image", "describe", "genre", "author", "publisher"]
        widgets = {
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "describe": forms.Textarea(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "publisher": forms.Select(attrs={"class": "form-control"}),
        }
