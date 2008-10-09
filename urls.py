from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import os.path

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    url(r'^$', 'product.views.home', name='scofield_home'),
    (r'cart/', include('cart.urls')),
    (r'account/', include('account.urls')),
    (r'product/', include('product.urls')),
    (r'category/', include('category.urls')),
    (r'manufacturer/', include('manufacturer.urls')),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^accounts/', include('registration.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
    )

