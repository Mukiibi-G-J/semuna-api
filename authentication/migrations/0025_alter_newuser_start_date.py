# Generated by Django 4.0.5 on 2022-07-07 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 7, 18, 43, 17, 970424, tzinfo=utc)),
        ),
    ]
