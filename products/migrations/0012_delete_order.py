# Generated by Django 4.0.5 on 2022-07-07 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
