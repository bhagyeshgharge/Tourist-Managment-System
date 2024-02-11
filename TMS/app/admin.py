from django.contrib import admin
from app.models import Package

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display=['Place','Country','State','Price','Days','Night','Description','is_active','Image','Image2','Image3','Image4']
    list_filter=['is_active']

admin.site.register(Package,PackageAdmin)

