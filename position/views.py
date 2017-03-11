from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from positions import CarPositions,peoplePositions
from m_user.token import userToken
from m_user.models import m_User
from .models import SavePosition
from django.utils import timezone
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


@csrf_exempt
def callcar(request):
    if request.method=='POST':
        token = request.POST.get('token')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if token:
            peoplePositions.changeCallCarPosition(token,latitude,longitude)
            return HttpResponse(json.dumps({
                'action':'callcar',
                'result':'succeed',
            }))
        else:
            return HttpResponse(json.dumps({
                'action':'callcar',
                'result':'error',
                'errorResult':'tokenDoNotExist',
            }))            
    

@csrf_exempt
def getcallcarpeoples(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
            positions = peoplePositions.getCallCarPositons()
            return HttpResponse(json.dumps({
                'action':'getcallcarpeoples',
                'result':'succeed',
                'positions':positions,
            }))            
        else:
            return HttpResponse(json.dumps({
                'action':'getcallcarpeoples',
                'result':'error',
                'errorResult':'UserDoNotExist',
            }))       

@csrf_exempt
def saveposition(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if not user:
            return HttpResponse(json.dumps({
                'action':'saveposition',
                'result':'error',
                'errorResult':'UserDoNotExist',
            }))      
        else:
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            tag = request.POST.get('tag')            
            position = SavePosition()
            position.user = user
            position.latitude = latitude
            position.longitude = longitude
            position.tag = tag
            position.save()
            return HttpResponse(json.dumps({
                'action':'saveposition',
                'result':'succeed',
            }))              

@csrf_exempt
def getpositions(request):
    if request.method=='POST':
        token = request.POST.get('token')
        getuser = request.POST.get('getuser')
        user = userToken.getUser(token)
        if not user:
            return HttpResponse(json.dumps({
                'action':'getposition',
                'result':'error',
                'errorResult':'UserDoNotExist',
            })) 
        if not getuser:
            getuser = user.username
        if user.username == getuser:# User it self
            positions = []
            tag = request.POST.get('tag')
            if tag:
                posData = user.SavePosition.filter(tag=tag)
            else:
                posData = user.SavePosition.all()            
            for pos in posData:
                positions.append({
                        'latitude':pos.latitude,
                        'longitude':pos.longitude,
                        'tag':pos.tag,
                        'time':str(pos.time),
                    })
            return HttpResponse(json.dumps({
                'action':'getposition',
                'result':'succeed',
                'positions':positions,
            }))   
        else:
            return HttpResponse(json.dumps({
                'action':'getposition',
                'result':'error',
                'errorResult':'CanNotGetOthersData',
            }))                  
