from django.conf.urls.defaults import *


urlpatterns = patterns('product.views',
    url(r'^(?P<product_slug>[-\w]+)/$', 'get_product', {}, 'scofield_product'),
 )
