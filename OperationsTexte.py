# coding: utf-8

#===============================================================================
# Name        : OperationsTexte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (10/06/2018)
# Description : Conversion, séparation, jointure et nettoyage de texte
#===============================================================================


def convertirTexteEnNombre(texte, retourNul=False):
    try:
        return int(texte)
    except ValueError:
        pass
    try:
        return float(texte)
    except ValueError:
        pass
    return None if retourNul else texte


def convertirTexteEnDate(texte, formatDate="%d/%m/%Y %H:%M:%S"):
    from datetime import datetime
    return datetime.strptime(texte, formatDate)


def convertirNombreEnTexte(nombre, retourNul=False):
    if isinstance(nombre, int):
        return str("%d" % (nombre))
    if isinstance(nombre, float):
        return str("%.16e" % (nombre))
    return None if retourNul else str("%s" % (nombre))


def convertirDateEnTexte(date, formatDate="%d/%m/%Y %H:%M:%S"):
    return date.strftime(formatDate)


def separerTexte(texte, separateur=" "):
    return [element for element in texte.split(separateur) if element is not None]


def joindreTexte(texte, separateur=" "):
    return separateur.join(texte)


def nettoyerTexte(texte, separateur=" "):
    return joindreTexte(separerTexte(texte, separateur), separateur)


def separerListeTexte(listeTexte, separateur=" "):
    return [separerTexte(element, separateur) for element in listeTexte]


def joindreListeTexte(listeTexte, separateur=" "):
    return [joindreTexte(element, separateur) for element in listeTexte]


def nettoyerListeTexte(listeTexte, separateur=" "):
    return [nettoyerTexte(element, separateur) for element in listeTexte]


def separerEtConvertirTexte(texte, separateur=" "):
    return [convertirTexteEnNombre(element) for element in separerTexte(texte, separateur)]


def joindreEtConvertirTexte(texte, separateur=" "):
    return joindreTexte([convertirNombreEnTexte(element) for element in texte], separateur)


def nettoyerEtConvertirTexte(texte, separateur=" "):
    return joindreEtConvertirTexte(separerEtConvertirTexte(texte, separateur), separateur)


def separerEtConvertirListeTexte(listeTexte, separateur=" "):
    return [separerEtConvertirTexte(element, separateur) for element in listeTexte]


def joindreEtConvertirListeTexte(listeTexte, separateur=" "):
    return [joindreEtConvertirTexte(element, separateur) for element in listeTexte]


def nettoyerEtConvertirListeTexte(listeTexte, separateur=" "):
    return [nettoyerEtConvertirTexte(element, separateur) for element in listeTexte]
