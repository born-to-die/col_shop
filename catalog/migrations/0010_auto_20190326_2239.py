# Generated by Django 2.1.7 on 2019-03-26 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_customer_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Game'),
            preserve_default=False,
        ),
    ]
