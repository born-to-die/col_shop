# Generated by Django 2.1.7 on 2019-05-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0039_check_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='counts',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
    ]
