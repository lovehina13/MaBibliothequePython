# coding: utf-8

#===============================================================================
# Name        : Iterateur.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (10/06/2018)
# Description : Itérateur de nombres
#===============================================================================


class Iterateur(object):

    def __init__(self, debut=0.0, fin=0.0, pas=0.0):
        self.__debut = None
        self.__fin = None
        self.__pas = None
        self.__position = 0
        self.__elements = []
        self.setDebut(debut)
        self.setFin(fin)
        self.setPas(pas)
        self.genererElements()

    def getDebut(self):
        return self.__debut

    def getFin(self):
        return self.__fin

    def getPas(self):
        return self.__pas

    def getPosition(self):
        return self.__position

    def getElements(self):
        return self.__elements

    def getElement(self, position=None):
        if position is None:
            return self.getElement(self.getPosition())
        else:
            elements = self.getElements()
            return elements[position] if position >= 0 and position <= (len(elements) - 1) else None

    def setDebut(self, debut):
        self.__debut = float(debut)
        # self.genererElements()

    def setFin(self, fin):
        self.__fin = float(fin)
        # self.genererElements()

    def setPas(self, pas):
        self.__pas = float(pas)
        # self.genererElements()

    def setPosition(self, position):
        elements = self.getElements()
        if position >= 0 and position <= (len(elements) - 1):
            self.__position = position

    def setElements(self, elements):
        self.__elements = elements

    def genererElements(self):
        from math import ceil
        debut = self.getDebut()
        fin = self.getFin()
        pas = self.getPas()
        elements = []
        nombre = int(ceil((fin - debut) / pas)) + 1
        for item in range(nombre):
            element = debut + item * pas
            elements.append(element)
        if elements[len(elements) - 1] != fin:
            elements[len(elements) - 1] = fin
        self.setElements(elements)

    def debut(self):
        self.setPosition(0)
        return (self.getPosition(), self.getElement())

    def fin(self):
        self.setPosition(len(self.getElements()) - 1)
        return (self.getPosition(), self.getElement())

    def precedent(self):
        self.setPosition(self.getPosition() - 1)
        return (self.getPosition(), self.getElement())

    def suivant(self):
        self.setPosition(self.getPosition() + 1)
        return (self.getPosition(), self.getElement())

    def courant(self):
        return (self.getPosition(), self.getElement())
