from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, model_to_dict
from django.forms.widgets import SelectMultiple
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods, require_safe

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from django_tables2_datatables import tables as dtd_tables
from helpers import url_add_app, render_thisapp

import user_list_uri.views
from user_list_uri.models import List
import user_user_groups.views
from user_user_groups.models import UserGroup
from .models import Issue

N_ISSUES_SERVER = 100
ITEMS_PER_PAGE = 100
ORDER_BY = '-creation_date'
FILTER_USER_LIST_NAME = 'ul' #user list filter table: "<input name="'+FILTER_URI_LIST_NAME+'">"
FILTER_URI_LIST_NAME = 'il' #uri list filter table: "<input name="'+FILTER_URI_LIST_NAME+'">"
FILTER_SERVER_FORM_ID = 'filter-server' #in the form that gets server data: <form id="'+FILTER_SERVER_FORM_ID+'">

def get_issue_table(
        data,
        id='issue-table',
    ):

    class T(tables.Table):

        id = dtd_tables.LinkColumn(
            url_add_app('detail'),
            args=[A('pk')],
        )

        creator = dtd_tables.LinkColumn(
            'userena_profile_detail',
            args=[A('creator.username')],
        )

        class Meta(dtd_tables.Meta):

            model = Issue

            fields = (
                'title',
                'creation_date',
                'uri',
            )

            sequence = [
                'id',
                'creator',
                'title',
                'uri',
                'creation_date',
            ]

    T.Meta.attrs["id"] = id

    return T(data)

class GetIssuesForm(forms.Form):
    form_id = 'get-issues'
    n = forms.IntegerField(
        initial = N_ISSUES_SERVER,
        widget = forms.TextInput(
            attrs={
                'form':form_id,
            }
        ),
    )

@require_safe
def index_all(request):
    """lists of issues
    
    get params
    ==========

    - FILTER_URI_LIST_NAME

        only uris in one of the given pk of uri lists will be gotten from server

        can be used multiple times

        Example:

            FILTER_URI_LIST_NAME='ul'

            ul=123&ul456

            only issues with uris inside lists with pks 123 or 456 will be selected

        if none is given, then all issues are selected
    """

    all_items_db = Issue.objects.order_by(ORDER_BY)

    #get_items_form = GetIssuesForm(request.GET)
    #if form.is_valid():
        #nItems = get_items_form.cleaned_data['n']
    #else:
        #nItems = N_items_SERVER
    #selected_items = all_items_db[:nItems]

    #filter by user lists
    filter_user_lists_pk = request.GET.getlist(FILTER_USER_LIST_NAME)
    filter_usernames = []
    for filter_user_list_pk in filter_user_lists_pk:
        list = get_object_or_404(UserGroup, pk=filter_user_list_pk)
        users_in_group = list.useringroup_set.all()
        filter_usernames.extend( user_in_group.user.username for user_in_group in users_in_group )

    user_list_table = user_user_groups.views.get_user_list_table(
        UserGroup.objects.order_by(ORDER_BY),
        has_owner=True,
        has_selection=True,
        form=FILTER_SERVER_FORM_ID,
        id='user-lists-table',
        selection_args={
            'name':FILTER_USER_LIST_NAME,
            'accessor':'pk',
        },
    )
    user_list_table_filter = dtd_tables.get_table_filter(user_list_table)

    #filter by uri lists
    filter_uri_lists_pk = request.GET.getlist(FILTER_URI_LIST_NAME)
    filter_uris = []
    for filter_uri_list_pk in filter_uri_lists_pk:
        list = get_object_or_404(List,pk=filter_uri_list_pk)
        uris_in_group = list.item_set.all()
        filter_uris.extend( uri_in_group.uri for uri_in_group in uris_in_group )

    uri_list_table = user_list_uri.views.get_list_table(
        List.objects.order_by(ORDER_BY),
        has_owner=True,
        has_selection=True,
        form=FILTER_SERVER_FORM_ID,
        id='uri-lists-table',
        selection_args={
            'name':FILTER_URI_LIST_NAME,
            'accessor':'pk',
        },
    )
    uri_list_table_filter = dtd_tables.get_table_filter(uri_list_table)

    #get issues table
    selected_issues = Issue.objects.all()
    if filter_usernames:
        selected_issues = selected_issues.filter(creator__username__in=filter_usernames)
    if filter_uris:
        selected_issues = selected_issues.filter(uri__in=filter_uris)
    table = get_issue_table(selected_issues)
    table_filter = dtd_tables.get_table_filter(table)

    return render_thisapp(
        request,
        'index_all',
        {
            'n_items_db': all_items_db.count(),
            #'get_items_form': get_items_form,
            'table': table,
            'table_filter': table_filter,
            'uri_list_table': uri_list_table,
            'uri_list_table_filter': uri_list_table_filter,
            'user_list_table': user_list_table,
            'user_list_table_filter': user_list_table_filter,
        },
    )

