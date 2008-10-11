from django.db import models
from django.core import urlresolvers


class Category(models.Model):

    """
    base class for Categories
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    sortorder = models.IntegerField(default=0, help_text='set the sort order')
    published = models.BooleanField(default=1)

    def get_products(self):
        return self.product_set.filter(published=True)

    def get_absolute_url(self):
        """ return a reversable url """
        return urlresolvers.reverse('scofield_category',
            kwargs={'category_slug': self.slug})

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

