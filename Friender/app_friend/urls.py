from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('add_user/', add_user, name='add_user'),
    path('host/', host, name='host'),

]
