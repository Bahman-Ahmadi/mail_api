from django.urls import path
appName = open("/data/data/com.termux/files/home/tools/djSocket/vars.txt").read().strip().split("|")[1]
exec(f"from {appName} import views")

urlpatterns = [
    path('', views.index, name='index')
]