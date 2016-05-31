
__author__="alfaflight"
__date__ ="$Apr 9, 2016 10:15:57 PM$"

from RegistrationTypes.BasketballRegistration import BasketballRegistration

class RegistrationOrganizer:

    def __init__(self, Database_db, TeamOrganizer_organizer):
        self.__Database_db = Database_db
        self.__TeamOrganizer_organizer = TeamOrganizer_organizer

    def newRegistrationRequest(self):