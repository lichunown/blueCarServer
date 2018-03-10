from django.db import models
from m_user.models import m_User
# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=30,blank=True,default=None)
    createuser = models.ForeignKey(m_User,related_name='Route')
    data = models.TextField(blank=True,default=None)
    type = models.CharField(max_length=50,blank=True,default=None)