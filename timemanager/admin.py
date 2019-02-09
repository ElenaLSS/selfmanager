from django.contrib import admin
from .models import SpecificTask, WeekDayTime
# Register your models here.


class SpecificTaskAdmin(admin.ModelAdmin):
    pass


class WeekDayTimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(SpecificTask, SpecificTaskAdmin)

admin.site.register(WeekDayTime, WeekDayTimeAdmin)
