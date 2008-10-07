from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from product.models import Product
from customer.models import *

class Order(models.Model):

    """
    Customer Order model
    """

    customer = models.ForeignKey(User)
    address = models.ForeignKey(Address)
    phone = models.ForeignKey(Phonenumber, null=True, blank=True)

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


