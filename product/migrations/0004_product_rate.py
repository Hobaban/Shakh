# Generated by Django 3.2.4 on 2021-10-28 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210918_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
