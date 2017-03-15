import hashlib,random  
import time
# m2 = hashlib.md5()   
# m2.update(src)   
# print m2.hexdigest()  

class Token(object):
    def __init__(self):
        self._loginTokens = {}
        self._md5 = hashlib.md5() 
    def createToken(self,user):
        if self._loginTokens:
            for oldToken in self._loginTokens:
                if self._loginTokens[oldToken] == user:
                    self.dropToken(oldToken)
                    break
        self._md5.update(str(user.username))
        self._loginTokens[str(self._md5.hexdigest())] = (user,time.time())
        return str(self._md5.hexdigest())
    def getUser(self,token):
        data = self._loginTokens.get(str(token))
        if data:
            detime = time.time() - data[1]
            if detime >= 60*60:
                self.dropToken(token)
                return None
            else:
                return data[0]
        return None
    def isCar(self,token):
        user = self.getUser(token)
        if not user:
            return None
        else:
            return bool(int(user.iscar))
    def dropToken(self,token):
        print 'drop '+str(token)
        try:
            user = self._loginTokens.pop(token)[0]
            return user
        except KeyError:
            return None

userToken = Token()