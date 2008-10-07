from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    url(r'^$', 'product.views.home', name='scofield_home'),
    (r'account/', include('account.urls')),
    (r'product/', include('product.urls')),
    (r'category/', include('category.urls')),
    (r'manufacturer/', include('manufacturer.urls')),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^accounts/', include('registration.urls')),

)

