# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

COLLEGES=(
    ('tongxin','通信工程学院'),
    ('dianzi','电子工程学院'),
    ('jisuanji','计算机学院'),
    ('jidian','机电工程学院'),
    ('wuguang','物理与光电工程学院'),
    ('jingguan','经济与管理学院'),
    ('shutong','数学与统计学院'),
    ('renwen','人文学院'),
    ('waiguoyu','外国语学院'),
    ('ruanjian','软件学院'),
    ('weidianzi','微电子学院'),
    ('shengke','生命科学技术学院'),
    ('kongjian','空间科学与技术学院'),
    ('cailiao','先进材料与纳米科技学院'),
    ('wangan','网络与信息安全学院'),
)
ISCARCHOICES = (
    ('0','student'),
    ('1','driver'),
)

class m_User(models.Model):
    username = models.CharField(max_length=50)
    pwd = models.CharField(max_length=33)
    iscar = models.CharField(max_length=1,choices=ISCARCHOICES, default='0')
    college = models.CharField(max_length=20,choices=COLLEGES, blank=True)#need add limit
    studentid = models.CharField(max_length=11,blank=True)
    truename = models.CharField(max_length=20,blank=True)
    def __unicode__(self):
        return smart_unicode(self.username)



# # Create your models here.

# PROJECT_STATUS=(
#     ('1','准备中'),
#     ('2','初期'),
#     ('3','中期'),
#     ('4','后期'),
#     ('5','已结束'),
# )
# INVITATION_STATUS=(
#     ('1','未阅读'),#students send to tutors
#     ('2','已阅读'),#students send to tutors
#     ('3','已接受'),
#     ('4','未接受'),
#     ('a','未阅读'),#student&tutors send to students
#     ('b','已阅读'),
#     ('c','已接受'),
#     ('d','未接受'),
# )
# TAG_CHOICE=(
#     ('gc','国创'),
#     ('yjs','研究生'),
#     ('qt','其他'),
# )
# TITLE_CHOICE=(
#     ('js','教授'),
#     ('fj','副教授'),
#     ('qt','其他'),
# )
# class Student(models.Model):
#     username=models.OneToOneField(User)
#     sid=models.CharField(max_length=11)
#     truename=models.CharField(max_length=50)
#     birthday=models.DateField(timezone.now,blank=True,null=True)
#     college=models.CharField(max_length=50,choices=COLLEGES)#need add limit
#     major=models.CharField(max_length=50,blank=True,null=True)#need add limit
#     introduction=models.TextField(blank=True,null=True)
#     img = models.ImageField(upload_to = 'media/', default = 'media/default/no-img.jpg')
#     def __unicode__(self):
#         return smart_unicode(self.sid)


# class Tutor(models.Model):
#     username=models.OneToOneField(User)
#     truename=models.CharField(max_length=50,blank=True,null=True)
#     jobtitle=models.CharField(max_length=3,choices=TITLE_CHOICE,blank=True,null=True)
#     college=models.CharField(max_length=50,blank=True,choices=COLLEGES)#need add limit
#     introduction=models.TextField(blank=True,null=True)
#     def __unicode__(self):
#         return smart_unicode(self.truename)

# class Project(models.Model):
#     name=models.CharField(max_length=50,blank=True,null=True)
#     status=models.CharField(max_length=10,choices=PROJECT_STATUS)
#     startdate=models.DateField(timezone.now)   
#     students=models.ManyToManyField(Student)
#     tutors=models.ManyToManyField(Tutor,blank=True,null=True)
#     introduction=models.TextField()

#     def __unicode__(self):
#         return smart_unicode(self.name)

# class Invitation(models.Model):
#     student=models.OneToOneField('Student')
#     tutor=models.OneToOneField('Tutor',blank=True,null=True)
#     project=models.OneToOneField('Project')    
#     tag=models.CharField(max_length=3,choices=TAG_CHOICE)
#     status=models.CharField(max_length=10,choices=INVITATION_STATUS)
#     invitetext=models.TextField(blank=True,null=True)


