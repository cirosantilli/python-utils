from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):

    user = models.OneToOneField(
            User,
            unique=True,
            verbose_name=_('user'),
            related_name='profile',
            )

    favourite_snack = models.CharField(
            verbose_name=_('favourite snack'),
            max_length=32,
            )

    class Meta:
            permissions = (
                ("is_member", "is member"),
            )
