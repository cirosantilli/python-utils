from django.db import models
from django.utils import timezone

import datetime

class Tab0(models.Model):
    r1 = models.CharField(max_length=200)
    r2 = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        #analogous to str(), but unicode
        #str() calls this
        #this output may be printed to end users
        return self.r1

class Tab1(models.Model):
    r1 = models.ForeignKey(Tab0)
    r2 = models.CharField(max_length=200)
    r3 = models.IntegerField()

    def __unicode__(self):
            return self.r2
