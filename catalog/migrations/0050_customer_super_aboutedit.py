# Generated by Django 2.2 on 2019-05-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0049_infosite'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='super_aboutedit',
            field=models.BooleanField(default=False),
        ),
    ]