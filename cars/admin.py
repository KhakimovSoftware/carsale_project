from django.contrib import admin
from .models import CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id',  'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')



admin.site.register(CarModel)

