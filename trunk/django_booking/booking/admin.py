from django.contrib import admin
from models import *

class GroupItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    ordering = ('sort_order',)
admin.site.register(GroupItem, GroupItemAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'manager', 'info')
admin.site.register(Item, ItemAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'item', 'group', 'start', 'end', 'user', 'validated')
admin.site.register(Booking, BookingAdmin)

class ParamAdmin(admin.ModelAdmin):
    list_display = ('name', 'value_or_color')
admin.site.register(Param, ParamAdmin)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('item', 'group', 'action')
    save_as = True
    list_filter = ('item', 'group')
admin.site.register(Permission, PermissionAdmin)

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'info')
admin.site.register(Policy, PolicyAdmin)
