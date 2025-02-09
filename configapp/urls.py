from django.contrib import admin
from django.urls import path
from configapp.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app),
    path('app1/', app1),
    path('app2/', app2),
]