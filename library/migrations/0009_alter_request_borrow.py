# Generated by Django 5.0.3 on 2024-03-25 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_request_reject_reason_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='borrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.borrow'),
        ),
    ]
