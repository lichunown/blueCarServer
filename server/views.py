from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    returnData = '''
    Welecome to visit this page.<br><br>
    '''
    if request.method =='POST':
        returnData  += 'You visit here by POST.<br> POSTData:<br>'
        for item in request.POST:
            returnData += item+' : '+request.POST[item]
    if request.method == 'GET':
        returnData  += 'You visit here by GET.<br> GETData:<br>'
        for item in request.GET:
            returnData += item+' : '+request.GET[item]            
    return HttpResponse(returnData)