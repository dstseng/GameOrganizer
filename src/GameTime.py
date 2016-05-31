
__author__="alfaflight"
__date__ ="$Apr 1, 2016 10:21:35 PM$"

from Database.Database import Database
from Database.Person import Person

Database_test = Database()
Person_test = Person("Hello", "World")
Database_test.addPerson(Person_test)
Person_test = Person("Derrick", "Tseng")
Database_test.addPerson(Person_test)
Database_test.displayDatabase()