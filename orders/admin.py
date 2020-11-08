from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Client)


@admin.register(Print_paper)
class Print_paperAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_if_before_1000', 'price_if_after_1000', 'price_form_print')

@admin.register(Devision)
class DevisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_phone', 'client_company', 'count', 'paper', 'devision_paper', 'print_paper', 'total_price', 'price_for_one')
    list_display_links = ('id', 'client_name')
    search_fields = ('client_name', 'client_company',)

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'format_paper',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'format_paper')