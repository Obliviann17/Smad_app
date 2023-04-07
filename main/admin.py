from django.contrib import admin
from .models import *

class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'photo', 'available', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('available',)
    search_fields = ('name',)

admin.site.register(Products, MainAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'email', 'address', 'phone_number', 'city',
                    'paid', 'created', 'updated', 'card_number', 'cvv_code', 'validity']
    list_filter = ['paid', 'created', 'updated']

admin.site.register(Order, OrderAdmin)
