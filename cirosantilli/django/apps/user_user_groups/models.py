from django.db import models
from django.contrib.auth.models import User,Group

class UserUserGroup(models.Model):

    users_who_voted = models.ManyToManyField(User)
