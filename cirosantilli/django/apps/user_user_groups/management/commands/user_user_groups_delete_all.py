from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from user_user_groups import UserGroup

class Command(BaseCommand):
    help = 'deletes all lists and their items'

    def handle(self, *args, **options):
        for usergroup in UserGroup.objects.all():
            usergroup.delete()
