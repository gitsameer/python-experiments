import json
import atom  
import gdata.contacts  
import gdata.contacts.data
import gdata.contacts.client
import gdata.contacts.service  
import xml.etree.ElementTree as et
from user import User


def listUsers():
  rel_list = {gdata.contacts.REL_WORK: "Work",
            gdata.contacts.REL_HOME: "Home",
            gdata.contacts.REL_OTHER: "Other",
            gdata.contacts.PHONE_MOBILE: "Mobile"}
 
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
    
  query = gdata.contacts.service.ContactsQuery(feed='/m8/feeds/contacts/default/full')
  query.max_results = 500
  #query.q = 'SOMECSID'
  #query.group = groupIDDict['iphone contacts']

  client = gdata.contacts.client.ContactsClient()
  client.client_login(u.user,u.pwd,'My Contacts')
  qry = gdata.contacts.client.ContactsQuery(max_results=50)
  feed = client.GetContacts(query=qry)
  #entry = feed.entry[]  
  #print feed
  for entry in feed.entry:
    print entry
    print entry.title.text
    print entry.id.text
    for phone in entry.phoneNumber:
        print rel_list[phone.rel] + ": " + phone.text

listUsers()
