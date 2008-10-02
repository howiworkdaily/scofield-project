from django.db import models


class TaxClass(models.Model):
    """
    Tax rate for a product.
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, help_text='Description of products to be taxed')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Tax Class"
        verbose_name_plural = "Tax Classes"

class Tax(models.Model):
    """
    Tax Percentage
    """
    taxClass = models.ForeignKey(TaxClass)
    percentage = models.DecimalField(max_digits=7, decimal_places=2)

    def _display_percentage(self):
        return "%#2.2f%%" % (100*self.percentage)
    _display_percentage.short_description = 'Percentage'
    display_percentage = property(_display_percentage)    

    class Meta:
        verbose_name = "Tax"
        verbose_name_plural = "Tax"

