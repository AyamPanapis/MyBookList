# Generated by Django 4.2.6 on 2023-12-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]