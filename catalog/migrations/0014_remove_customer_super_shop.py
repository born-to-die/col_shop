# Generated by Django 2.1.7 on 2019-04-20 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_customer_super_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='super_shop',
        ),
    ]
