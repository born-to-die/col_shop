# Generated by Django 2.1.7 on 2019-05-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0031_customer_super_edititems'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]