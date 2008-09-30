from django.db import models
from datetime import datetime

from scofield.category.models import *
from scofield.manufacturer.models import Manufacturer


class ProductModel(models.Model):

    """
    Base class for products
    """

    #timestamps
    date_added = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

class Product(ProductModel):
    """
    Product Model extends the abstract ProductModel
    """

    name = models.CharField(max_length=200, null=False, blank=False, help_text='Product Name')
    slug = models.SlugField(max_length=210, null=False, blank=False, help_text='Used for URLs, auto-generated from name if blank')
    sku = models.CharField(max_length=100, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=False, null=False)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    msrp = models.DecimalField(max_digits=14, decimal_places=2)


class Price(models.Model):

    """
    Base class for product pricing
    """

    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=14, decimal_places=2)

