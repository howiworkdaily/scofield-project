from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from scofield.product.models import Product
from scofield.customer.models import *

class Order(models.Model):

    """
    Customer Order model
    """

    customer = models.ForeignKey(User)
    phone = models.CharField('Phone Number', blank=False, max_length=30)

    # Billing Info
    bstreet1 = models.CharField('Street', blank=False, max_length=100)
    bstreet2 = models.CharField('Street', max_length=100, blank=True)
    bstate = models.CharField(max_length=100, blank=False)
    bcity = models.CharField(max_length=100, blank=False)
    bzip_code = models.CharField('Zip Code', blank=False, max_length=25)
    # Shipping Info
    sstreet1 = models.CharField('Street', blank=False, max_length=100)
    sstreet2 = models.CharField('Street', max_length=100, blank=True)
    sstate = models.CharField(max_length=100, blank=False)
    scity = models.CharField(max_length=100, blank=False)
    szip_code = models.CharField('Zip Code', blank=False, max_length=25)
    # Timestamp
    date_added = models.DateTimeField(default=datetime.now)

class OrderItem(models.Model):
    """
    Individual items related to an order
    """

    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField('Item Price', max_digits=14, decimal_places=2)
    tax = models.DecimalField('Item Tax', max_digits=14, decimal_places=2)
    discount = models.DecimalField(max_digits=14, decimal_places=2)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

class Payment(models.Model):
    """
    Customer Payments
    """

    customer = models.ForeignKey(Customer)
    order = models.ForeignKey(Order)
    payment_type = models.CharField('Payment Type', max_length=40, blank=True, null=True)
    payment_total = models.DecimalField('Payment Total', max_digits=14, decimal_places=2)

    date_added = models.DateTimeField(default=datetime.now)


