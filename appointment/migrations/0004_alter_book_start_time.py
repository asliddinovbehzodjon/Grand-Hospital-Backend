# Generated by Django 4.1.1 on 2022-09-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_remove_book_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(unique=True),
        ),
    ]
