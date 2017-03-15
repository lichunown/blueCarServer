#encoding:utf-8
from m_user.token import userToken
import time

class Position(object):# Latitude and longitude
    def __init__(self,Latitude=.0,longitude=.0):
        self.lat = Latitude
        self.lon = longitude
        self.time = time.time()

class ObjectPositions(object):
    def __init__(self):
        self._position = {}
        self._CHECKTIMELIMIT = 5
        self._checktime = time.time()
    def changePosition(self,token,lat,lon):
        if userToken.getUser(token):
            self._position[token] = Position(lat,lon)
        else:
            self.removePosition(token)
    def removePosition(self,token):
        try:
            print 'remove ' + token
            return self._position.pop(token)
        except KeyError:
            return None
    def check(self):
        tempposition = self._position.copy()
        for token in tempposition:
            if time.time() - tempposition[token].time >= self._CHECKTIMELIMIT:
                self.removePosition(token)
    def getPositions(self):
        if time.time()-self._checktime>=self._CHECKTIMELIMIT:
            self.check()
        result = [(0,0),]*len(self._position)
        i = 0
        for s_token in self._position:
            result[i] = (self._position[s_token].lat,self._position[s_token].lon)
            i += 1
        return result

class PeoplePositions(ObjectPositions):
    def __init__(self):
        ObjectPositions.__init__(self)
        self._callCarPosition = {}
    def changeCallCarPosition(self,token,lat,lon):
        self._callCarPosition[token] = Position(lat,lon)
    def getCallCarPositons(self):
        result = [(0,0),]*len(self._callCarPosition)
        i = 0
        for s_token in self._callCarPosition:
            result[i] = (self._callCarPosition[s_token].lat,self._callCarPosition[s_token].lon)
            i += 1
        return result



CarPositions = ObjectPositions()
peoplePositions = PeoplePositions()

'''
未验证token是否合法
'''