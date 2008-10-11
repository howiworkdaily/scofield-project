from product.models import *
from django.contrib import admin

class ProductImage_Inline(admin.StackedInline):
    model = ProductImage
    extra = 3

class ProductPrice_Inline(admin.StackedInline):
    model = Price
    extra = 1

class ProductLiterature_Inline(admin.StackedInline):
    model = ProductLiterature
    extra = 3

class ProductOptions(admin.ModelAdmin):
    inlines = [ProductImage_Inline, ProductLiterature_Inline, ProductPrice_Inline]

admin.site.register(Price)
admin.site.register(Product, ProductOptions)
admin.site.register(ProductImage)
admin.site.register(ProductLiterature)
admin.site.register(Discount)

