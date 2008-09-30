from django.db import models

from scofield.category.models import *
from scofield.manufacturer.models import Manufacturer


class Product(models.Model):

    """
    Base class for products
    """

    name = models.CharField(max_length=200, null=False, blank=False, help_text='Product Name')
    slug = models.SlugField(max_length=210, null=False, blank=False, help_text='Used for URLs, auto-generated from name if blank')
    sku = models.CharField(max_length=100, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=False)         

