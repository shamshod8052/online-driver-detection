from django.contrib import admin

from Admin.models.driver import DriverProfile


@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'is_busy', 'order', 'latitude', 'longitude', 'updated_at')
    list_filter = ('status', 'is_busy')
    search_fields = ('user__username', 'user__email', 'latitude', 'longitude')
    readonly_fields = ('updated_at', 'created_at')
    ordering = ('-created_at',)

    def order(self, obj):
        return obj.order or '-'
    order.short_description = 'Active order'
