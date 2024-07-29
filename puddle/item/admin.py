from django.contrib import admin

# Register your models here.

from item.models import Category,Item

admin.site.register(Category)
admin.site.register(Item)
