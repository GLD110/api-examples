#! /usr/bin/python3

import settings
import json

class User(object):
    def __init__(self, name="", email="", availability_status='available', numbers=[]):
        self.name = name
        self.email = email
        self.availability_status = availability_status
        self.numbers = numbers

    def getUsers(self):
        r = settings.s.get(settings.url+'/users')
        if r.status_code == 200:
            print("Success")
        else:
            print("Error")
        print(r.json())

    def getUser(self, id):
        r = settings.s.get(settings.url+'/users/'+id)
        if r.status_code == 200:
            user = r.json()
            user = user["user"]
            self.__init__(user["name"], user["email"], user["availability_status"], user["numbers"])
            self.id = user["id"]
        else:
            print("Error")
            print(r.text)

    def setUserAvailability(self, status="available"):
        params = json.dumps({'availability_status': status})
        r = settings.s.put(settings.url+'/users/'+str(self.id), params)
        print(r.json()) if r.status_code == 200 else print("Error : {}".format(r.json()))

