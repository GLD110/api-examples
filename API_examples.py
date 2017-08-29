#! /usr/bin/python

# Load HTTP requests components
import requests
from requests.auth import HTTPBasicAuth

# Authentication test

base_url = "https://api.aircall.io/v1"
user = "" #"your_api_id"
password = "" #"your_api_token"
auth = HTTPBasicAuth(user, password)

r = requests.get(base_url+"/ping", auth=auth)
r.text

# GET list of users, contacts, calls, numbers

r = requests.get(base_url+"/users", auth=auth)
r.text

# CREATE contact

import json

first_name = "John"
last_name = "Doe"
company_name = "Acme"
information = ""

class Phone(object):
	"""docstring for Phone"""
	def __init__(self, label="", value=""):
		self.label = "Work"
		self.value = "+33631000000"

class Email(object):
	"""docstring for Email"""
	def __init__(self, label="", value=""):
		self.label = "Work"
		self.value = 'john.doe@something.io'

phone_numbers = [Phone().__dict__]
emails = [Email().__dict__]

params = json.dumps({
	"first_name": first_name,
	"last_name": last_name,
	"company_name": company_name,
	"information": information,
	"phone_numbers": phone_numbers,
	"emails": emails
	})

headers = {'content-type': 'application/json'}

r = requests.post(base_url+"/contacts", params, auth=auth, headers=headers)
r.text

# DELETE contact, recording, voicemail

r = requests.delete(base_url+"/contacts/{contact_id}", auth=auth)
