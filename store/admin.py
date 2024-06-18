from django.contrib import admin
from.models import Categorey, Size, Color, Product, Imageproduct

# Register your models here.
@admin.register(Categorey)
class CategoryAdmin(admin.ModelAdmin):
    list_display= 'name', 'slug'

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Imageproduct)
class ImageproductAdmin(admin.ModelAdmin):
    pass

