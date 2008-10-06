from django.db import models


class Manufacturer(models.Model):

    """
    base class for Manufacturers
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)
    sortorder = models.IntegerField(default=0, help_text='set the sort order')
    published = models.BooleanField(default=1)


    def get_products(self):
        return self.product_set.filter(published=True)


