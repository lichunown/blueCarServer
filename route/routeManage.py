from .models import Route


def addtoDicts(dicts,str_type,name):
    temp = dicts
    names = str_type.split('|')
    for name in names[:-1]:
        if not temp.get(name):
            temp[name] = {}
        temp = temp[name]
    temp[names[-1]] = name

def initList():
    dicts = {}
    names = []
    for route in Route.objects.all():
        addtoDicts(dicts, route.type, route.name)
        names.append(route.name)
    print(names)
    return dicts,names

RouteTypeDicts,RouteNames = initList()