from django.db import models
from django.db.models.functions import Lower


class Hobbies(models.Model):
    name = models.CharField(max_length=30)


class Users(models.Model):
    name = models.CharField(max_length=30, verbose_name="name")
    surname = models.CharField(max_length=30, verbose_name="surname")
    age = models.IntegerField(verbose_name="age")
    adress = models.CharField(max_length=100, verbose_name="adress", default="")
    hobbies = models.ManyToManyField(Hobbies)


class UserRatings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, verbose_name="description")
    rating = models.IntegerField(verbose_name="rating")
