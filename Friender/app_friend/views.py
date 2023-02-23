from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import ListView

from .models import *
import json
from django.views.generic.edit import CreateView


def main(request):
    return render(request, 'main.html')


#
# def add_user(request):
#     if request.method == 'POST':
#         print(request.POST)
#         Users.objects.create(name=request.POST['name'],
#                              surname=request.POST['surname'],
#                              age=request.POST['age'],
#                              sex=request.POST['sex'],
#                              phone=request.POST['phone'],
#                              msg=request.POST['msg'],
#
#                              )
#         redirect('/app/main')
#     return render(request, 'add_user.html')

class add_user(CreateView):
    template_name = 'add_user_form.html'
    model = 'Users'
    fields = ['name', 'surname', 'age', 'sex', 'phone', 'msg']
    success_url = reverse_lazy("my-view")


class MyView(ListView, PermissionRequiredMixin):
    template_name = "form.html"
    model = Users
    context_object_name = "users"


def host(request):
    users = Users.objects.all()
    return render(request, 'host.html', {"users": users})
