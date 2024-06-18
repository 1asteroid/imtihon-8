from django.contrib import admin
from django.template.defaultfilters import slugify
import uuid

from .models import Product, Order, OrderItem, Team, Blog
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", "price", "slug", "description", "create_date")
    list_display_links = ('id', "name", "price", "slug", "description", "create_date")
    prepopulated_fields = {"slug": ("name", )}
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', 'name')

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name + f'{uuid.uuid4()}')
        super().save_model(request, obj, form, change)


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', "paid", "complete", "create_date", "last_update")
    list_display_links = ('id', 'user', "paid", "complete", "create_date", "last_update")
    search_fields = ("id", "paid")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('user',)


@admin.register(OrderItem)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'product', "order", "create_date")
    list_display_links = ('id', 'product', "order", "create_date")
    search_fields = ("id", )
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('order',)


@admin.register(Team)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'full_name', "speciality", "description")
    list_display_links = ('id', 'full_name', "speciality", "description")
    search_fields = ("id", "full_name" )
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('speciality',)


@admin.register(Blog)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', "team", "text", "create_date")
    list_display_links = ('id', 'name', "team", "text", "create_date")
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('team',)




