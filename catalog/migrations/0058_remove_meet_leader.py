# Generated by Django 2.2 on 2019-05-28 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0057_meet_leader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='leader',
        ),
    ]
