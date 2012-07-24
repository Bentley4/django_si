from django.db import models

class RoTable(models.Model):
    name = models.CharField(max_length = 60)
    number = models.IntegerField(default = 0)

    def __unicode__(self):
       return unicode(self.datetime)


