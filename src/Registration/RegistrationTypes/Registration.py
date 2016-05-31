
__author__="alfaflight"
__date__ ="$Apr 9, 2016 10:16:09 PM$"

class Registration:

    def __init__(self, Person_person, Bool_isCaptain):
        self.__Person_person = Person_person
        self.__Bool_isCaptain = Bool_isCaptain

    def Person_getPerson(self):
        return self.__Person_person

    def Bool_isCaptain(self):
        return self.__Bool_isCaptain()
