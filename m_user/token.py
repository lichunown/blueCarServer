import hashlib,random  

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
        self._loginTokens[str(self._md5.hexdigest())] = user
        return str(self._md5.hexdigest())
    def getUser(self,token):
        return self._loginTokens.get(str(token))
    def isCar(self,token):
        user = self._loginTokens.get(token)
        if not user:
            return None
        else:
            return bool(int(user.iscar))
    def dropToken(self,token):
        print 'drop '+token
        try:
            user = self._loginTokens.pop(token)
            return user
        except KeyError:
            return None

userToken = Token()