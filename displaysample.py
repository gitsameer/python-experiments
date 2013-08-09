import sha
import atom
import gdata.contacts
import gdata.contacts.service
from user import User
from xml.dom import minidom
from xml.etree.ElementTree import XML, fromstring, tostring

K_GROUP='Murmansk'
 
u = User()
additional_headers = {'GData-Version' : '3.0' }
gd_client = gdata.contacts.service.ContactsService(additional_headers = additional_headers)



# Change this obviously 
gd_client.email = u.user
gd_client.password = u.pwd
gd_client.ProgrammaticLogin()

# readin all the groups
groupIDDict = {}
groups = gd_client.GetGroupsFeed()
for g in groups.entry:
  groupIDDict[g.title.text] = g.id.text
  print g.title.text

"""
This is used like a case statement later on.
It's apparently a slightly slow way to do it but it just seems so elegant to me.  I'm not a Pythonista at all though so there may be a more Pythonic way to do it that I'm not aware of.
""" 
rel_list = {gdata.contacts.REL_WORK: "Work",
            gdata.contacts.REL_HOME: "Home",
            gdata.contacts.PHONE_WORK_FAX: "WorkFax",
            gdata.contacts.PHONE_PAGER: "Pager",
            gdata.contacts.REL_OTHER: "Other",
            gdata.contacts.PHONE_MOBILE: "Mobile"}

# This is the date used for "updated_min" below.
date = '2009-08-12T00:00:00'
 
query = gdata.contacts.service.ContactsQuery()
query.feed='/m8/feeds/contacts/default/full?max_results=1000'
query.max_results = 10000
query.updated_min = date
query.group = groupIDDict[K_GROUP]
 

feed = gd_client.GetContactsFeed(query.ToUri())
 
for contact in feed.entry:
      print contact.website[0].href
      print contact.id.text
      print contact.title.text
      for phone in contact.phone_number:
        print rel_list[phone.rel] + ": " + phone.text
 
def rel_type(rel):
    pass
