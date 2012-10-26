from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template

from user_user_groups.models import 
from polls.models import Poll

urlpatterns = patterns('',

    url(r'^$',
            ListView.as_view(
                    queryset=Poll.objects.order_by('-pub_date')[:5],
                    context_object_name='latest_poll_list',
                    template_name='polls/index.html',
                    paginate_by=10,
                    ),
            name='poll_index'),

)
