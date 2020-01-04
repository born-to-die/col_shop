# Generated by Django 2.1 on 2019-06-01 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0065_auto_20190601_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='games',
        ),
        migrations.AddField(
            model_name='meet',
            name='games',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Game'),
        ),
    ]
