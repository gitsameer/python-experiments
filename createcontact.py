import atom  
import gdata.contacts  
import gdata.contacts.data
import gdata.contacts.client
import gdata.contacts.service  
import xml.etree.ElementTree as et
from user import User

def createUser (fn, ln, mobile, csid):
  u = User()
  GDATA_VER_HEADER = 'GData-Version'
  additional_headers = {'GData-Version': 3}
  gd_client = gdata.contacts.service.ContactsService(additional_headers = additional_headers)  
  gd_client.email = u.user
  gd_client.password = u.pwd
  gd_client.source = 'My Contacts'
  #gd_client.source = 'exampleCo-exampleApp-1'  
  #gd_client.source =  '680949029771.apps.googleusercontent.com'
  gd_client.ProgrammaticLogin()  

  gd_client2 = gdata.contacts.client.ContactsClient()
  gd_client2.client_login(u.user,u.pwd,"My Contact")


  #### get all the groups
  groupIDDict = {}
  groups = gd_client.GetGroupsFeed()
  for g in groups.entry:
    groupIDDict[g.title.text] = g.id.text
    print g.title.text, g.id.text

  title = "John 111 Test"
  new_contact = gdata.contacts.data.ContactEntry()
  new_contact.name = gdata.data.Name(
     given_name=gdata.data.GivenName("Test"),                  
     family_name=gdata.data.FamilyName("Contact"),
  )
  #title=atom.Title(text=title))
  #new_contact.title = atom.Title()
  #new_contact.title.text = "Full Name"

  primary_email = 'lizzy@ztester.com'

  # Set the contact's name.
  #new_contact.name = gdata.data.Name(full_name=gdata.data.FullName(text="John 623 Doe"))

  REL_MOBILE  = 'http://schemas.google.com/g/2005#mobile' 
  #mobile = '+14156667777'
  # set phone numbers
  new_contact.phone_number.append(gdata.data.PhoneNumber(text=mobile,
     rel=REL_MOBILE)) 

  # set the email address
  #new_contact.email.append(gdata.contacts.Email(address=primary_email,
  #    primary='true', rel=gdata.contacts.REL_WORK))

  # set the websitea TO FIGURE OUT THIS ONE

  #new_contact.website = gdata.data.Website(label='URL',href='http://couchsurfing.org/people/' + csid)

  '''
  # Set user defined fields
  new_contact.user_defined_field.append(
      gdata.contacts.UserDefinedField(
   key='Field Name',
   value='Field Value'
      )
  )
  '''

### To figure out this one????
  #new_contact.group_membership_info.append(gdata.contacts.GroupMembershipInfo(href=groupIDDict['CS'],deleted='false'))

  #print new_contact.ToString()
  print "---------------------------------------"
  entry = gd_client2.CreateContact(new_contact)

  if entry:
    print entry
  else :
    print "error"
