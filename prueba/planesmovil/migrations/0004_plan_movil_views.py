# Generated by Django 3.1.2 on 2020-11-09 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planesmovil', '0003_auto_20201108_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_movil',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
