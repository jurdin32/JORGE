from django.contrib import admin

# Register your models here.
from Inicio.models import Premio
from JORGE.snniper import Attr


@admin.register(Premio)
class modelo(admin.ModelAdmin):
    list_display = Attr(Premio)
    list_display_links = Attr(Premio)
