#! /usr/bin/python3

import settings
import json

class Team(object):
    def __init__(self, name="", users=[]):
        self.name = name
        self.users = users

    def getTeams(self):
        r = settings.s.get(settings.url+'/teams')
        if r.status_code == 200:
            print("Success")
        else:
            print("Error")
        print(r.json())

    def getTeam(self, id):
        r = settings.s.get(settings.url+'/teams/'+str(id))
        if r.status_code == 200:
            team = r.json()
            team = team["team"]
            self.__init__(team["name"], team["users"])
            self.id = team["id"]
        else:
            print("Error")
            print(r.text)

    def addUserToTeam(self, user_id):
        params = {'id': user_id}
        r = settings.s.post(settings.url+'/teams/'+str(self.id)+'/users', params=params)
        if r.status_code == 201:
            print("Success")
            print(r.json())
        else:
            print("Error")
            print(r.text)

    def deleteUserFromTeam(self, user_id):
        r = settings.s.delete(settings.url+'/teams/'+str(self.id)+'/users/'+str(user_id))
        if r.status_code == 200:
            print("Success")
        else:
            print("Error %s" % (r.text))

