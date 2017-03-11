
class Position(object):# Latitude and longitude
    def __init__(self,Latitude=.0,longitude=.0):
        self.lat = Latitude
        self.lon = longitude

class ObjectPositions(object):
    def __init__(self):
        self._position = {}
    def addPosition(self,token,lat,lon):
        self._position[token] = Position(lat,lon)
    def changePosition(self,token,lat,lon):
        self._position[token] = Position(lat,lon)
    def removePosition(token):
        try:
            return self._position.pop(token)
        except KeyError:
            return None
    def getPositions(self):
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