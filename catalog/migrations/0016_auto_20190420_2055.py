# Generated by Django 2.1.7 on 2019-04-20 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_customer_super_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='city',
        ),
        migrations.AddField(
            model_name='shops',
            name='city',
            field=models.OneToOneField(default=None, help_text='Select a your city', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.City'),
            preserve_default=False,
        ),
    ]
