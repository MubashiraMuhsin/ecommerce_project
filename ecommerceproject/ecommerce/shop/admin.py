from django.contrib import admin

# Register your models here.
from .models import Category, Product


class category_admin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    prepopulated_fields = {'slug': ('name',)}

class product_admin(admin.ModelAdmin):
    list_display = ['name','price','stocks','available','created','updated']
    list_editable = ['price','stocks','available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(Category,category_admin)
admin.site.register(Product,product_admin)