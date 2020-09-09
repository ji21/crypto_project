from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from api.consumers import PriceConsumer
from django.urls import path

# from django.conf.urls import url

websocket_url_pattern = [
  path('ws/priceData/', PriceConsumer)
]

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_url_pattern)
          )
      )
})
