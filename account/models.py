from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(models.Model):
    django_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.django_user.last_name + ", " + self.django_user.first_name

