from django.contrib import admin
from django.urls import path, include

appName = open("/data/data/com.termux/files/home/tools/djSocket/vars.txt").read().strip().split("|")[1]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(f'{appName}.urls'))
]