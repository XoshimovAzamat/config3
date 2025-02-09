from django.contrib import admin
from django.urls import path
from configapp1.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app3/', app3),
    path('app4/', app4),
    path('app5/', app5),
]