from itertools import count
import random

from datetime import datetime
from optparse import make_option
from django.contrib.auth.models import User, Permission

from django.core.management.base import BaseCommand, CommandError

from user_user_groups.models import UserGroup, UserInGroup
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '[<groups_per_user> [<users_per_groups>]]'
    help = 'makes test user groups. default: 3 groups per user, 3 users per group'

    def handle(self, groups_per_user=3, users_per_group=3, *args, **options):

        users = User.objects.all()
        for creator in users:
            for i in xrange(groups_per_user):
                group = UserGroup.objects.create(
                        creator=creator,
                        groupname="group%d"%i
                    )
                for user in random.sample(users, users_per_group):
                    user_in_group = UserInGroup.objects.create(
                            user=user,
                            group=group,
                        )
                    group.group.add(user_in_group)

        self.stderr.write(
                "created %d groups per user with %d users per group"
                % (groups_per_user, users_per_group)
                )
