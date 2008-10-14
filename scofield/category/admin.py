from category.models import *
from django.contrib import admin

class CategoryOptions(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'sortorder', 'published']

admin.site.register(Category, CategoryOptions)

