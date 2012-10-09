from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

#TODO get it to show a specific generic template at a URL

urlpatterns = patterns('',

    ('^$', direct_to_template, {
        'template': 'home.html'
    }),
    #home page 

    ('^about/$', direct_to_template, {
        'template': 'about.html'
    }),
    #static page, simple generic view

    url(r'^polls/', include('polls.urls')),
    #mounts all the admin urls defined in admin.site.urls on top of admin/

    url(r'^admin/', include(admin.site.urls)),

    #<userena
    url(r'^accounts/', include('userena.urls')),
    #</userena
)
