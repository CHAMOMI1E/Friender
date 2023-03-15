from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', main, name='main'),
    #path('add_user/', add_user.as_view(), name='add_user'),
    path('add_user/', add_user.as_view(), name='add_user'),
    path('host/', host, name='host'),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
