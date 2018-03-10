from django.shortcuts import render
from .models import Route
from .routeManage import RouteTypeDicts,RouteNames,addtoDicts
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from m_user.token import userToken
from django.http import HttpResponse
import json

@csrf_exempt
def create(request):
    if request.method =='POST':
        token = request.POST.get('token')
        if userToken.isCar(token):
            user = userToken.getUser(token)
            name = request.POST.get('name')
            type = request.POST.get('type')
            data = request.POST.get('data')
            if len(Route.objects.filter(name=name)):
                return HttpResponse(json.dumps({
                    'action':'createRoute',
                    'result':'error',
                    'errorResult':'nameExist',
                }))
            newRoute = Route()
            newRoute.name = name
            newRoute.createuser = user
            newRoute.type = type
            newRoute.data = data
            newRoute.save()
            addtoDicts(RouteTypeDicts, type, name)
            RouteNames.append(name)
            return HttpResponse(json.dumps({
                'action':'createRoute',
                'result':'succeed',
                'savename':'name',
            }))
        else:
            return HttpResponse(json.dumps({
                'action':'createRoute',
                'result':'error',
                'errorResult':'userLimit',
            }))

@csrf_exempt
def delete(request):
    if request.method =='POST':
        token = request.POST.get('token')
        name = request.POST.get('name')
        user = userToken.getUser(token)
        if len(Route.objects.filter(name=name)):
            route = Route.objects.get(name=name)
            if route.createuser == user:
                route.delete()
                return HttpResponse(json.dumps({
                    'action':'deleteRoute',
                    'result':'succeed',
                }))
            else:
                return HttpResponse(json.dumps({
                    'action':'deleteRoute',
                    'result':'error',
                    'errorResult':'userLimit',
                }))
        else:
            return HttpResponse(json.dumps({
                'action':'deleteRoute',
                'result':'error',
                'errorResult':'nameNotExist',
            }))


@csrf_exempt
def modify(request):
    if request.method =='POST':
        token = request.POST.get('token')
        name = request.POST.get('name')
        user = userToken.getUser(token)
        if len(Route.objects.filter(name=name)):
            route = Route.objects.get(name=name)
            if route.createuser == user:
                data = request.POST.get('data')
                type = request.POST.get('type')
                route.data = data if data else route.data
                route.type = type if type else route.type
                route.save()
                return HttpResponse(json.dumps({
                    'action':'modifyRoute',
                    'result':'succeed',
                }))
            else:
                return HttpResponse(json.dumps({
                    'action':'modifyRoute',
                    'result':'error',
                    'errorResult':'userLimit',
                }))
        else:
            return HttpResponse(json.dumps({
                'action':'modifyRoute',
                'result':'error',
                'errorResult':'nameNotExist',
            }))



@csrf_exempt
def getdata(request):
    if request.method =='POST':
        token = request.POST.get('token')
        name = request.POST.get('name')
        # type = request.POST.get('type')
        if len(Route.objects.filter(username=username)):
            route = Route.objects.get(name=name)
            return HttpResponse(json.dumps({
                'action':'getRouteData',
                'result':'succeed',
                'type':route.type,
                'data':route.data,
            }))
        else:
            return HttpResponse(json.dumps({
                'action':'getRouteData',
                'result':'error',
                'errorResult':'nameNotExist',
            }))





@csrf_exempt
def list(request):
    return HttpResponse(json.dumps({
        'action':'getRouteList',
        'result':'succeed',
        'list':RouteTypeDicts,
    }))