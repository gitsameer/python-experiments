import xlrd
from createcontact3 import createUser3
from contactUtil import getGroupMembersDict


def createFromExcel (sheetName): 

  K_GROUP=sheetName
  csIDContactIDDict = getGroupMembersDict(K_GROUP)
  book = xlrd.open_workbook("/Users/sameersingh/Documents/Personal/Travel/CouchStatsNew.xls")

  K_CSID_COL = 0
  K_FN_COL = 2
  K_LN_COL = 3
  K_AGE_COL = 4
  K_PHONE_COL = 5
  K_RATING_COL = 6
  K_NOTES_COL = 7

  sheet = book.sheet_by_name(K_GROUP)

  print sheet.name, sheet.nrows, sheet.ncols

  #for rx in range(sheet.nrows):
  #        print sheet.row(rx)

  for rx in range(sheet.nrows):

   print "len = " + str(len(sheet.cell_value(rx,K_CSID_COL).strip()))
   if len == 0:
    continue 

   ### for phones check if it a number, if so, convert to string, strip trailing
   ### decimals and remove space in the numbers

   p = str(sheet.cell_value(rx,K_PHONE_COL))
   t = sheet.cell_type(rx,K_PHONE_COL)
   # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
   if (t == 2) :
     p = str(int(float(p)))
   p = "".join(p.split())
   p = "".join(c for c in p if c.isdigit() or c == "+")
   p = p.strip()

   print "p = " + p + "len = " + str(len(p))
   if len(p) == 0:
     continue

   rating = sheet.cell_value(rx,K_RATING_COL)
   if rating == "":
     rating = 4
   else:
     rating = int(rating)
    

   age = sheet.cell_value(rx,K_AGE_COL)
   if type(age) == str:
     age =  "??"
   else:
     age = int(age)
     
   print "csid = " + sheet.cell_value(rx,K_CSID_COL) + "\n"
   print "name = " + sheet.cell_value(rx,K_FN_COL) + " " + str(rating) + str(age) + " " + sheet.name + "\n"


   notes = sheet.cell_value(rx,K_NOTES_COL)

   if sheet.cell_value(rx,K_CSID_COL) in csIDContactIDDict:
     print "will update user " + sheet.cell_value(rx,2)
   else:
     print "will create user " + sheet.cell_value(rx,2)
     createUser3(sheet.cell_value(rx,2), str(rating)+str(age) +  " " + K_GROUP, p,sheet.cell_value(rx,K_CSID_COL),K_GROUP,notes)


createFromExcel("Murmansk")
