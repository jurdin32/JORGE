from django.contrib import admin

# Register your models here.
from JORGE.snniper import Attr
from Personas.models import Lugar, Persona


class LugarInline(admin.StackedInline):
    model = Lugar
    extra = 0

@admin.register(Lugar)
class modelo(admin.ModelAdmin):
    list_display = Attr(Lugar)
    list_display_links = Attr(Lugar)
    search_fields = ['nombre']
    inlines = [LugarInline]

@admin.register(Persona)
class modelo(admin.ModelAdmin):
    list_display = Attr(Persona)
    list_display_links = Attr(Persona)
    readonly_fields = ['edad']
