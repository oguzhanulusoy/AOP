# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20171128_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload_link',
            field=models.CharField(default=b'timezone.now', max_length=50),
        ),
    ]
