# Generated by Django 4.2.7 on 2023-12-03 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_practice', '0004_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(default=2023, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
