from django.db import models
from datetime import datetime

from scofield.category.models import *
from scofield.manufacturer.models import Manufacturer
from scofield.tax.models import TaxClass


class ProductModel(models.Model):

    """
    Base class for products
    """

    name = models.CharField(max_length=200, null=False, blank=False, help_text='Product Name')
    slug = models.SlugField(max_length=210, null=False, blank=False, help_text='Used for URLs, auto-generated from name if blank')
    sku = models.CharField(max_length=100, null=True, blank=True, help_text='Product SKU or Part Number')
    category = models.ManyToManyField(Category, blank=False, null=False)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    msrp = models.DecimalField(max_digits=14, decimal_places=2)
    taxable = models.BooleanField(default=False)
    taxClass = models.ForeignKey(TaxClass, blank=True, null=True, help_text='If taxable, choose the type of tax')
    published = models.BooleanField(default=True)
    is_featured = models.BooleanField('Is Featured Product', default=False)
    related_products = models.ManyToManyField('self', blank=True, null=True, related_name='related_products')

    #timestamps
    date_added = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Product(ProductModel):
    """
    Product Model extends the abstract ProductModel
    """

    


class Price(models.Model):

    """
    Base class for product pricing
    """

    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=14, decimal_places=2)


class ProductLiterature(models.Model):
    """
    Any literature a product may have
    """

    product = models.ForeignKey(Product)


class ProductImage(models.Model):
    """
    Images for a product
    """

    product = models.ForeignKey(Product)

