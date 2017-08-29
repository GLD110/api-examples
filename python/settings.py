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
    user = "" #"your_api_id"
    password = "" #"your_api_token"
    s.auth = HTTPBasicAuth(user, password)
    s.headers = {'Content-Type': 'application/json', 'User_Agent': 'AircallSDK'}
