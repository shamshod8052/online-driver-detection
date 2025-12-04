from django.db import models

from Admin.models.user import User


class OrderManager(models.Manager):
    def create(
            self, client: User, driver: 'DriverProfile', status: str,
            pickup_lat: float, pickup_lng: str, drop_lat: str=None,
            drop_lng: str=None
    ):
        order = super().create(
            client=client,
            driver=driver,
            status=status,
            pickup_lat=pickup_lat,
            pickup_lng=pickup_lng,
            drop_lat=drop_lat,
            drop_lng=drop_lng,
        )

        return order
