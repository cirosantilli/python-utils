from django.db import models

class Tab0(models.Model):
    r1 = models.CharField(max_length=200)
    r2 = models.DateTimeField('date published')

    #analogous to str(), but unicode
    #str() calls this
    #this output may be printed to end users
    def __unicode__(self):
            return self.r1

class Tab1(models.Model):
    r1 = models.ForeignKey(Tab0)
    r2 = models.CharField(max_length=200)
    r3 = models.IntegerField()

    def __unicode__(self):
            return self.r2
