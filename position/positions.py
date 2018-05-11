#encoding:utf-8
from m_user.token import userToken
import time
from collections import deque

'''
class Status(object):
    def __init__(self,status, latitude = 0, longitude = 0, time = None, speed = None):
        self.status = status
        self.latitude = latitude
        self.longitude = longitudes
        self.time = time
        self.speed = speed
    def dict(self):
        return self.__dict__

CARSTATUS = [
    'run',
    'stop',
    'pause',
    'start',
]
PEOPLESTATUS = [
    'non',
    'call',
]

class Obj(object):
    def __init__(self):
        self.status = deque(10)
    def addStatus(self,status):
        self.status.append(status)

class Car(Obj):
    def __init__(self):
        super(Car,self).__init__()

class People(Obj):
    def __init__(self):
        super(People,self).__init__()



'''
CARSTATUS = [
    'run',
    'stop',
    'pause',
    'start',
]
PEOPLESTATUS = [
    'non',
    'call',
    'dst',
]


class Position(object):# Latitude and longitude
    def __init__(self,Latitude=.0,longitude=.0,time = None,status = None):
        self.latitude = Latitude
        self.longitude = longitude
        self.time = time
        self.status = status

class ObjectPositions(object):
    def __init__(self):
        self._route = {}
        self._CHECKTIMELIMIT = 60*60
        self._DEQUELIMIT = 5
        self._checktime = time.time()
    def changePosition(self,route,token,lat,lon,time = None,status = None):
        if userToken.exists(token):
            if not self._route.get(route):
                self._route[route] = {}
            position = self._route[route]
            if not position.get(token):
                position[token] = deque(maxlen = self._DEQUELIMIT)
            position[token].append(Position(lat,lon,time,status)) 
        else:
            self.removePosition(route, token)

    def removePosition(self,route,token):
        try:
            print 'remove ' + token
            return self._route[route].pop(token)
        except KeyError:
            return None

    def check(self,route = None):
        for route in self._route:
            tempposition = self._route[route].copy()
            for token in tempposition:
                if time.time() - tempposition[token][-1].time >= self._CHECKTIMELIMIT:
                    self.removePosition(route,token)

    def getPositions(self,route):
        if time.time() - self._checktime > self._CHECKTIMELIMIT:
            self.check(route)
        if self._route.get(route):
            return [ self._route[route][token][-1].__dict__ for token in self._route[route] ]
        else:
            return []

    def getAllPositions(self,route):
        if time.time() - self._checktime > self._CHECKTIMELIMIT:
            self.check(route)
        # return [ pos.__dict__ for pos in self._route[route][token] for token in self._route[route] ]
        result = []
        for token in self._route[route]:
            result.extend([ pos.__dict__ for pos in self._route[route][token] ])
        return result

class PeoplePositions(ObjectPositions):
    def __init__(self):
        super(PeoplePositions,self).__init__()
        self._callCarPosition = {}
    # def changeCallCarPosition(self,token,lat,lon):
    #     self._callCarPosition[token] = Position(lat,lon)
    def getCallCarPositons(self,route):
        return list(filter(lambda x: x != None, [ self._route[route][token][-1].__dict__ \
            if self._route[route][token][-1].__dict__['status'] == 'call' or self._route[route][token][-1].__dict__['status'] == 'dst' else None \
            for token in self._route[route] ]))



CarPositions = ObjectPositions()
peoplePositions = PeoplePositions()

