from django.db import models
from django.db.models.functions import Lower


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")