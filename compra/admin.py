from django.contrib import admin
from .models import Compra, Item


class ItemInline(admin.TabularInline):
    model = Item


class CompraAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
admin.site.register(Compra, CompraAdmin)