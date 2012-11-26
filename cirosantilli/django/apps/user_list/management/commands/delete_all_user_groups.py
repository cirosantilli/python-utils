from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'deletes all Users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            user.delete() #also call delete on choices, default of foreign key!
