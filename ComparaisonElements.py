# coding: utf-8

#===============================================================================
# Name        : ComparaisonElements.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (07/04/2017)
# Description : Comparaison d'éléments
#===============================================================================

def identiques(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for it in range(0, len(a)):
            if not identiques(a[it], b[it]):
                return False
        return True
    if isinstance(a, dict) and isinstance(b, dict):
        if len(a) != len(b):
            return False
        for it in a.keys():
            if not b.has_key(it):
                return False
            if not identiques(a[it], b[it]):
                return False
        return True
    if isinstance(a, float) and isinstance(b, float):
        return str("%.16e" % (a)) == str("%.16e" % (b))
    return a == b
