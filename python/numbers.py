#! /usr/bin/python3

import settings
import json

class Number(object):
    
    def __init__(self,  name="", digits="", country="", time_zone="", open="",
                 availability_status="", users=""):
        self.name = name
        self.digits = digits
        self.country = country
        self.time_zone = time_zone
        self.open = open
        self.availability_status = availability_status
        self.users = users

    def getNumbers(self):
        r = settings.s.get(settings.url+'/numbers')
        print(r.json()) if r.status_code == 200 else print("Error : {}".format(r.json()))

    def getNumber(self, id):
        r = settings.s.get(settings.url+'/numbers/'+id)
        if r.status_code == 200:
            number = r.json()
            number = number["number"]
            self.__init__(number["name"], number["digits"], number["country"], number["time_zone"],
                          number["open"], number["availability_status"], number["users"])
            self.id = number["id"]
        else:
            print("ERROR : {}".format(r.text()))

    def setNumberAvailability(self, status="open"):
        status = json.dumps({'availability_status': status})
        r = settings.s.put(settings.url+'/numbers/'+str(self.id), status)
        print(r.json()) if r.status_code == 200 else print("Error : {}".format(r.text))
