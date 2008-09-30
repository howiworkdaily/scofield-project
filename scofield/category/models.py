from django.db import models


class Category(models.Model):

    """
    base class for Categories
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

