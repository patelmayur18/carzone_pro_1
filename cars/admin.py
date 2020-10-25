from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.car_photo.url))


    list_display = ('id','car_title','thumbnail','color','modal','year','body_style','fuel_type','is_fetured')
    list_display_links = ('car_title','thumbnail')
    list_editable = ('is_fetured',)

admin.site.register(Car,CarAdmin)