from django.contrib import admin
from .models import Pet
from django.utils.html import format_html


class CustomAdmin(admin.ModelAdmin):
    list_display = ['name','breed','gender','description','img_display']
    list_filter =['gender']
    search_fields=['breed']

    def img_display(self,obj):
        return format_html('<img src="{}" width="80" height="90"/>',obj.image.url)

# Register your models here.
admin.site.register(Pet,CustomAdmin)
admin.site.site_header="Pet Store Admin Panel"
admin.site.site_title="Welcome to Pet Store"
admin.site.index_title="Pet App Admin"