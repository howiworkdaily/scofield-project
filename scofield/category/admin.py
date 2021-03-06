from models import *
from forms import CategoryImageForm
from django.contrib import admin

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    form = CategoryImageForm

class CategoryOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'parent', 'sortorder', 'published']

    inlines = [
        CategoryImageInline,
    ]

    fieldsets = (
    (None, {
                'fields': ('name', 'slug', 'parent', 'sortorder', 'published',)
            }),
    ('Meta options', {
               'classes': ('collapse',),
               'fields': ('meta_keywords', 'meta_description', )
           }),
    )
    
class CategoryImageAdmin(admin.ModelAdmin):
    model = CategoryImage
    form = CategoryImageForm
        
admin.site.register(CategoryImage, CategoryImageAdmin)
admin.site.register(Category, CategoryOptions)