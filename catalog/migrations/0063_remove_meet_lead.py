# Generated by Django 2.2 on 2019-05-29 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0062_auto_20190530_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='lead',
        ),
    ]
