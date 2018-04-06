from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import os

Game_Categories = (
    ('savas', 'SAVAS'),
    ('strateji', 'STRATEJI'),
    ('spor', 'SPOR'),
    ('bulmaca', 'BULMACA'),
    ('diger', 'DIGER'))



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, default="empty")
    category = models.CharField(max_length=6, choices=Game_Categories, default='bulmaca')


