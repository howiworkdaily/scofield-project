from django.db import models


class Manufacturer(models.Model):

    """
    base class for Manufacturers
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)


