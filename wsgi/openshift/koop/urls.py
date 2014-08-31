from django.conf.urls import patterns, include, url

import django.views.generic.base as django_views

import koop.views as koop_views
from koop.views import UploadView, FolderCreateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', koop_views.MainView.as_view(), name='home'),
    url(r'^upload$', UploadView.as_view(), name='upload'),
    url(r'^folder$', FolderCreateView.as_view(), name='create_folder')
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
