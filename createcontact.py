import atom  
import gdata.contacts  
import gdata.contacts.data
import gdata.contacts.service  
import xml.etree.ElementTree as et
from user import User
u = User()
  
GDATA_VER_HEADER = 'GData-Version'
additional_headers = {GDATA_VER_HEADER: 3.0}
gd_client = gdata.contacts.service.ContactsService(additional_headers = additional_headers)  
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

'''
name = 'Johnnie'
primary_email = 'testjohn@tester.com'
new_contact = gdata.contacts.ContactEntry(title=atom.Title(text=name))
new_contact.email.append(gdata.contacts.Email(address=primary_email,
    primary='true', rel=gdata.contacts.REL_WORK))
#new_contact.addExternalId('abcJohnnie')
new_contact.extended_property.append(gdata.ExtendedProperty(name='CSID',value='abcJohnnie'))
entry = gd_client.CreateContact(new_contact)

'''

new_contact = gdata.contacts.ContactEntry()
primary_email = 'lizzy@ztester.com'

# Set the contact's name.
new_contact.name = gdata.data.Name(
    given_name=gdata.data.GivenName(text='Elizabeth'),
    family_name=gdata.data.FamilyName(text='Bennet'),
    full_name=gdata.data.FullName(text='Elizabeth Bennet')
)

REL_MOBILE  = 'http://schemas.google.com/g/2005#mobile' 
mobile = '+14156667777'
# set phone numbers
new_contact.phone_number.append(gdata.contacts.PhoneNumber(text=mobile,
                        rel=REL_MOBILE)) 

# set the email address
new_contact.email.append(gdata.contacts.Email(address=primary_email,
    primary='true', rel=gdata.contacts.REL_WORK))

# set the website
new_contact.website = gdata.contacts.Website(label='URL',href='http://www.yahoo.com')

# Set user defined fields
new_contact.user_defined_field.append(
    gdata.contacts.UserDefinedField(
        key='Field Name',
        value='Field Value'
    )
)

new_contact.group_membership_info.append(gdata.contacts.GroupMembershipInfo(href=groupIDDict['CS'],deleted='false'))
entry = gd_client.CreateContact(new_contact)

if entry:
  print entry
else :
  print "error"
