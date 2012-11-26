from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.views.generic.create_update import create_object 
from django.views.generic.simple import direct_to_template

from views import UserGroupForm

from settings import THISAPP as thisapp

USERNAME_RE = r'(?P<owner_username>[^/?]+)'
ID2_RE = r'(?P<id2>[^/?]+)'

username_url_re_prefix = r'^' + USERNAME_RE 
username_id2_url_re_prefix = username_url_re_prefix + r'/' + ID2_RE
suffix = r'/$'

urlpatterns = patterns('user_user_groups.views',

    url(
        r'^$',
        'index_all',
        name='user_user_groups_index_all',
    ),

    url(
        username_url_re_prefix + r'/create' + suffix,
        'create',
        name='user_user_groups_create',
    ),

    url(
        username_id2_url_re_prefix +  r'/update' + suffix,
        'update2',
        name='user_user_groups_update2',
    ),

    url(
        username_url_re_prefix + suffix,
        'index',
        name='user_user_groups_index',
    ),

    url(
        username_url_re_prefix +  r'/bulk_action' + suffix,
        'bulk_action',
        name='user_user_groups_bulk_action',
    ),

    url(
        username_id2_url_re_prefix +  r'/bulk_action2' + suffix,
        'bulk_action2',
        name='user_user_groups_bulk_action2',
    ),

    url(
        username_id2_url_re_prefix +  suffix,
        'detail',
        name='user_user_groups_detail',
    ),

)
