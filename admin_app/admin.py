from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
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

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Punishment)
admin.site.register(User)
admin.site.register(DetailRequest)


class DetailBorrowInline(admin.TabularInline):
    model = DetailBorrow


class BookCopyInline(admin.TabularInline):
    model = BookCopy


class DetailRequestInline(admin.TabularInline):
    model = DetailRequest


class PunishmentInline(admin.TabularInline):
    model = Punishment


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
    list_filter = ("author", "genre", "publisher")
    search_fields = (
        "pk",
        "isbn",
        "title",
        "author__name",
        "genre__name",
        "publisher__name",
    )
    list_per_page = 5
    resource_classes = [BookResource]

    def total_borrow(self, instance):
        copys = BookCopy.objects.filter(book=instance)
        return DetailBorrow.objects.filter(copy__in=copys).count()


@admin.register(BookCopy)
class BookCopyAdminModel(admin.ModelAdmin):
    list_display = ("status", "condition", "book")
    list_filter = ("status",)


@admin.register(Borrow)
class BorrowAdminModel(admin.ModelAdmin):
    list_display = (
        "borrow_date",
        "return_date",
        "status",
        "actual_return_date",
        "user",
        "overdue",
    )
    inlines = [DetailBorrowInline, PunishmentInline]
    list_filter = (
        "status",
        ("borrow_date", DateRangeFilterBuilder("Borrow date:")),
        ("return_date", DateRangeFilterBuilder("Return date:")),
    )

    def overdue(self, instance):
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
class DetailBorrowAdminModel(admin.ModelAdmin):
    list_display = ("copy", "borrow")
    list_filter = ("borrow",)


@admin.register(Request)
class RequestAdminModel(admin.ModelAdmin):
    inlines = [DetailRequestInline]


@admin.register(Review)
class ReviewAdminModel(admin.ModelAdmin):
    list_display=("book", "user", "rating", "comment_text")