#def get_item_table(
        #data,
        #id='',
        #form='',
        #has_selection=True,
    #):
    #"""returns an instance of a class named UserTable derived from tables.Table

    #:param data: table data
    #:type data: data accepted by a django_tables2.Table constructor
    #:param id: <table id="id">
    #:type id: string
    #:param form: <td><input form="form">
    #:type form: string
    #:param has_selection: if True, table gets a master checkbox column at right
    #:type has_selection: boolean
    #"""

    #class T(tables.Table):

        #if has_selection:
            #selection = dtd_tables.MasterCheckBoxColumn(
                #"select-users",
                #name="usernames",
                #form=form,
                #accessor="username",
            #)

        #class Meta(dtd_tables.Meta):

            #model = Item

            #fields = (
                #'uri',
                #'date_added',
            #)

            #sequence = []
            #if has_selection:
                #sequence.append('selection')
            #sequence.extend([
                #'uri',
                #'date_added',
            #])

        #Meta.attrs['id'] = id

    #return T(data)

@require_safe
def detail(request, pk):

    issue = get_object_or_404(Issue, pk=pk)

    return render_thisapp(
        request,
        'detail',
        {
            'issue': issue,
        },
    )

#class UrisField(forms.Field):
    #"""to preprocess form data, make this new class
    
    #validated data will always be a list of strings split at \n or \r chars
    #and such that:

    #1) only one copy is kept of dupe lines
    #2) whiteline only lines are discarded
    #"""
    #def to_python(self, value):
        #"""
        #>>> "a\nb\rc\n\r\r\rd"
        #["a","b","c","d"]
        #>>> "b\na"
        #["a","b"]
        #>>> "a\na"
        #["a"]
        #>>> "a\n "
        #["a"]
        #"""
        #if not value:
            #return []
        #return list(set(sorted(filter(lambda v:v.strip(),value.splitlines()))))

