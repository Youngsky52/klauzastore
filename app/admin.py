from django.contrib import admin

from app.models import Produit

# Register your models here.
admin.site.register(Produit)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']

    search_fields = ['name']
