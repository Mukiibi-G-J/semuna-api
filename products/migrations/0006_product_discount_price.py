# Generated by Django 4.0.4 on 2022-05-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_regular_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(default=1, help_text='Price in USh 🇺🇬', verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
