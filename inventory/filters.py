# pip install django-filter
# pip install django-crispy-forms

import django_filters
from inventory.models import Item, Category


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item 
        fields = ['name']

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['category_name']
