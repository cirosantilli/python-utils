from itertools import count
import random

from datetime import datetime
from optparse import make_option
from django.contrib.auth.models import User, Permission

from django.core.management.base import BaseCommand, CommandError

from user_list_uri.models import List, Item
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '[<item2_per_user> [<item3_per_item2>]]'
    help = 'makes test user groups. default: 3 groups per user, 3 users per group'

    def handle(self, item2_per_user=3, item3_per_item2=3, *args, **options):

        owners = User.objects.all()
        for owner in owners:
            for i in xrange(item2_per_user):
                list = List.objects.create(
                    owner=owner,
                    id2="id%d"%i,
                    description="desc%d"%i,
                )
                for i in xrange(item3_per_item2):
                    Item.objects.create(
                        list=list,
                        uri="uri%d"%i,
                    )

        self.stderr.write(
            "created %d item2 per user with %d item3 per item2"
            % (item2_per_user, item3_per_item2)
        )
