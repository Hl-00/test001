# Generated by Django 3.2 on 2021-05-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_meter_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_show',
            field=models.CharField(default='flase', max_length=10),
        ),
    ]
