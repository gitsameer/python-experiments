import json
import atom  
import gdata.contacts  
import gdata.contacts.service  
import xml.etree.ElementTree as et
from user import User
u = User()

GDATA_VER_HEADER = 'GData-Version'
additional_headers = {GDATA_VER_HEADER: 3}
gd_client = gdata.contacts.service.ContactsService(additional_headers = additional_headers)  
gd_client.email = u.user
gd_client.password = u.pwd
gd_client.source = 'My Contacts'
#gd_client.source = 'exampleCo-exampleApp-1'  
#gd_client.source =  '680949029771.apps.googleusercontent.com'
gd_client.ProgrammaticLogin()  

groupIDDict = {}
groups = gd_client.GetGroupsFeed()
for g in groups.entry:
  groupIDDict[g.title.text] = g.id.text
  print g.title.text
  
query = gdata.contacts.service.ContactsQuery()
query.max_results = 10000
query.q = 'SOMECSID'
#query.group = groupIDDict['iphone contacts']

feed = gd_client.GetContactsFeed(query.ToUri())  
#entry = feed.entry[]  
#print feed
for entry in feed.entry:
  if (entry.title.text == "Test 111 Moscow") :
    print entry 
    print entry.nickname.text
    for user_defined_field in entry.user_defined_field:
      print '    User Defined Field %s: %s' % (user_defined_field.key, user_defined_field.value)


