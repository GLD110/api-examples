#! /usr/bin/python3

import settings
import json

class Calls(object):
    """Calls class"""

    def __init__(self, id=""):
       self.id = id

    def getCalls(self):
        r = settings.s.get(settings.url+'/calls')
        print(r.json()) if r.status_code == 200 else print("Error : {}".format(r.json()))

    def getCallsByTag(self, tags=[]):
        tags = {'tags': tags} if isinstance(tags, list) else {'tags': [tags]}
        r = settings.s.get(settings.url+'/calls/search', params=tags)
        print(r.json()) if r.status_code == 200 else print("Error : {}".format(r.text))

    def getCall(self, id=None, fr="", to=""):
        params = {'from':fr, 'to':to}
        if id != None:
            r = settings.s.get(settings.url+'/calls/'+id)
            if r.status_code == 200:
                call = r.json()
                call = call["call"]
                self.id = call["id"]
                print("Success : {}".format(call))
            else:
                print("Error : {}".format(r.json()))
        else:
            r = settings.s.get(settings.url+'/calls?', params=params)
            if r.status_code == 200:
                print(r.json())
            else:
                print("Error : {}".format(r.text))

    def setCallLink(self, link):
        r = settings.s.post(settings.url+'/calls/'+str(self.id)+'/link?link='+link)
        print("Success") if r.status_code == 200 else print("Error")
        print(r.text)
        print(r.url)
        print(r.status_code)

    def transferCall(self, user_id):
        params = {'user_id': user_id}
        r = settings.s.post(settings.url+'/calls/'+str(self.id)+'/transfers', params=params)
        if r.status_code == 204:
            print("Success")
        elif r.status_code == 400:
            print("Error : Call ended")
        elif r.status_code == 404:
            print("Error : User not found or Call not found")
        else:
            print("Error")
        print(r.text)

    def deleteRecording(self):
        r = settings.s.delete(settings.url+'/calls/'+str(self.id)+'/recording')
        print("Success") if r.status_code == 200 esle print("Error : {}".format(r.json()))
        
    def deleteVoicemail(self):
        r = settings.s.delete(settings.url+'/calls/'+str(self.id)+'/voicemail')
        print("Success") if r.status_code == 200 else print("Error : {}".format(r.text))
