
from bs4 import BeautifulSoup
import re,time,sys
import codecs
import urllib2,os,json,urllib
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
headers = { 'User-Agent' : user_agent }

def getPage(url,post = None,decode = 'UTF-8'):
    try:
        if post:
            post = urllib.urlencode(post)
            request = urllib2.Request(url, headers=headers,data = post)
            #print post
        else:
            request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        return response.read().decode(decode)
    except Exception,e:
        print 'GET Page: %s error : %s ' % (url,e)

URL = 'http://127.0.0.1:8000/'

def getToken(data):
    data = json.loads(data)
    return data['token']

def signup(username,password):
    return getPage(URL+'user/signup',{
        'username':username,
        'password':password,
    })
    
def login(username,password):
    return getPage(URL+'user/login',{
        'username':username,
        'password':password,
    })

def logout(token):
    return getPage(URL+'user/logout',{
        'token':token,
    })

def modify(token,modifyData):
    return getPage(URL+'user/logout',{
        'token':token,
        'modifydata':json.dumps(modifyData),
    })

def getdata(username,token=None):
    data = {
        'getdatausername':username,
    }
    if token:
        data['token'] = token
    return getPage(URL+'user/logout',data)


class User(object):
    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password
        self.token = None
        self.data = None
        self.situation = [0,0]
    def signup(self):
        return getPage(URL+'user/signup',{
            'username':self.username,
            'password':self.password,
        })        

    def login(self):
        result = getPage(URL+'user/login',{
            'username':self.username,
            'password':self.password,
        })
        result = json.loads(result)
        if result['result'] == 'succeed':
            self.token = result['token']
            return True
        else:
            return False

    def logout(self):
        return getPage(URL+'user/logout',{
            'token':self.token,
        })
    def getdata(self,username=None):
        if not username:
            getdatausername = self.username
            result = getPage(URL+'user/getdata',{
                'token':self.token,
                'getdatausername':getdatausername,
            })
            result = json.loads(result)
            if result['result'] =='succeed':
                self.data = result['data']
            return result
        else:
            getdatausername = username
            return getPage(URL+'user/getdata',{
                'token':self.token,
                'getdatausername':getdatausername,
            })
    def modify(self):
        return getPage(URL+'user/modify',{
            'token':self.token,
            'modifydata':json.dumps(self.data),
        })        
    def send(self):
        return getPage(URL+'station/send',{
            'token':self.token,
            'latitude':self.situation[0],
            'longitude':self.situation[1],
        }) 
    def getcars(self):
        return getPage(URL+'station/getcars',{
            'token':self.token,
        }) 
    def getpeoples(self):
        return getPage(URL+'station/getcars',{
            'token':self.token,
    }) 