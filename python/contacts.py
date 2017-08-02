#! /usr/bin/python3

import settings
import requests
import json
import re
import phonenumbers

class Contact(object):
    """ Aircall contact """

    def __init__(self, first_name="", last_name="", company='', information='', phone_numbers={},
                 emails={}):
       self.first_name = first_name
       self.last_name = last_name
       self.company = company
       self.information = information
       self.phone_numbers = phone_numbers if isinstance(phone_numbers, list) else [phone_numbers]
       self.emails = emails if isinstance(emails, list) else [emails]

    def getContact(self, id):
        r = settings.s.get(settings.url+'/contacts/'+id)
        contact = r.json()
        contact = contact["contact"]
        self.__init__(contact["first_name"], contact["last_name"], contact["company_name"],
                    contact["information"], contact["phone_numbers"], contact["emails"])
        self.id = contact["id"]

    def getContacts(self):
        r = settings.s.get(settings.url+'/contacts/')
        if r.status_code == 200:
            print(r.json())
        else:
            print("Error")
            print(r.json())

    def setContact(self):
        params = json.dumps(self.__dict__)
        r = settings.s.post(settings.url+'/contacts', params)
        if r.status_code == 201:
            contact = r.json()
            contact = contact["contact"]
            self.__init(contact["first_name"], contact["last_name"], contact["company_name"],
                    contact["information"], contact["phone_numbers"], contact["emails"])
            self.id = contact["id"]
            print(r.json())
        else:
            print("Error")
            print(r.text)

    def deleteContact(self):
        r = settings.s.delete(settings.url+'/contacts/'+str(self.id))
        if r.status_code == 204:
            print("Successfully deleted")
        else:
            print("Error")
            print(r.json())
            
    def updateContact(self):
        params = json.dumps(self.__dict__)
        r = settings.s.post(settings.url+'/contacts/'+str(self.id), params)
        if r.status_code == 200:
            print("Success")
        else:
            print("ERROR")
        print(r.json())
   
class Phone(object):
    def __init__(self, label, value):
        self.label = label
        number = phonenumbers.parse(value, None)
        if phonenumbers.is_possible_number(number): 
            print("Success")
            self.value = value
        else:
            print("Error phone number")

    def addPhone(self, contact_id):
        params = json.dumps(self.__dict__)
        r = settings.s.post(settings.url+'/contacts/'+contact_id+'/phone_details', params)
        if r.status_code == 201:
            print("Success")
        else:
            print("ERROR")
        print(r.json())

    def updatePhone(self, contact_id, phone_id):
        params = json.dumps(self.__dict__)
        r = settings.s.put(settings.url+'/contacts/'+contact_id+'/phone_details/'+phone_id, params)
        if r.status_code == 202:
            print("Success")
        else:
            print("ERROR")
        print(r.json())

    def deletePhone(self, contact_id, phone_id):
        r = settings.s.delete(settings.url+'/contacts/'+contact_id+'/phone_details/'+phone_id)
        if r.status_code == 204:
            print("Phone number successfully deleted")
        else:
            print("ERROR")
            print(r.text)

class Email(object):
    def __init__(self, label, value):
        self.label = label
        if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value, re.I):
            print("Success")
            self.value = value
        else:
            print("Your email address format is not valid")
        
    def addEmail(self, contact_id):
        params = json.dumps(self.__dict__)
        r = settings.s.post(settings.url+'/contacts/'+contact_id+'/email_details', params)
        if r.status_code == 201:
            print("Success")
        else:
            print("ERROR")
        print(r.json()) 

    def updateEmail(self, contact_id, email_id):
        params = json.dumps(self.__dict__)
        r = settings.s.put(settings.url+'/contacts/'+contact_id+'/email_details/'+email_id,
                           params)
        if r.status_code == 202:
            print("Success")
        else:
            print("Error")
        print(r.json())

    def deleteEmail(self, contact_id, email_id):
        r = settings.s.delete(settings.url+'/contacts/'+contact_id+'/email_details/'+email_id)
        if r.status_code == 204:
            print("Mail successfully deleted")
        else:
            print("Error")
            print("r.text")
