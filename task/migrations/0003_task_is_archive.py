# Generated by Django 3.0.7 on 2020-06-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20200607_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
    ]
