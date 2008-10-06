from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^(?P<product_slug>[-\w]+)/$', "product.views.get_product", name="product_details"),
 )
