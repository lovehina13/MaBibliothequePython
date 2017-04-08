# coding: utf-8

#===============================================================================
# Name        : FiltrageFichier.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (08/04/2017)
# Description : Filtrage de fichier
#===============================================================================

def filtrerFichierSelonPrecision(fichier, resultat, precision, separateur=" "):
    from ComparaisonElements import identiques
    from LectureEcritureFichier import ecrireFichier, lireFichier
    from OperationsTexte import joindreEtConvertirListeTexte, separerEtConvertirListeTexte
    from math import fabs

    lignes = separerEtConvertirListeTexte(lireFichier(fichier), separateur)
    nbLignes = len(lignes)

    deltaColonnes = {}
    valeursColonnes = {}
    for itLigne in range(nbLignes):
        elements = lignes[itLigne]
        nbElements = len(elements)
        for itElement in range(nbElements):
            element = elements[itElement]
            if not valeursColonnes.has_key(itElement):
                valeursColonnes[itElement] = []
            valeursColonnes[itElement].append(element)
    nbColonnes = len(valeursColonnes)
    for itColonne in range(nbColonnes):
        valeurs = valeursColonnes[itColonne]
        delta = recupererDeltaValeurs(valeurs)
        deltaColonnes[itColonne] = delta

    lignesFiltrees = [lignes[0]]
    elementsPrecedents = lignes[0]
    for itLigne in range(1, nbLignes):
        elements = lignes[itLigne]
        nbElements = len(elements)
        for itElement in range(nbElements):
            elementPrecedent = elementsPrecedents[itElement]
            element = elements[itElement]
            divergence = False
            if isinstance(element, str) or isinstance(elementPrecedent, str):
                if not identiques(element, elementPrecedent):
                    divergence = True
            else:
                delta = deltaColonnes[itElement]
                try:
                    ecart = fabs(element - elementPrecedent) / min(fabs(element), fabs(elementPrecedent))
                except ZeroDivisionError:
                    ecart = fabs(element - elementPrecedent)
                if ecart > (delta * precision):
                    divergence = True
            if divergence:
                elementsPrecedents = elements
                lignesFiltrees.append(elements)
                break
    if lignes[nbLignes - 1] not in lignesFiltrees:
        lignesFiltrees.append(lignes[nbLignes - 1])

    ecrireFichier(resultat, joindreEtConvertirListeTexte(lignesFiltrees, separateur))

def filtrerFichierSelonNombreLignes(fichier, resultat, nbLignes, separateur=" "):
    from LectureEcritureFichier import lireFichier
    import sys

    precisionInferieure = 0.0
    precisionSuperieure = 1.0
    precision = (precisionInferieure + precisionSuperieure) / 2.0
    epsilon = sys.float_info.epsilon
    while True:
        filtrerFichierSelonPrecision(fichier, resultat, precision, separateur)
        nbLignesFiltrees = len(lireFichier(resultat))
        if nbLignesFiltrees < nbLignes:
            print "Précision %e trop grande, %d lignes récupérées" % (precision, nbLignesFiltrees)
            precisionSuperieure = precision
            precision = (precisionInferieure + precisionSuperieure) / 2.0
        elif nbLignesFiltrees > nbLignes:
            print "Précision %e trop petite, %d lignes récupérées" % (precision, nbLignesFiltrees)
            precisionInferieure = precision
            precision = (precisionInferieure + precisionSuperieure) / 2.0
        elif (precisionSuperieure - precisionInferieure) < epsilon:
            print "Précision limite %e insuffisante, %d lignes récupérées" % (precision, nbLignesFiltrees)
            break
        else:
            print "Précision %e suffisante, %d lignes récupérées" % (precision, nbLignesFiltrees)
            break

def recupererDeltaValeurs(valeurs):
    from OperationsTexte import convertirTexteEnNombre
    from math import fabs

    minimum = None
    maximum = None
    delta = 0.0
    nbValeurs = len(valeurs)
    for itValeur in range(nbValeurs):
        valeur = valeurs[itValeur]
        if convertirTexteEnNombre(valeur, True) is not None:
            if valeur < minimum or minimum is None:
                minimum = valeur
            if valeur > maximum or maximum is None:
                maximum = valeur
    if minimum is not None and maximum is not None:
        delta = fabs(maximum - minimum)
    return delta
