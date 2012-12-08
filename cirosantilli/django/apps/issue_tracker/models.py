from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

MAX_TITLE_LENGTH = 255
MAX_DESCRIPTION_LENGTH = 2**16-1 #max mysql BLOB TEXT 8kb = 65k
MAX_URI_LENGTH = 2000 #http://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url

class Issue(models.Model):

    creator = models.ForeignKey(
        User,
    )

    uri = models.TextField(
        max_length=MAX_URI_LENGTH,
        help_text='max length: %d chars'%MAX_URI_LENGTH,
    )

    title = models.CharField(
        'title',
        max_length=MAX_TITLE_LENGTH,
        help_text='max length: %d chars'%MAX_TITLE_LENGTH,
    )

    description = models.TextField(
        'description',
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=True,
        help_text='max length: %d chars'%MAX_DESCRIPTION_LENGTH,
    )

    creation_date = models.DateTimeField(
        'created',
        default=lambda:datetime.now(),
    )

    def __unicode__(self):
        return self.pk
