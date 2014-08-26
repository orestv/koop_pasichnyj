from django.conf.urls import patterns, include, url

from django.contrib import admin

import django.views.generic.base as django_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('koop.urls'), name='koop'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
