from django.contrib import admin

# Register your models here.
from .models import Doctor
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['image_show','fullname','profession','job']
    list_filter = ['profession','job']
    search_fields = ['fullname','profession','job','phone']
    list_editable = ['fullname','profession','job']
    list_display_links =['image_show']
    list_per_page = 10
admin.site.register(Doctor,DoctorAdmin)