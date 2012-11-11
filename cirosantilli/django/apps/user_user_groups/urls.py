from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.views.generic.create_update import create_object 
from django.views.generic.simple import direct_to_template

from views import UserGroupForm

#from user_user_groups.models import UserGroup

USERNAME_RE = r'(?P<username>[^/?]+)'
USERUSERGROUPS_URL = r'user-groups'
GROUP_NAME_RE = r'(?P<groupname>[^/?]+)'

username_url_re_prefix = r'^' + USERNAME_RE  + r'/' + USERUSERGROUPS_URL
username_groupname_url_re_prefix = username_url_re_prefix + r'/' + GROUP_NAME_RE

suffix = r'/$'

urlpatterns = patterns('user_user_groups.views',

    url(
        username_url_re_prefix + r'/create' + suffix,
        'create',
        name='user_user_groups_create',
    ),

    url(
        username_groupname_url_re_prefix +  r'/update' + suffix,
        'update',
        name='user_user_groups_update',
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
        username_url_re_prefix +  r'/delete' + suffix,
        'delete',
        name='user_user_groups_delete',
    ),

    url(
        username_url_re_prefix +  r'/copy' + suffix,
        'copy',
        name='user_user_groups_copy',
    ),

    url(
        username_groupname_url_re_prefix +  suffix,
        'detail',
        name='user_user_groups_detail',
    ),

)
