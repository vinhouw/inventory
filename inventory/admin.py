from django.contrib import admin

# Register your models here.
from .models import Item, Category

admin.site.register(Item)
admin.site.register(Category)

class ItemInline(admin.TabularInline):
    model = Item

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, 
    ]