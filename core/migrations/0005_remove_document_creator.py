# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_document_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='creator',
        ),
    ]
