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
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from user_user_groups.models import UserGroup, UserInGroup

ITEMS_PER_PAGE = 100

def index(request, username):
    creator = get_object_or_404(User,username=username)
    items_list = UserGroup.objects.filter(creator=creator)
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
                    'items': items
                }
            )

def detail(request, username, groupname):
    creator = get_object_or_404(User, username=username)
    usergroup = get_object_or_404(UserGroup, creator=creator, groupname=groupname)
    return render(
                request,
                'user_user_groups/detail.html',
                {
                    'creator': creator,
                    'usergroup': usergroup,
                },
            )

#TODO 0 add help
class UserGroupForm(ModelForm):

    users = forms.ModelMultipleChoiceField(
            queryset=User.objects.all(),
            widget=FilteredSelectMultiple(
                    "users",
                    is_stacked=False,
                    attrs={'rows':'10'},
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
            new_groupname = cleaned_data['groupname']
            if UserGroup.objects.filter(
                            creator=self.creator,
                            groupname=new_groupname
                        ).exists(): #new name exists: might be error
                error = False
                if( (self.old_groupname and self.old_groupname != new_groupname ) #update, and name different from old. error
                        or not self.old_groupname ): #create and new name exists. error
                    self._errors['groupname'] = [_(
                            "groupname %s already exists for user %s. "
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
        form = UserGroupForm(initial_usergroup=usergroup) #TODO 2 get useringroup in! search querriset to dict google

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
#TODO return 404
@login_required
def delete(request, username, groupname):

    creator = get_object_or_404(User, username=username)
    usergroup = get_object_or_404(UserGroup, creator=creator, groupname=groupname)

    if request.user != creator:
        return HttpResponse(_("you cannot delete a group that belongs to another user!")) #TODO decent

    if request.method != "POST": #TODO use delete
        return HttpResponse(_('deleting must be done via an empty POST request')) #TODO decent

    usergroup.delete()

    return HttpResponseRedirect(reverse('user_user_groups_index',args=(username,)))
