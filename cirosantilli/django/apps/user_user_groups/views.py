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

from user_user_groups.models import UserGroup, UserInGroup

ITEMS_PER_PAGE = 100

@require_safe
def index(request, username):

    table = {
            'id':'grouptable',
            'filter_global':True,
        }

    creator = get_object_or_404(User,username=username)
    items_list = UserGroup.objects.filter(creator=creator).order_by('groupname')
    paginator = Paginator(items_list, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(
                request,
                'user_user_groups/index.html',
                {
                    'creator': creator,
                    'items': items,
                    'table': table,
                }
            )

@require_safe
def detail(request, username, groupname):
    creator = get_object_or_404(User, username=username)
    usergroup = get_object_or_404(UserGroup, creator=creator, groupname=groupname)
    usersingroup = UserInGroup.objects.filter(group=usergroup).order_by('user__username')
    return render(
                request,
                'user_user_groups/detail.html',
                {
                    'creator': creator,
                    'usergroup': usergroup,
                    'usersingroup': usersingroup,
                },
            )

#TODO 0 add help
class UserGroupForm(ModelForm):

    users = forms.ModelMultipleChoiceField(
            queryset=User.objects.all(),
            widget=SelectMultiple(
                    attrs={
                        'rows':'10',
                        'class':'jquery-ui-autocomplete',
                        }
                )
        )

    def __init__(self, *args, **kwargs):
        """
        #kwargs

        - creator
            Auth.User object

            if no creator is given, unicity check does nothing:
            it is probably the initial GET request.

            rationale: without a creator, one cannot know if the
            groupname/username pair is unique.

        - initial_usergroup
            UserGroup object

            loads form with given UserGroup object.

            if given, dictionnary *arg is ignored,
            just like it is if a ModelForm is given a initial
            kwarg

            if 'initial' is given with initial_usergroup, its values are considered
            'initial' dictionnary value pairs have precedence over
            those extracted in initial_usergroup.

        - old_groupname
            String

            if given supposes it is an update of old_groupname.
            therefore, in that case, will only raise an unicity check error
            it then new username/groupname is already taken and if the
            new groupaname is different from the old one, meaning that the
            user is trying to update the name to a new one.
        """

        self.creator = kwargs.pop('creator',None)
        self.old_groupname = kwargs.pop('old_groupname',None)

        #update initial values based on model
        initial_usergroup = kwargs.pop('initial_usergroup',None)
        if initial_usergroup: 
            old_initial = kwargs.get('initial',{})
            kwargs['initial'] = {}
            kwargs['initial'].update(model_to_dict(initial_usergroup,fields=['groupname']))
            kwargs['initial']['users'] = [
                    useringroup.user.pk for useringroup in initial_usergroup.useringroup_set.all()
                ]
            kwargs['initial'].update(old_initial)

        super(UserGroupForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        ensure creator/groupname pair is unique taking into consideration update
        """
        cleaned_data = super(UserGroupForm, self).clean()
        if self.creator: #POST
            new_groupname = cleaned_data.get('groupname',None) #because is_valid calls clean first, before passing it to the model for field validation
            if new_groupname:
                if UserGroup.objects.filter(
                                creator=self.creator,
                                groupname=new_groupname
                            ).exists(): #new name exists: might be error
                    error = False
                    if( (self.old_groupname and self.old_groupname != new_groupname ) #update, and name different from old. error
                            or not self.old_groupname ): #create and new name exists. error
                        self._errors['groupname'] = [_(
                                "groupname \"%s\" already exists for user \"%s\". "
                                "please choose a different groupname."
                                %(new_groupname,self.creator.username)
                            )]
        return cleaned_data

    class Meta:
        model = UserGroup
        fields = (
                'groupname',
            )

#TODO 0 confirm before exiting create!
#TODO 1 add nice admin search widget
@require_http_methods(["GET","HEAD","POST"])
@login_required
def create(request, username):

    creator = get_object_or_404(User, username=username)

    if request.user != creator:
        return HttpResponse(_(
                "you are logged in as \"%s\" "
                "and cannot create a group for user \"%s\""
                % (request.user.username, creator.username)
            ))

    if request.method == "POST":
        form = UserGroupForm(request.POST, creator=creator)
        if form.is_valid():
            groupname = form.cleaned_data['groupname']
            group = UserGroup.objects.create(
                    groupname=groupname,
                    creator=creator,
                )
            for user in form.cleaned_data['users']:
                user_in_group = UserInGroup.objects.create(
                        user=user,
                        group=group,
                    )
            return HttpResponseRedirect(reverse('user_user_groups_index',args=(username,)))
    else:
        form = UserGroupForm()

    return render(
            request,
            "user_user_groups/create_usergroup.html",
            {
                "form": form,
                "creator": creator,
            },
        )

@require_http_methods(["GET","POST"])
@login_required
def update(request, username, groupname):

    creator = get_object_or_404(User, username=username)
    usergroup = get_object_or_404(UserGroup, creator=creator, groupname=groupname)

    if request.user != creator:
        return HttpResponse(_(
                "you are logged in as \"%s\" "
                "and cannot update a group for user \"%s\""
                % (request.user.username, creator.username)
            ))

    if request.method == "POST":
        form = UserGroupForm(request.POST, creator=creator, old_groupname=usergroup.groupname)
        if form.is_valid():

            #update name
            old_name = usergroup.groupname
            new_name = form.cleaned_data['groupname']
            if new_name != old_name: #validation already guarantees new name is available
                usergroup.groupname = new_name
                usergroup.save()

            #update users
            old_users = usergroup.useringroup_set.all()
            new_users = form.cleaned_data['users']
            for user in new_users: #add new ones
                if not user in old_users:
                    user_in_group = UserInGroup.objects.create(
                            user=user,
                            group=usergroup,
                        )
            for user in old_users: #delete removed ones
                if not user in new_users:
                    user.delete()
            return HttpResponseRedirect(
                    reverse('user_user_groups_detail',
                    args=(username,usergroup.groupname))
                )
    else:
        form = UserGroupForm(initial_usergroup=usergroup)

    return render(
            request,
            "user_user_groups/update_usergroup.html",
            {
                "form": form,
                "creator": creator,
                "usergroup": usergroup,
            },
        )

#TODO are you sure you want to delete?
@login_required
@require_http_methods(["POST"])
def delete(request, username):
    """
    delete multiple groups given in post request

    username is given on the url

    groupnames to delete for the given username
    are given in request.POST.getlist['groupnames']

    if a single username groupname pair does not exist,
    no deletion is made, and a 404 is returned
    """

    creator = get_object_or_404(User, username=username)

    if request.user != creator:
        return HttpResponse(_("you cannot delete a group that belongs to another user")) #TODO decent

    #first check all groupnames exist, then delete them
    #if one does not exist, 404
    groups = [ get_object_or_404(UserGroup, creator=creator, groupname=groupname)
            for groupname in request.POST.getlist('groupnames') ] 

    for group in groups:
        group.delete()

    return HttpResponseRedirect(reverse('user_user_groups_index',args=(username,)))

def _get_unique_groupname(user, groupname):
    """
    returns an groupname such that the pair user/groupname is not taken up

    if no conflict exists for groupname, returns the given groupname
    
    else "000_\n+_" preffix is appended to the groupname, where \n+ is
    the first integer starting from 1 that makes the groupname unique
    """
    PREFIX = '000_'
    SUFFIX = '_'
    if ( UserGroup.objects.filter(
                    creator=user,
                    groupname=groupname,
                ).exists() ):
        i=1
        old_groupname = groupname
        groupname = PREFIX + str(i) + SUFFIX + old_groupname
        while ( UserGroup.objects.filter(
                    creator=user,
                    groupname=groupname,
                    ).exists() ):
            i=i+1
            groupname = PREFIX + str(i) + SUFFIX + old_groupname
    return groupname

@login_required
@require_http_methods(["POST"])
def copy(request, username):
    """
    same as delete, but copies the groups from the given username,
    to the authenticated user.

    in case of conflict of existing groupname,
    it is resolved by _get_unique_groupname
    """

    creator = get_object_or_404(User, username=username)

    groups = [ get_object_or_404(UserGroup, creator=creator, groupname=groupname)
            for groupname in request.POST.getlist('groupnames') ] 

    for old_group in groups:
        new_group = UserGroup.objects.create(
                creator=request.user,
                groupname=_get_unique_groupname(request.user,old_group.groupname)
            )
        for user_in_group in UserInGroup.objects.filter(group=old_group):
            user_in_group.pk = None
            user_in_group.group = new_group
            user_in_group.save()

    return HttpResponseRedirect(reverse('user_user_groups_index',args=(username,)))

@login_required
@require_http_methods(["POST"])
def bulk_action(request, username):
    """
    decides between bulk actions (actions which may affect several objects at once)
    such as copy or delete.
    """

    if request.POST.__contains__('copy'):
        return copy(request,username)
    if request.POST.__contains__('delete'):
        return delete(request,username)
    else:
        return HttpResponseBadRequest("unknown action" % action)
        
