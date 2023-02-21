from django.db import models
from django.db.models.functions import Lower


class Users(models.Model):
    name = models.CharField(max_length=30, verbose_name="name", null=False)
    surname = models.CharField(max_length=30, verbose_name="surname", null=False)
    age = models.IntegerField(verbose_name="age", null=False)
    sex = models.CharField(max_length=1, null=False, default="")
    phone = models.IntegerField(verbose_name="Phone number")
    hobbies = models.ManyToManyField('Hobbies', verbose_name="list of hobbies")
    msg = models.CharField(max_length=100, verbose_name="MSG", null=False)
    favorite_place_name = models.ForeignKey('Cafe', on_delete=models.CASCADE, default='')
    work = models.ForeignKey('Work', on_delete=models.CASCADE, null=True,default='')

    def __str__(self):
        return self.name

    class Meta:

        indexes = [
            models.Index(fields=['sex'], name='sex_idx')
        ]


class Hobbies(models.Model):
    name = models.CharField(max_length=30)


class Cafe(models.Model):
    name = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    average_amount = models.IntegerField()


class Work(models.Model):
    name = models.CharField(max_length=40)
    pilot_salary = models.IntegerField(null = True)

    def __str__(self):
        return self.name

    # class Meta:
    #     abstract = True
    #     indexes = [
    #         models.Index(filds=['pilot_salary'], name='pilot_salary_idx')
    #     ]
