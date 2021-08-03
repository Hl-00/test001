# Generated by Django 3.2 on 2021-05-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_numbering', models.CharField(max_length=32)),
                ('stop_numbering', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=100)),
                ('factory', models.CharField(max_length=32)),
                ('date', models.DateTimeField(auto_now=True)),
                ('years', models.CharField(max_length=32)),
                ('cycle', models.CharField(max_length=32)),
                ('appraiser', models.CharField(max_length=32)),
                ('appraisal_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
