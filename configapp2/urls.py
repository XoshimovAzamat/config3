from django.contrib import admin
from django.urls import path
from configapp2.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app6/', app6),
    path('app7/', app7),
    path('app8/', app8),
]