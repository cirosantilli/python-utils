import os

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

thisapp = os.path.split(os.path.dirname(os.path.abspath(__file__)))[1]

urlpatterns = patterns('',

    url('^static/js/main.js$',
        direct_to_template,
        {
            'template': thisapp+'/static/js/main.js',
            'extra_context': settings.CONTEXT,
        },
        name="cirosantilli_main_js",
    ),

)
