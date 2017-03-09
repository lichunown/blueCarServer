
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
        for item in self._position:
            result[i] = (self._position[item].lat,self._position[item].lon)
        return result

CarPositions = ObjectPositions()
peoplePositions = ObjectPositions()