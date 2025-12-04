from django.contrib.auth.models import AbstractUser
from django.db import models


DRIVER, CLIENT = 'DRIVER', 'CLIENT'


class User(AbstractUser):
    ROLE_CHOICES = (
        (DRIVER, DRIVER),
        (CLIENT, CLIENT),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"
