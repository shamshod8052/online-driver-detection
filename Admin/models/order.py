from django.db import models
from django.utils.timezone import now

from Admin.managers.order import OrderManager
from Admin.models.user import User

CREATED, CANCELLED, ASSIGNED, COMPLETED = 'CREATED', 'CANCELLED', 'ASSIGNED', 'COMPLETED'


class Order(models.Model):
    manager = OrderManager()

    STATUS_CHOICES = (
        (CREATED, CREATED),
        (ASSIGNED, ASSIGNED),
        (COMPLETED, COMPLETED),
    )

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    driver = models.ForeignKey(
        'DriverProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    pickup_lat = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_lng = models.DecimalField(max_digits=9, decimal_places=6)

    drop_lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    drop_lng = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=CREATED
    )

    created_at = models.DateTimeField(auto_now_add=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def assign_driver(self, driver: 'DriverProfile'):
        """Assign driver to this order"""
        self.driver = driver
        self.status = ASSIGNED
        self.assigned_at = now()
        self.save(update_fields=["driver", "status", "assigned_at"])

        driver.mark_busy()

    def complete(self):
        """Mark order as completed"""
        self.status = COMPLETED
        self.completed_at = now()
        self.save(update_fields=["status", "completed_at"])

        if self.driver:
            self.driver.mark_free()

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
