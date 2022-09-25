from django.contrib import admin

# Register your models here.
from .models import Drug
@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['image_show','title']
    list_filter = ['expiration_date']
    list_per_page = 10
    search_fields = ['title','description']
