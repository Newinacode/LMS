# Generated by Django 5.0.1 on 2024-01-31 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='books.genre'),
        ),
        migrations.AlterField(
            model_name='bookdetail',
            name='book_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.book'),
        ),
    ]