from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
appName = open("/data/data/com.termux/files/home/tools/djSocket/vars.txt").read().strip().split("|")[1]
exec(f"from {appName} import routing")

application = ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    )
})