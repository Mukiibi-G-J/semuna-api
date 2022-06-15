# Generated by Django 4.0.4 on 2022-05-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_discount_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='regular_price',
            field=models.IntegerField(default=1, help_text='Price in USh 🇺🇬', verbose_name='Regular Price'),
            preserve_default=False,
        ),
    ]
