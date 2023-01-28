from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *


def main(request):
    return render(request, 'main.html')
