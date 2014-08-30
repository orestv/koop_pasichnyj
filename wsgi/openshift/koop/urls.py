from django.conf.urls import patterns, include, url

import django.views.generic.base as django_views

import koop.views as koop_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', koop_views.MainView.as_view(), name='home'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
