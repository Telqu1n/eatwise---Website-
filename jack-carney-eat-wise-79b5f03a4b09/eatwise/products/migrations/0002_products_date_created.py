# Generated by Django 5.1.2 on 2025-02-26 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
