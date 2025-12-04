from functools import cached_property

from django.db import models

from Admin.models.order import ASSIGNED, CREATED, CANCELLED, COMPLETED, Order
from Admin.models.user import User


ONLINE, OFFLINE = 'ONLINE', 'OFFLINE'


class DriverProfile(models.Model):
    STATUS_CHOICES = (
        (ONLINE, ONLINE),
        (OFFLINE, OFFLINE),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="driver_profile"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=OFFLINE
    )

    is_busy = models.BooleanField(default=False)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_online(self):
        self.status = ONLINE
        self.save(update_fields=["status", "updated_at"])

    def mark_offline(self):
        self.status = OFFLINE
        self.save(update_fields=["status", "updated_at"])

    def mark_busy(self):
        self.is_busy = True
        self.save(update_fields=["is_busy", "updated_at"])

    def mark_free(self):
        self.is_busy = False
        self.save(update_fields=["is_busy", "updated_at"])

    @cached_property
    def get_CREATED_orders(self):
        return self.orders.filter(status=CREATED)

    @cached_property
    def get_CANCELLED_orders(self):
        return self.orders.filter(status=CANCELLED)

    @cached_property
    def get_ASSIGNED_orders(self):
        return self.orders.filter(status=ASSIGNED)

    @cached_property
    def get_COMPLETED_orders(self):
        return self.orders.filter(status=COMPLETED)

    @cached_property
    def order(self) -> Order:
        """
        :return: ASSIGNED order object or None
        """
        order = self.get_ASSIGNED_orders.first() if self.get_ASSIGNED_orders.exists() else None

        return order

    def __str__(self):
        return f"{self.user.username} ({self.user.role}){'🟢' if self.status else '🔴'}"
