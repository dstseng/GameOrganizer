__author__="alfaflight"
__date__ ="$Apr 1, 2016 10:27:23 PM$"
import csv

class Database:
    FirstNameToken = 'First Name'
    LastNameToken = 'Last Name'

    def __init__(self, String_pathToCsvDB = None):
        self.__List_fields = [Database.FirstNameToken, Database.LastNameToken]
        self.__List_db = []
        if String_pathToCsvDB != None:
            File_csv = open(String_pathToCsvDB)
            DictReader_reader = csv.DictReader(File_csv)
            self.List_fields = DictReader_reader.fieldnames
            for row in DictReader_reader:
                self.__List_db.append(row)

    def addPerson(self, Person_newPerson):
        self.__List_db.append(Person_newPerson.Dict_databaseEntry())

    def removePerson(self, Int_personID):
        self.__List_db.pop(Int_personID)

    def displayDatabase(self):
        for entry in self.__List_db:
            print str(entry)

