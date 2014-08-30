from django.conf.urls import patterns, include, url

from django.contrib import admin

import django.views.generic.base as django_views
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('^$', RedirectView.as_view(url='/reports')),
    url(r'^reports/', include('koop.urls'), name='koop'),
    url(r'^api/', include('api.urls'), name='api_views'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
