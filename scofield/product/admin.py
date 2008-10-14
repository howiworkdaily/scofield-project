from models import *
from forms import *
from django.contrib import admin

class ProductImage_Inline(admin.TabularInline):
    model = ProductImage
    form = ProductImageForm
    
class ProductImageAdmin(admin.ModelAdmin):
    model = ProductImage
    form = ProductImageForm

class ProductPrice_Inline(admin.StackedInline):
    model = Price
    extra = 1

class ProductLiterature_Inline(admin.StackedInline):
    model = ProductLiterature
    extra = 3

class ProductOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImage_Inline, ProductLiterature_Inline, ProductPrice_Inline]
    list_display = ['name', 'sku', 'is_featured', 'published']
    search_fields = ['slug', 'sku', 'name', 'description']
    
    inlines = [
        ProductImage_Inline,
    ]


admin.site.register(Price)
admin.site.register(Product, ProductOptions)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductLiterature)
admin.site.register(Discount)

