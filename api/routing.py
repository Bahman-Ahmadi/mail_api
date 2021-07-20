from django.urls import path
appName = open("/data/data/com.termux/files/home/tools/djSocket/vars.txt").read().strip().split("|")[1]
exec(f"from {appName} import consumers")

websocket_urlpatterns = [
    path("ws/", consumers.AppConsumer),
]
