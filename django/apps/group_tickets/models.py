from django.db import models
from django.contrib.auth.models import User,Group

from django.utils import timezone

import datetime


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
            return self.choice_text
