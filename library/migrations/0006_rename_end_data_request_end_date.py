# Generated by Django 5.0.3 on 2024-03-25 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_borrow_reject_reason_remove_detailborrow_note_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='end_data',
            new_name='end_date',
        ),
    ]
