from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Borrow, DetailBorrow, BookCopy
from .utils.contants import BOOK_COPY_STATUS_BORROWED, BORROW_STATUS_BORROW

@receiver(post_save, sender=Borrow)
def set_book_copy_to_borrow_status(sender, instance, **kwarg):
    if instance.status == BORROW_STATUS_BORROW:
        copy_ids = DetailBorrow.objects.filter(borrow=instance).values_list("copy", flat=True)
        copies = BookCopy.objects.filter(pk__in=copy_ids)
        for copy in copies:
            copy.status = BOOK_COPY_STATUS_BORROWED
            copy.save()