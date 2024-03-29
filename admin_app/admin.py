from django.contrib import admin
from library.models import Borrow, Book, Author, BookCopy, DetailBorrow, DetailRequest, Genre, Publisher, Punishment, Request, Review, User

# Register your models here.

admin.site.register(Author)
admin.site.register(DetailBorrow)
admin.site.register(DetailRequest)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Punishment)
admin.site.register(Request)
admin.site.register(Review)
admin.site.register(User)

class DetailBorrowInline(admin.TabularInline):
    model = DetailBorrow

class BookCopyInline(admin.TabularInline):
    model = BookCopy
    
@admin.register(Book)
class BookAdminModel(admin.ModelAdmin):
    list_display = ("pk","isbn", "title", "image", "author", "genre", "publisher", "total_borrow")
    inlines = [BookCopyInline]
    list_filter =("author", "genre", "publisher")
    search_fields = ("pk","isbn", "title", "author__name", "genre__name", "publisher__name")
    list_per_page=5
  
    def total_borrow(self, instance):
        copys = BookCopy.objects.filter(book=instance)
        return DetailBorrow.objects.filter(copy__in=copys).count()

@admin.register(BookCopy)
class BookCopyAdminModel(admin.ModelAdmin):
    list_display = ("status", "condition", "book")
    list_filter =("status",)

@admin.register(Borrow)
class BorrowAdminModel(admin.ModelAdmin):
    list_display = ("borrow_date","return_date", "status", "actual_return_date", "user")
    inlines = [DetailBorrowInline]
    list_filter=("status",)