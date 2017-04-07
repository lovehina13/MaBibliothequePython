# coding: utf-8

#===============================================================================
# Name        : ComparaisonFichier.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (07/04/2017)
# Description : Comparaison de fichiers
#===============================================================================

def comparerFichiers(fichier1, fichier2, resultat, precision, caractere=" "):
    from ComparaisonElements import identiques
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import joindreEtConvertirTexte, separerEtConvertirListeTexte
    from math import fabs
    from xml.etree import ElementTree

    html = ElementTree.Element("html")
    head = ElementTree.SubElement(html, "head")
    body = ElementTree.SubElement(html, "body")

    titre = str("Comparaison de %s et %s avec une précision de %e" % (fichier1, fichier2, precision)).decode("utf-8")
    head_title = ElementTree.SubElement(head, "title")
    head_title.text = titre
    body_h1 = ElementTree.SubElement(body, "h1")
    body_h1.text = titre

    lignes1 = separerEtConvertirListeTexte(lireFichier(fichier1), caractere)
    lignes2 = separerEtConvertirListeTexte(lireFichier(fichier2), caractere)
    nbLignes1 = len(lignes1)
    nbLignes2 = len(lignes2)
    if nbLignes1 != nbLignes2:
        note = str("Nombre de lignes différent").decode("utf-8")
        contexte1 = str("Contexte 1 = %d" % (nbLignes1)).decode("utf-8")
        contexte2 = str("Contexte 2 = %d" % (nbLignes2)).decode("utf-8")
        construireDifference(body, note, contexte1, contexte2)
    else:
        for itLigne in range(nbLignes1):
            elements1 = lignes1[itLigne]
            elements2 = lignes2[itLigne]
            nbElements1 = len(elements1)
            nbElements2 = len(elements2)
            if nbElements1 != nbElements2:
                note = str("Ligne %d : nombre d'éléments différent" % (itLigne + 1)).decode("utf-8")
                contexte1 = str("Contexte 1 = %s" % (joindreEtConvertirTexte(elements1, caractere))).decode("utf-8")
                contexte2 = str("Contexte 2 = %s" % (joindreEtConvertirTexte(elements2, caractere))).decode("utf-8")
                construireDifference(body, note, contexte1, contexte2)
            else:
                for itElement in range(nbElements1):
                    element1 = elements1[itElement]
                    element2 = elements2[itElement]
                    if not identiques(element1, element2):
                        if isinstance(element1, str) or isinstance(element2, str):
                            note = str("Ligne %d : élément %d différent" % (itLigne + 1, itElement + 1)).decode("utf-8")
                            contexte1 = str("Contexte 1 = %s" % (element1)).decode("utf-8")
                            contexte2 = str("Contexte 2 = %s" % (element2)).decode("utf-8")
                            construireDifference(body, note, contexte1, contexte2)
                        else:
                            try:
                                ecart = fabs(element1 - element2) / min(fabs(element1), fabs(element2))
                            except ZeroDivisionError:
                                ecart = fabs(element1 - element2)
                            if ecart > precision:
                                note = str("Ligne %d : précision de l'élément %d non respectée, écart relatif de %e" % (itLigne + 1, itElement + 1, ecart)).decode("utf-8")
                                contexte1 = str("Contexte 1 = %s" % (element1)).decode("utf-8")
                                contexte2 = str("Contexte 2 = %s" % (element2)).decode("utf-8")
                                construireDifference(body, note, contexte1, contexte2)

    arbre = ElementTree.ElementTree(html)
    arbre.write(resultat)

def construireDifference(parent, note, contexte1, contexte2):
    from xml.etree import ElementTree
    p1 = ElementTree.SubElement(parent, "p")
    ul = ElementTree.SubElement(parent, "ul")
    li1 = ElementTree.SubElement(ul, "li")
    li2 = ElementTree.SubElement(ul, "li")
    p2 = ElementTree.SubElement(ul, "p")
    p1.text = note
    li1.text = contexte1
    li2.text = contexte2
    p2.text = str("Commentaire ...").decode("utf-8")
