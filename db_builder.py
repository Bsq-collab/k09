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
              
command= "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

command= "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

for each in peeps:
    print each
    add= "INSERT INTO peeps VALUES ('" + each['name'] + "'," + each['age'] + "," + each['id'] + ")"
    c.execute(add)

for each in courses:
    print each
    add= "INSERT INTO courses VALUES ('" + each['code'] + "'," + each['mark'] + "," + each['id'] + ")"
    c.execute(add)

    
#==========================================================

db.commit() #save changes
db.close()  #close database


