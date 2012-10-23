from datetime import datetime
from optparse import make_option
import itertools

from django.core.management.base import BaseCommand, CommandError

from polls.models import Poll, Choice

class Command(BaseCommand):
    help = 'makes a bunch of test polls'

    def handle(self, *args, **options):

        npolls = 10
        choices_per_poll = 5

        now = datetime.now()
        polls = [ Poll.objects.create(question='question%d' % i, pub_date=now) for i in xrange(npolls) ]
        
        for i,j in itertools.product(xrange(npolls),xrange(choices_per_poll)):
            Choice.objects.create(poll=polls[i], choice_text="choice%d" % j, votes=0)
