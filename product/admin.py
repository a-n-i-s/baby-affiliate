from django.contrib import admin
from .models import Product,Tag

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['id',( 'name','price'),'detail','affiliate_url','image_url','tags',('created_at','updated_at')]
    readonly_fields = ['id', 'updated_at','created_at']
    list_display = ['name', 'price' , 'affiliate_url']
    list_filter = ['tags']
    filter_horizontal = ['tags']
    search_fields = ['name','price','tags__name']





@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

