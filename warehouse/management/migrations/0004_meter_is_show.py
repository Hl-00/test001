# Generated by Django 3.2 on 2021-05-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20210507_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='is_show',
            field=models.CharField(default='flase', max_length=10),
        ),
    ]