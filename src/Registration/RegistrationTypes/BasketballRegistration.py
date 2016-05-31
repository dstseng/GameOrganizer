
__author__="alfaflight"
__date__ ="$Apr 9, 2016 10:16:54 PM$"

from RegistrationTypes import Registration

class BasketballRegistration(Registration):

    def __init__(self, Person_person, Bool_isCaptain):
        super(BasketballRegistration, self).__init__(Person_person, Bool_isCaptain)