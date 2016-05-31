
__author__="alfaflight"
__date__ ="$Apr 9, 2016 10:32:15 PM$"

class Team:

    def __init__(self, List_Registration_teammates):
        self.__Int_numOfWins = 0
        self.__List_Registration_teammates = List_Registration_teammates
        
    def addWin(self):
        self.__Int_numOfWins += 1

    def getNumOfWins(self):
        return self.__Int_numOfWins

    def getTeammates(self):
        return List_Registration_teammates