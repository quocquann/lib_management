from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
from library.models import (
    Borrow,
    Book,
    Author,
    BookCopy,
    DetailBorrow,
    DetailRequest,
    Genre,
    Publisher,
    Punishment,
    Request,
    Review,
    User,
)
from rangefilter.filters import (
    DateRangeFilterBuilder,
)
from datetime import date
from library.utils.contants import BORROW_STATUS_BORROW
from .resources import BookResource
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header="Library management"
admin.site.site_title="Library management"
admin.site.index_title="Admin"

admin.site.unregister(Group)

class AuthorFilter(AutocompleteFilter):
    title='Author'
    field_name="author"

class GenreFilter(AutocompleteFilter):
    title='Genre'
    field_name="genre"
    
class PublisherFilter(AutocompleteFilter):
    title='Publisher'
    field_name="publisher"

class DetailBorrowInline(admin.TabularInline):
    model = DetailBorrow
    autocomplete_fields=["copy"]


class BookCopyInline(admin.TabularInline):
    model = BookCopy
    autocomplete_fields=['book']


class DetailRequestInline(admin.TabularInline):
    model = DetailRequest


class PunishmentInline(admin.TabularInline):
    model = Punishment

@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ("pk","username", "email", "is_staff")
    search_fields=("pk", "username", "email")

@admin.register(Author)
class AuthorAdminModel(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields=["name"]

@admin.register(Genre)
class GenreAdminModel(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields=["name"]
    
@admin.register(Publisher)
class PublisherAdminModel(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields=["name"]
    
    
@admin.register(Book)
class BookAdminModel(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "pk",
        "isbn",
        "title",
        "image",
        "author",
        "genre",
        "publisher",
        "price",
        "total_borrow",
    )
    inlines = [BookCopyInline]
    list_filter = (AuthorFilter, GenreFilter, PublisherFilter)
    search_fields = (
        "pk",
        "isbn",
        "title",
        "author__name",
        "genre__name",
        "publisher__name",
    )
    autocomplete_fields=('author', 'genre', 'publisher')
    list_per_page = 5
    resource_classes = [BookResource]

    def total_borrow(self, instance):
        copys = BookCopy.objects.filter(book=instance)
        return DetailBorrow.objects.filter(copy__in=copys).count()


@admin.register(BookCopy)
class BookCopyAdminModel(admin.ModelAdmin):
    list_display = ("pk", "status", "condition", "book")
    list_filter = ("status",)
    search_fields=('book__title','pk')
    autocomplete_fields=("book",)


@admin.register(Borrow)
class BorrowAdminModel(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        "borrow_date",
        "return_date",
        "status",
        "actual_return_date",
        "user",
        "is_overdue",
    )
    inlines = [DetailBorrowInline, PunishmentInline]
    list_filter = (
        "status",
        ("borrow_date", DateRangeFilterBuilder("Borrow date:")),
        ("return_date", DateRangeFilterBuilder("Return date:")),
    )
    autocomplete_fields=("user",)
    search_fields=("pk",)

    def is_overdue(self, instance):
        if (
            (instance.return_date < date.today())
            or (
                instance.actual_return_date
                and instance.actual_return_date > instance.return_date
            )
        ) and instance.status == BORROW_STATUS_BORROW:
            return True
        else:
            return False


@admin.register(DetailBorrow)
class DetailBorrowAdminModel(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("pk", "copy", "borrow")
    list_filter = ("borrow",)
    autocomplete_fields=("copy","borrow")


@admin.register(Request)
class RequestAdminModel(admin.ModelAdmin):
    list_display = ("pk", "status", "start_date", "end_date", "type", "reject_reason", "user", "borrow")
    inlines = [DetailRequestInline]
    search_fields=("pk",)
    autocomplete_fields=("user", "borrow")
    

@admin.register(DetailRequest)
class DetailRequestAdminModel(admin.ModelAdmin):
    list_display = ("pk", "book", "request")
    autocomplete_fields=("book", "request")

@admin.register(Review)
class ReviewAdminModel(admin.ModelAdmin):
    list_display=("pk", "book", "user", "rating", "comment_text")
    autocomplete_fields=("user", "book")
    
@admin.register(Punishment)
class PunishmentAdminModel(admin.ModelAdmin):
    list_display = ("pk", "reason", "fine", "borrow")
    autocomplete_fields=("borrow",)