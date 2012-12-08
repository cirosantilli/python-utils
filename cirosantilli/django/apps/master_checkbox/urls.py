from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

urlpatterns = patterns('',

    url('^static/js/main.js$',
        direct_to_template,
        {
            'template': settings.THISAPP+'/media/js/master-checkbox.js',
            'extra_context': settings.CONTEXT,
        },
        name=settings.THISAPP+"_js",
    ),

)


