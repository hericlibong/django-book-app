# Generated by Django 4.2.7 on 2023-12-05 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_practice', '0009_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]