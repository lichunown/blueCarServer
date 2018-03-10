import hashlib,random  
import time

# m2 = hashlib.md5()   
# m2.update(src)   
# print m2.hexdigest()  

class Token(object):
    def __init__(self):
        self._loginTokens = {}
        self._md5 = hashlib.md5() 
        self.MAXTIME = 24*60*60
    def createToken(self,user):
        if self._loginTokens:
            for oldToken in self._loginTokens:
                if self._loginTokens[oldToken] == user:
                    self.dropToken(oldToken)
                    break
        self._md5.update(str(user.username))
        token = str(self._md5.hexdigest())
        self._loginTokens[token] = (user,time.time())
        return token

    def getUser(self,token):
        data = self._loginTokens.get(token)
        if data:
            detime = time.time() - data[1]
            if detime >= self.MAXTIME:
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
        print('drop '+str(token)) 
        try:
            user = self._loginTokens.pop(token)[0]
            return user
        except KeyError:
            return None

    def exists(self,token):
        return True if self.getUser(token) is not None else False
userToken = Token()