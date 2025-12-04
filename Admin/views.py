from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from Admin.models.driver import DriverProfile, ONLINE
from Admin.models.order import Order, ASSIGNED
from Admin.permissions import IsClient, IsDriver
from Admin.serializers import DriverSerializer, DriverLocationSerializer, OrderSerializer


class DriverOnlineView(APIView):
    permission_classes = [IsAuthenticated, IsDriver]
    def post(self, request):
        try:
            driver = DriverProfile.objects.get(user=request.user)
        except DriverProfile.DoesNotExist:
            return Response({"error": "Driver Profile does not exists!"}, status=status.HTTP_404_NOT_FOUND)
        driver.mark_online()
        return Response({"message": "Driver set to ONLINE"}, status=status.HTTP_200_OK)


class DriverOfflineView(APIView):
    permission_classes = [IsAuthenticated, IsDriver]
    def post(self, request):
        try:
            driver = DriverProfile.objects.get(user=request.user)
        except DriverProfile.DoesNotExist:
            return Response({"error": "Driver Profile does not exists!"}, status=status.HTTP_404_NOT_FOUND)
        driver.mark_offline()
        return Response({"message": "Driver set to OFFLINE"}, status=status.HTTP_200_OK)


class DriverLocationUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsDriver]
    def post(self, request, latitude: str, longitude: str):
        try:
            driver = DriverProfile.objects.get(user=request.user)
        except DriverProfile.DoesNotExist:
            return Response({"error": "Driver does not exists!"}, status=status.HTTP_404_NOT_FOUND)
        if latitude is None or longitude is None:
            return Response({"error": "latitude or longitude not entered!"}, status=HTTP_400_BAD_REQUEST)
        serializer = DriverLocationSerializer(
            driver,
            data={'latitude': float(latitude), 'longitude': float(longitude)},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Location updated!"},
            status=status.HTTP_200_OK
        )


class AvailableDriversListView(generics.ListAPIView):
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        return DriverProfile.objects.filter(status=ONLINE, is_busy=False)


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated, IsClient]
    def post(self, request):
        user = request.user

        with transaction.atomic():
            available_driver: DriverProfile = (
                DriverProfile.objects
                .filter(status=ONLINE, is_busy=False)
                .select_for_update(skip_locked=True)
                .order_by("updated_at")
                .first()
            )

            if not available_driver:
                return Response({"error": "No available driver"}, status=HTTP_404_NOT_FOUND)

            available_driver.mark_busy()

            order = Order.manager.create(
                client=user,
                driver=available_driver,
                status=ASSIGNED,
                pickup_lat=0,
                pickup_lng=0,
                drop_lat=0,
                drop_lng=0,
            )

        return Response(OrderSerializer(order).data, status=HTTP_200_OK)


class CompleteOrderView(APIView):
    permission_classes = [IsAuthenticated, IsDriver]
    def post(self, request):
        driver: DriverProfile = request.user.driver_profile
        if not driver.order:
            return Response({"error": "You have no active order!"}, status=HTTP_404_NOT_FOUND)
        driver.order.complete()
        return Response({"message": "Order completed!"}, status=status.HTTP_200_OK)


from django.shortcuts import render

def driver_panel(request, driver_id):
    return render(request, "driver.html", {"driver_id": driver_id})

def client_panel(request):
    return render(request, "client.html")

