# coding: utf-8

#===============================================================================
# Name        : Temps.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (07/06/2017)
# Description : Temps et liste de temps
#===============================================================================

class Temps(object):

    def __init__(self, listeTemps=None):
        self.__listeTemps = []
        if listeTemps is not None:
            self.setListeTemps(listeTemps)

    def getListeTemps(self):
        return self.__listeTemps

    def setListeTemps(self, listeTemps):
        self.__listeTemps = []
        for temps in listeTemps:
            self.ajouterTemps(temps)

    def ajouterTemps(self, temps, trier=True):
        from datetime import datetime
        if isinstance(temps, datetime):
            self.__listeTemps.append(temps)
            if trier:
                self.__listeTemps.sort()

    def getListeDeltaTemps(self):
        listeTemps = self.getListeTemps()
        listeDeltaTemps = []
        tempsPrecedent = None
        for temps in listeTemps:
            if tempsPrecedent is not None:
                deltaTemps = temps - tempsPrecedent
                listeDeltaTemps.append(deltaTemps)
            tempsPrecedent = temps
        return listeDeltaTemps

    def etape(self):
        from datetime import datetime
        self.ajouterTemps(datetime.now(), False)

    def debut(self):
        self.etape()

    def fin(self):
        self.etape()
