# Generated by Django 2.1.3 on 2018-11-07 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='thread',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
