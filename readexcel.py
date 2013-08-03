import xlrd

book = xlrd.open_workbook("/Users/sameersingh/Documents/Personal/Travel/CouchStatsNew.xls")

sheet = book.sheet_by_name("St Petersburg")

print sheet.name, sheet.nrows, sheet.ncols

#for rx in range(sheet.nrows):
#        print sheet.row(rx)

for rx in range(sheet.nrows):

 print "len = " + str(len(sheet.cell_value(rx,0).strip()))
 if len == 0:
   next

 rating = sheet.cell_value(rx,6)
 if rating == "":
   rating = 4
 else:
   rating = int(rating)
  

 age = sheet.cell_value(rx,5)
 if type(age) == str:
   age =  25
 else:
   age = int(age)
   
 print "csid = " + sheet.cell_value(rx,0) + "\n"
 print "name = " + sheet.cell_value(rx,2) + " " + str(rating) + str(age) + " " + sheet.name + "\n"
 print "phone = " + str(sheet.cell_value(rx,4)) + "\n"
 print "notes = " + sheet.cell_value(rx,7) + "\n"
 print "URL = " + "http://www.couchsuring.org/people/" + sheet.cell_value(rx,0) + "/"
