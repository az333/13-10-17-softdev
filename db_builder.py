
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="data.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

def maketable (tablename, csvdict):
    #create table
    datatypes = ["INTEGER", "TEXT", "INTEGER"]
    command = 'CREATE TABLE ' + tablename + '('
    fields = []
    for key in csvdict.next():
        fields.append(key)
    for i in range(len(fields)):
        command += " " + fields[i] + " " + datatypes[i] + ","
    #remove last comma
    command = command[:-1]
    command += ");"
    c.execute(command)

    #insert values
    for row in csvdict:
        command = "INSERT INTO " + tablename + " VALUES ("
        for key in row:
            command += ' "' + row[key] + '",'
        command = command[:-1]
        command += ");"
        c.execute(command)


peepscsv = open('data/peeps.csv')
peeps = csv.DictReader(peepscsv)
maketable ("peeps", peeps)
peepscsv.close()

coursescsv =  open('data/courses.csv')
courses = csv.DictReader(coursescsv)
maketable ("courses", courses)
coursescsv.close()


db.commit() #save changes
db.close()  #close database
