from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),

    # url(r'^accounts/signin$',views.signin,name='signin'),
    # url(r'^accounts/signout$',views.signout,name='signout'),
    # url(r'^accounts/signup$',views.signup2,name='signup'),
    # url(r'^accounts/modify$',views.modifyaccount,name='modifyaccount'),

    # url(r'^tutors/page/(?P<page>[0-9]+)/$',views.showtutors,name='showtutors'),
    # url(r'^tutors/(?P<id>[0-9]+)/$',views.showtutor,name='showtutor'),

    # url(r'^projects/page/(?P<page>[0-9]+)/$',views.showprojects,name='showprojects'),
    # url(r'^projects/(?P<id>[0-9]+)$',views.showproject,name='showproject'),
    # url(r'^projects/create/$',views.createproject,name='createproject'),

    # url(r'^students/(?P<id>[0-9]+)/$',views.showstudent,name='showstudent'),

    # url(r'^invite/tutor/$',views.invitetutor,name='invitetutor'),
    # url(r'^invite/student/$',views.invitestudent,name='invitestudent'),
    url(r'send$',views.send,name='send'),
    url(r'getcars$',views.getcars,name='getcars'),
    url(r'getpeoples$',views.getpeoples,name='getpeoples'),
    url(r'callcar$',views.callcar,name='callcar'),
    url(r'getcallcarpeoples$',views.getcallcarpeoples,name='getcallcarpeoples'),
    url(r'saveposition$',views.saveposition,name='saveposition'),
    url(r'getpositions$',views.getpositions,name='getpositions'),
]
