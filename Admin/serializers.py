from rest_framework import serializers

from Admin.models.order import Order
from Admin.models.driver import DriverProfile


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = DriverProfile
        fields = ['id', 'user', 'status', 'is_busy', 'latitude', 'longitude', 'updated_at']

class DriverLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = ["latitude", "longitude"]

class OrderSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "client", "driver", "status", "created_at"]
        read_only_fields = ["status", "driver", "client"]
