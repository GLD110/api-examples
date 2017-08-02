#! /usr/bin/python

import requests
from requests.auth import HTTPBasicAuth

def init():
    global url
    global user
    global password
    global auth
    global headers
    global s
    s = requests.Session()
    url = 'https://api.aircall.io/v1'
    user = "9605cc2704e252fdab7cca5e2c3e5528" #"your_api_id"
    password = "8639783a24d5da4ff23f05ee09f42b5c" #"your_api_token"
    s.auth = HTTPBasicAuth(user, password)
    s.headers = {'Content-Type': 'application/json', 'User_Agent': 'AircallSDK'}
