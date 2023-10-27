# Generated by Django 4.2.6 on 2023-10-27 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
        ('book', '0004_rename_name_book_title_book_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset.book'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
