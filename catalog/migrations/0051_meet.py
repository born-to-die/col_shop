# Generated by Django 2.2 on 2019-05-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0050_customer_super_aboutedit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=300)),
                ('summary', models.CharField(max_length=1000)),
            ],
        ),
    ]