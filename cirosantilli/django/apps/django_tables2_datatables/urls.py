import os

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

thisapp = os.path.split(os.path.dirname(os.path.abspath(__file__)))[1]

urlpatterns = patterns('',

    url('^media/js/jquery.dataTables.config.js$',
        direct_to_template,
        {
            'template': thisapp+'/media/js/jquery.dataTables.config.js',
            'extra_context': settings.CONTEXT,
        },
        name="django_tables2_datatables_config_js",
    ),

)
