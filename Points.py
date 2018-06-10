# coding: utf-8

#===============================================================================
# Name        : Points.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (10/06/2018)
# Description : Point, liste de points, interpolation et polynôme
#===============================================================================


class Point(object):

    def __init__(self, x=0.0, y=0.0):
        self.__x = None
        self.__y = None
        self.setX(x)
        self.setY(y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getXY(self):
        return (self.getX(), self.getY())

    def setX(self, x):
        self.__x = float(x)

    def setY(self, y):
        self.__y = float(y)

    def setXY(self, x, y):
        self.setX(x)
        self.setY(y)


class Points(object):

    def __init__(self, listePoints=None):
        self.__listePoints = []
        if listePoints is not None:
            self.setListePoints(listePoints)

    def getListePoints(self):
        return self.__listePoints

    def setListePoints(self, listePoints):
        self.__listePoints = []
        for point in listePoints:
            self.ajouterPoint(point)

    def ajouterPoint(self, point, trier=True):
        if isinstance(point, Point):
            self.__listePoints.append(point)
            if trier:
                self.__listePoints.sort(key=lambda point: (point.getX(), point.getY()))

    def interpolerPoint(self, x):
        listePoints = self.getListePoints()
        pointPrecedent = None
        pointSuivant = None
        for point in listePoints:
            if point.getX() == x:
                return point.getY()
            elif point.getX() < x:
                pointPrecedent = point
            elif point.getX() > x:
                pointSuivant = point
                break
        if pointPrecedent is None:
            pointPrecedent = listePoints[0]
            pointSuivant = listePoints[1]
        if pointSuivant is None:
            pointPrecedent = listePoints[len(listePoints) - 2]
            pointSuivant = listePoints[len(listePoints) - 1]
        deltaX = pointSuivant.getX() - pointPrecedent.getX()
        deltaY = pointSuivant.getY() - pointPrecedent.getY()
        pente = deltaY / deltaX
        y = pente * (x - pointPrecedent.getX()) + pointPrecedent.getY()
        return y

    def interpolerPas(self, pas):
        from math import ceil, floor
        listePoints = self.getListePoints()
        nombrePoints = len(listePoints)
        borneInferieure = listePoints[0].getX()
        borneSuperieure = listePoints[nombrePoints - 1].getX()
        listePointsInterpoles = []
        xMinimum = floor(borneInferieure / pas) * pas
        xMaximum = ceil(borneSuperieure / pas) * pas
        nombrePointsInterpoles = int(round((xMaximum - xMinimum) / pas)) + 1
        for element in range(nombrePointsInterpoles):
            xInterpole = xMinimum + element * pas
            yInterpole = self.interpolerPoint(xInterpole)
            pointInterpole = Point(xInterpole, yInterpole)
            listePointsInterpoles.append(pointInterpole)
        return listePointsInterpoles

    def recupererPolynome(self, degre):
        from numpy import poly1d, polyfit
        listePoints = self.getListePoints()
        abscisses = [point.getX() for point in listePoints]
        ordonnees = [point.getY() for point in listePoints]
        coefficients = polyfit(abscisses, ordonnees, degre, full=True)[0]
        polynome = poly1d(coefficients)
        return polynome, list(reversed(coefficients.tolist()))

    def estTrie(self):
        abscisses = [point.getX() for point in self.getListePoints()]
        abscissesTriees = sorted(abscisses)
        return abscisses == abscissesTriees


def interpolerFichier(fichierEntree, fichierSortie, pas):
    from LectureEcritureFichier import ecrireFichier, lireFichier
    from OperationsTexte import convertirNombreEnTexte, separerEtConvertirTexte

    listePoints = Points()
    lignesFichierEntree = lireFichier(fichierEntree)
    for ligne in lignesFichierEntree:
        x = separerEtConvertirTexte(ligne)[0]
        y = separerEtConvertirTexte(ligne)[1]
        point = Point(x, y)
        listePoints.ajouterPoint(point)
    listePointsInterpoles = listePoints.interpolerPas(pas)
    lignesFichierSortie = [str("%s %s" % (
        convertirNombreEnTexte(pointInterpole.getX()),
        convertirNombreEnTexte(pointInterpole.getY())))
        for pointInterpole in listePointsInterpoles]
    ecrireFichier(fichierSortie, lignesFichierSortie)


def recupererPolynomeFichier(fichierEntree, degre):
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import separerEtConvertirTexte

    listePoints = Points()
    lignesFichierEntree = lireFichier(fichierEntree)
    for ligne in lignesFichierEntree:
        x = separerEtConvertirTexte(ligne)[0]
        y = separerEtConvertirTexte(ligne)[1]
        point = Point(x, y)
        listePoints.ajouterPoint(point)
    return listePoints.recupererPolynome(degre)
