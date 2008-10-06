from django.conf.urls.defaults import *


urlpatterns = patterns('manufacturer.views',
    url(r'^(?P<manufacturer_slug>[-\w]+)/$', 'get_manufacturer', {}, 'scofield_manufacturer'),
 )

