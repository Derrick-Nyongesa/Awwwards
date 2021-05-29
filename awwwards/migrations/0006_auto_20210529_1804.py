# Generated by Django 3.2.2 on 2021-05-29 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0005_rename_creativity_rating_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]