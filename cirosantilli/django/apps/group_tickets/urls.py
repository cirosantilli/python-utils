from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',

    ##without generic templates:
    #url(r'^$', 'index'),
    #url(r'^(?P<poll_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote

    #with generic templates:
    url(r'^$',
            ListView.as_view( #premade view: list of object
            queryset=Poll.objects.order_by('-pub_date')[:5], #what to list
            context_object_name='latest_poll_list', #object passed to the template
            template_name='polls/index.html'), #template is uses. has default <app_name>/<model_name>_list.html
        name='poll_index'), #to refer to its url with reverse (and so url in templates). therefore, this must be unique

    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll, #which model is being detailed
            template_name='polls/detail.html'), #has default teplate <app_name>/<model_name>_detail.html
        name='poll_detail'),

    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),

    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
