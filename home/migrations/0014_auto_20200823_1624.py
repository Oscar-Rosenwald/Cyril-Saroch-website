# Generated by Django 3.1 on 2020-08-23 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200823_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
