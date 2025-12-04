from django.urls import path
from Admin.consumers import DriverConsumer, OrderConsumer

websocket_urlpatterns = [
    path("ws/drivers/", DriverConsumer.as_asgi()),
    path("ws/orders/", OrderConsumer.as_asgi()),
]
