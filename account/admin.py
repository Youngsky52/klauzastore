from django.contrib import admin

from account.models import Shopper

# Register your models here.

admin.site.register(Shopper)

class ShopperAdmin(admin.ModelAdmin):

    list_display = ['username','email']

    search_fields = ['name']



