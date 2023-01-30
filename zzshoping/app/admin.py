from django.contrib import admin

# Register your models here.
from .models import Cart,Customer,Order_placed,Product
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state','zipcode']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__']
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','__str__']
@admin.register(Order_placed)
class OrderedAdmin(admin.ModelAdmin):
    list_display=['user','__str__']