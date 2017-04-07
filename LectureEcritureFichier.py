# coding: utf-8

#===============================================================================
# Name        : LectureEcritureFichier.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (07/04/2017)
# Description : Lecture et écriture de fichier
#===============================================================================

def lireFichier(nomFichier):
    instanceFichier = open(nomFichier, "r")
    lignesFichier = instanceFichier.readlines()
    instanceFichier.close()
    lignesFichierEdit = []
    for ligneFichier in lignesFichier:
        ligneFichierEdit = str(ligneFichier).strip("\n")
        lignesFichierEdit.append(ligneFichierEdit)
    return lignesFichierEdit

def ecrireFichier(nomFichier, lignesFichier):
    instanceFichier = open(nomFichier, "w")
    for ligneFichier in lignesFichier:
        ligneFichierEdit = str("%s\n" % str(ligneFichier))
        instanceFichier.write(ligneFichierEdit)
    instanceFichier.close()
