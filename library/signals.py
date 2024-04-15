from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Borrow, DetailBorrow, BookCopy, Request
from .utils.contants import BOOK_COPY_STATUS_BORROWED, BORROW_STATUS_BORROW
from django.core.mail import send_mail
from lib_management.settings import EMAIL_HOST_USER

@receiver(post_save, sender=Borrow)
def set_book_copy_to_borrow_status(sender, instance, **kwarg):
    if instance.status == BORROW_STATUS_BORROW:
        copy_ids = DetailBorrow.objects.filter(borrow=instance).values_list("copy", flat=True)
        copies = BookCopy.objects.filter(pk__in=copy_ids)
        for copy in copies:
            copy.status = BOOK_COPY_STATUS_BORROWED
            copy.save()
            

@receiver(post_save, sender=Request)
def send_email_to_user(sender, instance, **kwarg):
    from_email = EMAIL_HOST_USER
    
    if instance.status == 'approved':
        subject = "Chấp nhận yêu cầu mượn sách"
        msg = "Thư viện xin thông báo yêu cầu mượn sách(Mã phiếu: " + str(instance.pk) + ") từ ngày " + str(instance.start_date) + " đã được chấp nhận."
        send_mail(
            subject,
            msg,
            from_email,
            [instance.user.email],
            fail_silently=False,
        )
    elif instance.status == 'rejected':
        subject = "Từ chối yêu cầu mượn sách"
        msg = "Thư viện xin thông báo yêu cầu mượn sách(Mã phiếu: " + str(instance.pk) + ") từ ngày " + str(instance.start_date) + " đã bị từ chối với lý do:\n " + str(instance.reject_reason)
        send_mail(
            subject,
            msg,
            from_email,
            [instance.user.email],
            fail_silently=False,
        )
        
@receiver(post_save, sender=Request)
def renew_borrow(sender, instance, **kwarg):
    if instance.type == "renew":
        borrow = instance.borrow
        borrow.return_date = instance.end_date
        borrow.save()