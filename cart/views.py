from django import http
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from utils import bad_or_missing
from django.contrib.auth.models import User
from django.utils._decimal import Decimal
from product.models import *
from cart.models import *


def add(request):
    """
    Add product to cart
    """
    if request.method == 'POST':
        next = request.POST.get("next")
        try:
            product = Product.objects.get(published=True, slug=request.POST['product'])
        except Product.DoesNotExist:
            return bad_or_missing(request, 'The product have requested is not in the catalog.')

        if 'cart' in request.session:
            if Cart.objects.get(pk=request.session['cart']):
                cart = Cart.objects.get(pk=request.session['cart'])
                if CartItem.objects.filter(cart=cart, object_id=product.id):
                    item = CartItem.objects.get(cart=cart, object_id=product.id)
                    item.quantity = item.quantity + int(request.POST['quantity'])
                    item.save()
                
                else:
                    cartitems = CartItem(cart=cart, content_object=product, quantity=request.POST['quantity'])
                    CartItem.save(cartitems)
        else:
            cart = Cart()
            cart.save()
            request.session['cart'] = cart.id
            cartitems = CartItem(cart=cart, content_object=product, quantity=request.POST['quantity'])
            CartItem.save(cartitems)

        print request.session['cart']
    
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse("show_cart"))


def show(request, template_name="cart/show.html"):
    """
    returns the current cart or not
    """

    if 'cart' in request.session:
        cart = Cart.objects.get(pk=request.session['cart'])
        cartitems = CartItem.objects.filter(cart=cart)
        product = []
        total = 0
        for c in cartitems:
            prod = Product.objects.get(pk=c.object_id)
            price = Price.objects.get(product=prod.id)
            prod.quantity = c.quantity
            product.append(prod)
            print price
            total = total + (c.quantity * price.price)

    else:
        product = None
        
    return render_to_response(template_name, {
        "product": product,
        "total": total,
    }, context_instance=RequestContext(request))
