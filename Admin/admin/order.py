from django.contrib import admin

from Admin.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'driver', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('pickup_lat', 'pickup_lng', 'drop_lat', 'drop_lng', 'client__username', 'driver__user__username')
    readonly_fields = ('created_at', 'assigned_at', 'completed_at')
    ordering = ('-created_at',)
