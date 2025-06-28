import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rt_chat.settings')

django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
# This ASGI configuration file sets up the Django application to handle both HTTP and WebSocket protocols.
# It uses Django's ASGI application for HTTP requests and Channels' URLRouter for WebSocket connections.
# The AuthMiddlewareStack is used to handle authentication for WebSocket connections, allowing users to
# access WebSocket endpoints with their authenticated session.