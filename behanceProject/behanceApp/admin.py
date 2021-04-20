from django.contrib import admin
from .models import Information


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'phone']

admin.site.register(Information, UserAdmin)
