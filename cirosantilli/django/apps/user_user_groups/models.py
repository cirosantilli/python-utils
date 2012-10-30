import re
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

MAX_GROUPNAME_LENGTH = 256
VALID_GROUPNAME_RE = r'^[a-z0-9_]+$'


def validate_groupname_chars(groupname):
    if not re.match(VALID_GROUPNAME_RE,groupname):
        raise forms.ValidationError(
                _("groupname \"%s\" contains invalid characters. valid characters are: 'a' to 'z' (lowercase) and underscore '_'."%(groupname))
            )


class UserGroup(models.Model):

    creator = models.ForeignKey(
                User,
                related_name='user_group_creator'
            )

    groupname = models.CharField(
                'group name',
                max_length=MAX_GROUPNAME_LENGTH,
                validators=[
                        validate_groupname_chars,
                    ],
            )

    creation_date = models.DateTimeField(
                'date published',
                default=lambda:datetime.now(),
            )

    def __unicode__(self):
        return self.groupname

    class Meta:
        unique_together = ("creator", "groupname")

class UserInGroup(models.Model):

    user = models.ForeignKey(
                User,
                related_name='user_in_group'
            )

    date_added = models.DateTimeField(
                'date added',
                default=lambda:datetime.now(),
            )

    group = models.ForeignKey(
                UserGroup,
                related_name='group',
            )

    def __unicode__(self):
        return self.user.username
