# Generated by Django 2.1.7 on 2019-05-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_game_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(max_length=200)),
                ('date_create', models.DateField(auto_now_add=True, null=True)),
                ('games', models.ManyToManyField(help_text='Зажмите Ctrl для выбора нескольких', to='catalog.Game')),
            ],
        ),
    ]
