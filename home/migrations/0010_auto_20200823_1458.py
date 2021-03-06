# Generated by Django 3.1 on 2020-08-23 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200823_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 14, 58, 5, 106144)),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 14, 58, 5, 106511)),
        ),
    ]
