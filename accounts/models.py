from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name='سن')
    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name='تلفن همراه')
    addres = models.TextField(null=True, blank=True, verbose_name="آدرس")

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربران'
        