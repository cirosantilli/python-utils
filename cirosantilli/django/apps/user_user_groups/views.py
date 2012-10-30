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

SUCCESS_REDIRECT = 'user_user_groups_index'

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
            widget=FilteredSelectMultiple("users", is_stacked=False, attrs={'rows':'10'})
        )

    def __init__(self, *args, **kwargs):
        """
        may be called with or without creator.

        if no creator is given, unicity check does nothing: it is the initial GET request.
        """
        self.creator = kwargs.pop('creator',None)
        super(UserGroupForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserGroupForm, self).clean()
        if self.creator:
            groupname = cleaned_data['groupname']
            if UserGroup.objects.filter(creator=self.creator,groupname=groupname).exists():
                self._errors['groupname'] = [_(
                        "groupname %s already exists for user %s. "
                        "please choose a different groupname."
                        %(groupname,self.creator.username)
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
            return HttpResponseRedirect(reverse(SUCCESS_REDIRECT,args=(username,)))
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
        form = UserGroupForm(request.POST, creator=creator)
        if form.is_valid():
            old_users = usergroup.useringroup_set.all()
            new_users = form.cleaned_data['users']
            for user in new_users: #add new ones
                if not user in current_users:
                    user_in_group = UserInGroup.objects.create(
                            user=user,
                            group=group,
                        )
            for user in old_users: #delete removed ones
                if not user in new_users:
                    user.delete()
            return HttpResponseRedirect(reverse(SUCCESS_REDIRECT,args=(username,)))
    else:
        #form = UserGroupForm(initial=) #TODO 2 get useringroup in! search querriset to dict google
        form = UserGroupForm()

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

    return HttpResponseRedirect(reverse(SUCCESS_REDIRECT,args=(username,)))
