from django.contrib import admin

from .models import exampleModal


# Register your models here.
class exampleModalAdmin(admin.ModelAdmin):
    list_display = ('name', 'fistName', 'data')
    list_filter = ('name', 'fistName', 'data')
    search_fields = ('name', 'fistName', 'data')
    list_per_page = 25


admin.site.register(exampleModal, exampleModalAdmin)
