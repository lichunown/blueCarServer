import hashlib,random  

# m2 = hashlib.md5()   
# m2.update(src)   
# print m2.hexdigest()  

class Token(object):
    def __init__(self):
        self._loginTokens = {}
        self._md5 = hashlib.md5() 
    def createToken(self,username):
        self._md5.update(str(username)+str(int(random.random()*10000)))
        self._loginTokens[str(self._md5.hexdigest())] = username
        return str(self._md5.hexdigest())
    def getUsername(self,md5):
        return self._loginTokens.get(str(md5))
    def dropToken(self,token):
        try:
            username = self._loginTokens.pop(token)
            return username
        except KeyError:
            return None

userToken = Token()