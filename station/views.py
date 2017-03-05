from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from stations import CarStations,peopleStations
from m_user.token import userToken
from m_user.models import m_User
# Create your views here.
def send(request):
    pass

def getcars(request):
    pass

def getpeoples(request):
    pass