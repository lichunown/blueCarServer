
class Station(object):# Latitude and longitude
    def __init__(self,Latitude=.0,longitude=.0):
        self.lat = Latitude
        self.lon = longitude

class ObjectStations(object):
    def __init__(self):
        self._station = {}
    def addStation(self,token,lat,lon):
        self._station[token] = Station(lat,lon)
    def changeStation(self,token,lat,lon):
        self._station[token] = Station(lat,lon)
    def removeStation(token):
        try:
            return self._station.pop(token)
        except KeyError:
            return None
    def getStations(self):
        result = [(0,0),]*len(self._station)
        i = 0
        for item in self._station:
            result[i] = (self._station[item].lat,self._station[item].lon)
        return result

CarStations = ObjectStations()
peopleStations = ObjectStations()