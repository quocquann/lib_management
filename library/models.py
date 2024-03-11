from django.db import models

# Create your models here.

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    student_no = models.CharField(max_length=500, unique=True)
    role = models.CharField(max_length=500)


class Borrow(models.Model):
    borrow_id = models.IntegerField(primary_key=True)
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=500)
    actual_return_date = models.DateField(null=True)
    user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=5000)


class Punishment(models.Model):
    punish_id = models.IntegerField(primary_key=True)
    reason = models.CharField(max_length=5000)
    fine = models.IntegerField()
    borrow_id = models.IntegerField()
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)


class Book(models.Model):
    isbn = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)
    book_id = models.IntegerField(primary_key=True)
    genre_id = models.IntegerField()
    author_id = models.IntegerField()
    publisher_id = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class BookCopy(models.Model):
    copy_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=500)
    book_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    comment_text = models.CharField(max_length=5000)
    book_id = models.IntegerField()
    user_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DetailBorrow(models.Model):
    id = models.IntegerField(primary_key=True)
    copy_id = models.IntegerField()
    borrow_id = models.IntegerField()
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
