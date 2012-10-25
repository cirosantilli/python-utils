from itertools import count

from datetime import datetime
from optparse import make_option
from django.contrib.auth.models import User, Permission

from django.core.management.base import BaseCommand, CommandError

from polls.models import Poll, Choice
from accounts.models import Profile

class Command(BaseCommand):
    args = '[<nusers>]'
    help = 'makes test users. default: 10'

    def handle(self, nusers=10, *args, **options):

        users = []

        u = User.objects.create_user("admin","admin@mail.com","pass")
        u.is_superuser=True
        u.is_staff=True
        u.save()
        users.append(u)

        for i in xrange(nusers):
            u = User.objects.create_user("user%d"%i,"user%d@mail.com"%i,"pass")
            u.user_permissions.add(Permission.objects.get(codename='can_vote'))
            u.save()
            users.append(u)
        print users

        for i,user in zip(count(),users):
            Profile.objects.create(user=user,favourite_snack="snack%d"%i)
            print i

        self.stderr.write("created one superuser and %d regular users" % (nusers))
