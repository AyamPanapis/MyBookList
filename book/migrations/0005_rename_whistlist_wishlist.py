# Generated by Django 4.2.6 on 2023-10-27 16:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_remove_review_book_list_remove_review_user_whistlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WhistList',
            new_name='WishList',
        ),
    ]
