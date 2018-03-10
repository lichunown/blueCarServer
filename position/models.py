from django.db import models
from m_user.models import m_User
from django.utils import timezone
from django.utils.encoding import smart_unicode
# Create your models here.

CARSTATUS = (
    ('run','run'),
    ('stop','stop'),
    ('pause','pause'),
    ('start','start'),
)

# class CallCarPosition(models.Model):
#     user = models.ForeignKey(m_User,default=None,related_name='CallCarPosition')
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     time = models.DateTimeField(default=timezone.now)


class SavePosition(models.Model):
    user = models.ForeignKey(m_User,default=None,related_name='SavePosition')
    latitude = models.FloatField()
    longitude = models.FloatField()
    tag = models.CharField(max_length = 10,default=None,blank=True,null=True)
    time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return smart_unicode(self.time)