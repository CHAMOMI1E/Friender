from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('add_user/', add_user, name='add_user'),
    path('mine/', MyView.as_view(), name='my-view'),
    path('host/', host, name='host'),

]
