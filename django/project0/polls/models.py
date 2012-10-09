from django.db import models
from django.utils import timezone

import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date' #if clicks on this, sorts by r2 instead (gives the same thing, but sort by function is not supported)
    was_published_recently.boolean = True #treats output as boolean, and prints nice output to end user
    was_published_recently.short_description = 'Published recently?' #title that will to to admin colum

    def __unicode__(self):
        #analogous to str(), but unicode
        #str() calls this
        #this output may be printed to end users
        return self.question

    class Meta:
            permissions = (
                ("vote", "Can see available tasks"),
                ("view_results", "Can see available tasks"),
            )

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
            return self.choice_text
