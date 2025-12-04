from django.urls import path
from Admin.views import DriverOnlineView, DriverOfflineView, DriverLocationUpdateView, \
    AvailableDriversListView, CompleteOrderView, CreateOrderView

urlpatterns = [
    path("driver/online/", DriverOnlineView.as_view(), name="driver_online"),
    path("driver/offline/", DriverOfflineView.as_view(), name="driver_offline"),
    path("driver/location/<str:latitude>/<str:longitude>/", DriverLocationUpdateView.as_view(), name="driver_location"),
    path("drivers/available/", AvailableDriversListView.as_view(), name="available_drivers"),
    path("order/create/", CreateOrderView.as_view(), name="create_order"),
    path("order/complete/", CompleteOrderView.as_view(), name="complete_order"),
]
