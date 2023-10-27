# Generated by Django 4.2.6 on 2023-10-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
        ('book', '0008_alter_wishlist_book_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dataset.book'),
            preserve_default=False,
        ),
    ]
