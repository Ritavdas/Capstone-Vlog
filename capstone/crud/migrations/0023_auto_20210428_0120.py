# Generated by Django 3.0.4 on 2021-04-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0022_auto_20210426_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donors',
            old_name='bike',
            new_name='bruise',
        ),
        migrations.RenameField(
            model_name='donors',
            old_name='age',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='donors',
            old_name='boat',
            new_name='fainting',
        ),
        migrations.RenameField(
            model_name='donors',
            old_name='car',
            new_name='none',
        ),
        migrations.RenameField(
            model_name='donors',
            old_name='amount',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='donors',
            name='vein',
            field=models.BooleanField(default=False),
        ),
    ]
