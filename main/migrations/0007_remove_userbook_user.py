# Generated by Django 4.2.6 on 2023-10-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userbook_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='user',
        ),
    ]