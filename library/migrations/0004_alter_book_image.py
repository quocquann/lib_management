# Generated by Django 5.0.3 on 2024-03-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_author_name_alter_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=None, max_length=5000, null=None, upload_to='images'),
        ),
    ]
