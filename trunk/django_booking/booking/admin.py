from django.contrib import admin
from models import *

class ParamProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
admin.site.register(ParamProfile, ParamProfileAdmin)


class DataUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'last_name', 'first_name', 'profile', 'locked', 'admin', 'email')
admin.site.register(DataUser, DataUserAdmin)

class ParamFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    ordering = ('sort_order',)
admin.site.register(ParamFamily, ParamFamilyAdmin)

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'manager')
admin.site.register(Data, DataAdmin)

class DataBookingAdmin(admin.ModelAdmin):
    list_display = ('data', 'start', 'end', 'user', 'validated')
admin.site.register(DataBooking, DataBookingAdmin)

class ParamAdmin(admin.ModelAdmin):
    list_display = ('name', 'value_or_color')
admin.site.register(Param, ParamAdmin)

class ParamLangAdmin(admin.ModelAdmin):
    list_display = ('english', 'french', 'german', 'norwegian')
admin.site.register(ParamLang, ParamLangAdmin)
