# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_post_upload_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_link',
            field=models.FileField(upload_to=b'documents/'),
        ),
    ]