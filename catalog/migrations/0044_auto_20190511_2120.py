# Generated by Django 2.1.7 on 2019-05-11 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0043_check_competed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check',
            old_name='competed',
            new_name='completed',
        ),
    ]
