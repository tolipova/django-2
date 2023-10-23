from django.contrib import admin
from .models import Malumot
from django.utils.html import format_html
from django.utils.html import mark_safe
# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display = ('ism','about','age','get_html_photo',)
    list_filter = ('ism',)

    def get_html_photo(self,object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None
    get_html_photo.short_description = 'Surat'
admin.site.register(Malumot, InformationAdmin)
