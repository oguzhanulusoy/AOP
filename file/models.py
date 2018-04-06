from django.db import models
from django.contrib.auth.models import User


# Create your models here.

Game_Categories = (
    ('savas', 'SAVAS'),
    ('strateji', 'STRATEJI'),
    ('spor', 'SPOR'),
    ('bulmaca', 'BULMACA'),
    ('diger', 'DIGER'))


class Post(models.Model):
    #creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=6, choices=Game_Categories, default='bulmaca')
    description = models.TextField()
    file = models.FileField(upload_to='files/', default="default")




