import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib_management.settings")

django.setup()

from library.models import Book, DetailBorrow, Borrow, User, BookCopy

def choiceCopy():
    copys = BookCopy.objects.all()
    choice_copys = random.choices(copys, k=2)
    while choice_copys[0].book.title == choice_copys[1].book.title:
        choice_copys = random.choices(copys, k=2)
    return choice_copys
    
def addData():
    user = User.objects.get(pk=1)
    for i in range(5000):
        borrow = Borrow.objects.create(borrow_date="2024-04-08", return_date="2024-04-12",actual_return_date="2024-04-12", status="returned", user=user)
        choice_books = choiceCopy()
        DetailBorrow.objects.create(copy=choice_books[0], borrow=borrow)
        DetailBorrow.objects.create(copy=choice_books[1], borrow=borrow)


if __name__ == '__main__':
    addData()
    