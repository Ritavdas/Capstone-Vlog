# Generated by Django 3.0.4 on 2021-04-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210425_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='address',
            field=models.TextField(max_length=1000),
        ),
    ]