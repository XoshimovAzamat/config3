from django.contrib import admin
from django.urls import path, include
from configapp.views import *
from configapp1.views import *
from configapp2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('configapp.urls')),
    path('app1/', include('configapp1.urls')),
    path('app2/', include('configapp2.urls')),
]
