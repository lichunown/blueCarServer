from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from positions import CarPositions,peoplePositions
from m_user.token import userToken
from m_user.models import m_User
# Create your views here.



@csrf_exempt
def send(request):
    if request.method=='POST':
        token = request.POST.get('token')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if userToken.isCar(token):
            CarPositions.changePosition(token,latitude,longitude)
            return HttpResponse(json.dumps({
                'action':'send',
                'result':'succeed',
                'position':'CarPositions',
            }))
        else:
            peoplePositions.changePosition(token,latitude,longitude)
            return HttpResponse(json.dumps({
                'action':'send',
                'result':'succeed',
                'position':'peoplePositions',
            }))            

@csrf_exempt
def getcars(request):
    if request.method =='POST':
        token = request.POST.get('token')
        positions = CarPositions.getPositions()
        return HttpResponse(json.dumps({
            'action':'getpeoples',
            'result':'succeed',
            'positions':positions,
        }))

@csrf_exempt
def getpeoples(request):
    if request.method =='POST':
        token = request.POST.get('token')
        positions = peoplePositions.getPositions()
        return HttpResponse(json.dumps({
            'action':'getpeoples',
            'result':'succeed',
            'positions':positions,
        }))
