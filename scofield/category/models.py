from django.db import models
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    """
    base class for Categories
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=210, null=False, blank=False)
    meta_description = models.TextField(_('description'), blank=True, null=True)
    meta_keywords = models.TextField(_('keywords'), blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    sortorder = models.IntegerField(default=0, help_text='set the sort order')
    published = models.BooleanField(default=1)
    
    @property
    def main_image(self):
        img = False
        if self.images.count() > 0:
            img = self.images[0]
        else:
            if self.parent_id:
                img = self.parent.main_image

        if not img:
            #TODO: this should return a default "Image Not Found" placeholder image we install by default
            try:
                img = CategoryImage.objects.filter(category__isnull=True).order_by('sort')[0]
            except IndexError:
                import sys
                print >>sys.stderr, 'Warning: default category image not found - try syncdb'

        return img

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


class CategoryImage(models.Model):
    """
    Image(s) for your category.

    """
    category = models.ForeignKey(Category, null=True, blank=True, related_name="images")
    picture = models.ImageField(upload_to="images",) 
    caption = models.CharField(_("optional caption"), max_length=100, null=True, blank=True, help_text="And used as the alt text in the html.")
    sortorder = models.IntegerField(_("sort order"), )

    def __unicode__(self):
        if self.category:
            return u"Image of Category %s" % self.category.slug
        elif self.caption:
            return u"Image with caption \"%s\"" % self.caption
        else:
            return u"%s" % self.picture

    class Meta:
        ordering = ['sortorder']

