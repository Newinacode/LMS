# Generated by Django 5.0.1 on 2024-01-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_bookdetail_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
