import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==============~~~using csv module~~~=================
ppls= open("peeps.csv")
peeps= csv.DictReader(ppls)

crses= open("courses.csv")
courses= csv.DictReader(crses)

#==========================================================
'''for each in peeps:
   # print each #+":" each['name']+','+each['age']+','+each['id']
    print each['name']
    print each['age']
    print each['id']
'''

command = "CREATE TABLE people (name TEXT, age INTEGER, id INTEGER)" #put SQL statement in this string
c.execute(command)    #run SQL statement
print "table people created\n\n"

def populate(d, one, two,three,tbl):
    for i in d:
        print i
        c.execute("INSERT INTO "+tbl+" VALUES("+i[one]+","+ i[two]+","+i[three]+")")
        print "row inserted"
    print "inserted all things to tbl"
    
populate(peeps, 'name','age','id','people')

'''comm = "CREATE TABLE classes(code TEXT, mark INTEGER, id INTEGER)"
c.execute (comm)

for i in courses:
    c.execute("INSERT INTO classes VALUES("+i['code']+","+ i['mark']+","+i['id']+")")

'''

#==========================================================

db.commit() #save changes
db.close()  #close database


