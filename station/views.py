from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from stations import CarStations,peopleStations
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
            CarStations.changeStation(token,latitude,longitude)
            return HttpResponse(json.dumps({
                'action':'send',
                'result':'succeed',
                'station':'CarStations',
            }))
        else:
            peopleStations.changeStation(token,latitude,longitude)
            return HttpResponse(json.dumps({
                'action':'send',
                'result':'succeed',
                'station':'peopleStations',
            }))            

@csrf_exempt
def getcars(request):
    if request.method =='POST':
        token = request.POST.get('token')
        stations = CarStations.getStations()
        return HttpResponse(json.dumps({
            'action':'getpeoples',
            'result':'succeed',
            'stations':stations,
        }))

@csrf_exempt
def getpeoples(request):
    if request.method =='POST':
        token = request.POST.get('token')
        stations = peopleStations.getStations()
        return HttpResponse(json.dumps({
            'action':'getpeoples',
            'result':'succeed',
            'stations':stations,
        }))