##TODO 0 add help
#class ListForm(ModelForm):

    #uris = UrisField(
        #widget=forms.Textarea(),
        #required=False,
        #help_text='newline separated uris. whitechar lines ignored. dupes will be removed'
    #)

    #def __init__(self, *args, **kwargs):
        #"""
        #:param owner:
            #Auth.User object

            #if no owner is given, unicity check does nothing:
            #it is supposed by clean that this is the initial GET request.

            #rationale: without a owner, one cannot know if the
            #id2/owner_username pair is unique.

        #:param old_id2:
            #String

            #if given supposes it is an update of old_id2.
            #therefore, in that case, will only raise an unicity check error
            #it then new username/id2 is already taken and if the
            #new groupaname is different from the old one, meaning that the
            #user is trying to update the name to a new one.

        #:param instance:
            #same as super class instance, except this is also used to set initial data for
            #the uris textarea. therefore there is no need to user the initial
            #kwarg to do this:
            
            #>>> owner = get_object_or_404(User, username=owner_username)
            #>>> list = get_object_or_404(List, owner=owner, id2=id2)
            #>>> form = ListForm(instance=list)

            #and the initial['uris'] textarea will automatically get populated

            #if initial['uris'] is specified, it overides this automatic initialization
        #:type instance: List
        #"""

        #self.owner = kwargs.pop('owner',None)
        #self.old_id2 = kwargs.pop('old_id2',None)

        ##update initial values based on model
        #instance = kwargs.get('instance',None)
        #set_initial_uris = False
        #if instance: 
            #initial = kwargs.get('initial',{})
            #if initial:
                #uris = initial.get('uris','')
                #if not uris: #
                    #set_initial_uris = True
            #else:
                #kwargs['initial'] = {}
                #set_initial_uris = True

        ##at this point, kwargs['initial'] is assured to exist
        #if set_initial_uris:
            #kwargs['initial']['uris'] = "\n".join( item.uri for item in instance.item_set.all() )

        #super(ListForm, self).__init__(*args, **kwargs)

    #def clean(self):
        #"""
        #ensure owner/id2 pair is unique taking into consideration update
        #"""
        #cleaned_data = super(ListForm, self).clean()

        #if self.owner: #only for POST
            #new_id2 = cleaned_data.get('id2',None)
            #if new_id2:
                #if List.objects.filter(
                            #owner=self.owner,
                            #id2=new_id2
                        #).exists(): #new name exists: might be error
                    #error = False
                    #if( (self.old_id2 and self.old_id2 != new_id2 ) #update, and name different from old. error
                            #or not self.old_id2 ): #create and new name exists. error
                        #self._errors['id2'] = [_(
                                #"groupaname \"%s\" already exists for user \"%s\". "
                                #"please choose a different groupname."
                                #%(new_id2,self.owner.username)
                            #)]
        #return cleaned_data

    #class Meta:
        #model = List
        #fields = (
            #'id2',
            #'description',
            #'uris',
        #)

@require_http_methods(["GET","HEAD","POST"])
@login_required
def create_issue(request):

    if request.user != owner:
        return HttpResponse(_(
            "you are logged in as \"%s\" "
            "and cannot create a group for user \"%s\""
            % (request.user.username, owner.username)
        ))

    if request.method == "POST":
        form = ListForm(request.POST, owner=owner)
        if form.is_valid():
            print 'create'
            print form.cleaned_data
            uri_list = List.objects.create(
                owner=owner,
                id2=form.cleaned_data['id2'],
                description=form.cleaned_data['description'],
            )
            for uri in form.cleaned_data['uris']:
                Item.objects.create(
                    list=uri_list,
                    uri=uri,
                )
            return HttpResponseRedirect(reverse(
                url_add_app('index_user'),
                args=(owner_username,),
            ))
    else:
        form = ListForm()

    return render_thisapp(
        request,
        'create_list',
        {
            "form": form,
            "owner": owner,
        },
    )

#@require_http_methods(["GET","POST"])
#@login_required
#def update_list(request, owner_username, id2):

    #owner = get_object_or_404(User, username=owner_username)
    #list = get_object_or_404(List, owner=owner, id2=id2)

    #if request.user != owner:
        #return HttpResponse(_(
            #"you are logged in as \"%s\" "
            #"and cannot update a data for another user \"%s\""
            #% (request.user.username, owner.username)
        #))

    #if request.method == "POST":

        ##load post data on form so in case validation fails it will be redirected here
        #form = ListForm(
            #request.POST,
            #owner=owner,
            #old_id2=list.id2
        #)
        #if form.is_valid():

            ##update id2
            #new_id2 = form.cleaned_data['id2']
            #if new_id2 != list.id2: #validation already guarantees new name is available
                #list.id2 = new_id2
                #list.save()

            ##update description
            #new_description = form.cleaned_data['description']
            #if new_description != list.description:
                #list.description = new_description
                #list.save()

            ##update uris
            #old_items = list.item_set.all()
            #old_uris = [ item.uri for item in old_items ]
            #new_uris = form.cleaned_data['uris']

            ##add new ones
            #for new_uri in new_uris:
                #if not new_uri in old_uris:
                    #Item.objects.create(
                        #uri=new_uri,
                        #list=list,
                    #)

            ##delete removed ones
            #for old_uri in old_uris: 
                #if not old_uri in new_uris:
                    #next( item for item in old_items if item.uri==old_uri ).delete()

            #return HttpResponseRedirect(reverse(
                #url_add_app('detail'),
                #args=(owner_username,list.id2)
            #))
    #else:
        #form = ListForm(instance=list)

    #return render_thisapp(
        #request,
        #'update_list',
        #{
            #'form': form,
            #'owner': owner,
            #'list': list,
            ##'update_table': update_table,
            ##'update_table_filter': update_table_filter,
        #},
    #)

