from django.contrib import admin
from .models import SpecificTask, WeekDayTime
# Register your models here.


class SpecificTaskAdmin(admin.ModelAdmin):
    pass


class WeekDayTimeAdmin(admin.ModelAdmin):
    list_display = ('headline', 'day', 'time', 'time_length')

    def headline(self, obj):
        return obj.specific_task.headline


admin.site.register(SpecificTask, SpecificTaskAdmin)

admin.site.register(WeekDayTime, WeekDayTimeAdmin)
