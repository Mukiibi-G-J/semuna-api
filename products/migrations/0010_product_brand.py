# Generated by Django 4.0.4 on 2022-06-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_imagelogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='brand name', max_length=255),
        ),
    ]