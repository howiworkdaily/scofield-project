from django.db import models


class Category(models.Model):

    """
    base class for Categories
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    sortorder = models.IntegerField(default=0, help_text='set the sort order')
    published = models.BooleanField(default=1)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

