#import pdb
import atom.data  
import gdata
import gdata.data
import gdata.contacts  
import gdata.contacts.data
import gdata.contacts.client
import gdata.contacts.service  
import xml.etree.ElementTree as et
from user import User
from urllib import urlretrieve

def createUser3 (fn, ln, mobile, csid, group, notes, url):
  u = User()
  GDATA_VER_HEADER = 'GData-Version'
  additional_headers = {'GData-Version': 3.0}
  gd_client = gdata.contacts.service.ContactsService(additional_headers = additional_headers)  
  gd_client.debug = True
  #gd_client = gdata.contacts.service.ContactsService()
  gd_client.email = u.user
  gd_client.password = u.pwd
  gd_client.source = 'My Contacts'
  #gd_client.source = 'exampleCo-exampleApp-1'  
  #gd_client.source =  '680949029771.apps.googleusercontent.com'
  gd_client.ProgrammaticLogin()  


  #### get all the groups
  groupIDDict = {}
  groups = gd_client.GetGroupsFeed()
  for g in groups.entry:
    groupIDDict[g.title.text] = g.id.text
    print g.title.text, g.id.text

  title = "John 111 Test"
  new_contact = gdata.contacts.ContactEntry()
  #title=atom.Title(text=title))
  #new_contact.title = atom.Title()
  #new_contact.title.text = "Full Name"

  primary_email = 'lizzy@ztester.com'

  # Set the contact's name.
  #new_contact.name = gdata.data.Name(full_name=gdata.data.FullName(text="John 623 Doe"))
  new_contact.name = gdata.data.Name(
     given_name=gdata.data.GivenName("Test___"),                  
     family_name=gdata.data.FamilyName("Contact___"),
  )

  REL_MOBILE  = 'http://schemas.google.com/g/2005#mobile' 
  #mobile = '+14156667777'
  # set phone numbers
  new_contact.phone_number.append(gdata.contacts.PhoneNumber(text=mobile,
     rel=REL_MOBILE)) 

  # set the email address
  #new_contact.email.append(gdata.contacts.Email(address=primary_email,
  #    primary='true', rel=gdata.contacts.REL_WORK))

  # set the website TO FIGURE OUT THIS ONE

  new_contact.website = gdata.contacts.Website(label='URL',href='http://couchsurfing.org/people/' + csid)

  '''
  # Set user defined fields
  new_contact.user_defined_field.append(
      gdata.contacts.UserDefinedField(
   key='Field Name',
   value='Field Value'
      )
  )
  '''

  new_contact.group_membership_info.append(gdata.contacts.GroupMembershipInfo(href=groupIDDict['CS'],deleted='false'))
  new_contact.group_membership_info.append(gdata.contacts.GroupMembershipInfo(href=groupIDDict[group],deleted='false'))

  #print new_contact.ToString()
  print "---------------------------------------"
  entry = gd_client.CreateContact(new_contact)

  if len(url)>0:
    fname = url.split('/')[-1]
    urlretrieve(url,fname)
    gd_client.ChangePhoto(fname,entry.GetPhotoLink().href,content_type='image/jpeg', content_length=len)

  if entry:
    print entry.id
    gd_client2 = gdata.contacts.client.ContactsClient()
    gd_client2.client_login(u.user,u.pwd,"My Contact")
    contact2 = gd_client2.GetContact(entry.id.text)
    contact2.content = atom.data.Content(text=notes)
    contact2.name = gdata.data.Name(
     given_name=gdata.data.GivenName(fn),                  
     family_name=gdata.data.FamilyName(ln),
    )

    entry2 = gd_client2.Update(contact2)

  else :
    print "error"
