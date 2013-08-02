import json

class User:
 user = ''
 pwd = ''
 def __init__(self):
   j=open('settings.json')
   data = json.load(j)
   self.user = data["user"]
   self.pwd  = data["pwd"]


