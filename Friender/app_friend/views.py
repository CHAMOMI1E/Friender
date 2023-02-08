from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import transaction

from .models import *
import json


def main(request):
    return render(request, 'main.html')


def add_user(request):
    if request.method == 'POST':
        print(request.POST)
        Users.objects.create(name=request.POST['name'],
                             surname=request.POST['surname'],
                             age=request.POST['age'],
                             sex=request.POST['sex']
                             )
        redirect('/app/main')
    return render(request, 'add_user.html')


def host(request):
    users = Users.objects.all()
    return render(request, 'host.html', {"users": users})


def add_users(request):
    return render(request, 'Users.html')
