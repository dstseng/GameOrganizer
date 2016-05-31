__author__="alfaflight"
__date__ ="$Apr 1, 2016 10:27:30 PM$"

from Database import Database

class Person:
    def __init__(self, String_firstName, String_lastName):
        self.__String_firstName = String_firstName
        self.__String_lastName = String_lastName
        self.__Dict_dbEntry = {}
        self.__Dict_dbEntry[Database.FirstNameToken] = self.__String_firstName
        self.__Dict_dbEntry[Database.LastNameToken] = self.__String_lastName

    def Dict_databaseEntry(self):
        return self.__Dict_dbEntry

    def String_getFirstName(self):
        return self.__String_firstName

    def String_getLastName(self):
        return self.__String_lastName