##TODO are you sure you want to delete?
#@login_required
#@require_http_methods(["POST"])
#def delete_selected(request, owner_username):
    #"""
    #delete multiple groups given in post request

    #owner_username is given on the url

    #id2 to delete for the given owner_username
    #are given in request.POST.getlist['id2']

    #if a single owner_username groupname pair does not exist,
    #no deletion is made, and a 404 is returned
    #"""

    #owner = get_object_or_404(User, username=owner_username)

    #if request.user != owner:
        #return HttpResponse(_("you cannot delete a group that belongs to another user")) #TODO decent

    ##first check all id2 exist, then delete them
    ##if one does not exist, 404
    #groups = [ get_object_or_404(List, owner=owner, id2=id2)
            #for id2 in request.POST.getlist('id2') ] 

    #for group in groups:
        #group.delete()

    #return HttpResponseRedirect(reverse(
        #url_add_app('index_user'),
        #args=(owner_username,),
    #))

#def _get_unique_id2(user, id2):
    #"""
    #returns an id2 such that the pair user/id2 is not taken up

    #if no conflict exists for id2, returns the given id2
    
    #else "000_\n+_" preffix is appended to the id2, where \n+ is
    #the first integer starting from 1 that makes the id2 unique
    #"""
    #PREFIX = '000_'
    #SUFFIX = '_'
    #if ( List.objects.filter(
                #owner=user,
                #id2=id2,
            #).exists() ):
        #i=1
        #old_id2 = id2
        #id2 = PREFIX + str(i) + SUFFIX + old_id2
        #while ( List.objects.filter(
                    #owner=user,
                    #id2=id2,
                #).exists() ):
            #i=i+1
            #id2 = PREFIX + str(i) + SUFFIX + old_id2
    #return id2

#@login_required
#@require_http_methods(["POST"])
#def copy_selected(request, owner_username):
    #"""
    #same as delete, but copies the groups from the given owner_username,
    #to the authenticated user.

    #in case of conflict of existing id2,
    #it is resolved by _get_unique_id2
    #"""

    #owner = get_object_or_404(User, username=owner_username)

    #lists = [ get_object_or_404(List, owner=owner, id2=id2)
            #for id2 in request.POST.getlist('id2') ] 

    #for old_list in lists:
        #new_list = List.objects.create(
            #owner=request.user,
            #id2=_get_unique_id2(request.user,old_list.id2)
        #)
        #for user_in_list in Item.objects.filter(list=old_list):
            #user_in_list.pk = None
            #user_in_list.list = new_list
            #user_in_list.save()

    #return HttpResponseRedirect(reverse(
        #url_add_app('index_user'),
        #args=(owner_username,)
    #))

#@login_required
#@require_http_methods(["POST"])
#def bulk_action(request, owner_username):
    #"""
    #decides between bulk actions (actions which may affect several objects at once)
    #such as copy or delete.
    #"""

    #if request.POST.__contains__('copy'):
        #return copy_selected(request,owner_username)
    #if request.POST.__contains__('delete'):
        #return delete_selected(request,owner_username)
    #else:
        #return HttpResponseBadRequest("unknown action" % action)

##if __name__ == "__main__":
    ##quick and dirty tests
    ##import doctest
    ##doctest.testmod()


