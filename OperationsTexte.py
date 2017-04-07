# coding: utf-8

#===============================================================================
# Name        : OperationsTexte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (07/04/2017)
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

def separerTexte(texte, caractere=" "):
    return [element for element in texte.split(caractere) if element is not None]

def joindreTexte(texte, caractere=" "):
    return caractere.join(texte)

def nettoyerTexte(texte, caractere=" "):
    return joindreTexte(separerTexte(texte, caractere), caractere)

def separerListeTexte(listeTexte, caractere=" "):
    return [separerTexte(element, caractere) for element in listeTexte]

def joindreListeTexte(listeTexte, caractere=" "):
    return [joindreTexte(element, caractere) for element in listeTexte]

def nettoyerListeTexte(listeTexte, caractere=" "):
    return [nettoyerTexte(element, caractere) for element in listeTexte]

def separerEtConvertirTexte(texte, caractere=" "):
    return [convertirTexteEnNombre(element) for element in separerTexte(texte, caractere)]

def joindreEtConvertirTexte(texte, caractere=" "):
    return joindreTexte([convertirNombreEnTexte(element) for element in texte], caractere)

def nettoyerEtConvertirTexte(texte, caractere=" "):
    return joindreEtConvertirTexte(separerEtConvertirTexte(texte, caractere), caractere)

def separerEtConvertirListeTexte(listeTexte, caractere=" "):
    return [separerEtConvertirTexte(element, caractere) for element in listeTexte]

def joindreEtConvertirListeTexte(listeTexte, caractere=" "):
    return [joindreEtConvertirTexte(element, caractere) for element in listeTexte]

def nettoyerEtConvertirListeTexte(listeTexte, caractere=" "):
    return [nettoyerEtConvertirTexte(element, caractere) for element in listeTexte]
