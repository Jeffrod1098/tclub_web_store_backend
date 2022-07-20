from django.contrib import admin

# Register your models here.
from .models import Item, CartItem, Cart, Comment

admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Comment)
