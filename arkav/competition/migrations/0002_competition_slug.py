# Generated by Django 2.2.6 on 2019-10-24 07:44

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='slug',
            field=models.SlugField(default='undefined'),
            preserve_default=False,
        ),
    ]
