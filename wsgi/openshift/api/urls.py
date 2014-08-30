from api.views import TreeView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^tree$', TreeView.as_view(), name='tree_view'),

)