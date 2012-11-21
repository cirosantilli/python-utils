from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('cirosantilli.urls')),

    url(r'^master-checkbox/', include('master_checkbox.urls')),

    #<userena
    url(r'^users/', include('userena.urls')),
    #>userena

    url(r'^user-groups/', include('user_user_groups.urls')),

    url(r'^django_tables2_datatables/', include('django_tables2_datatables.urls')),
    
)

urlpatterns += staticfiles_urlpatterns() #to serve static files
