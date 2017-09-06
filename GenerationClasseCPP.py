# coding: utf-8

#===============================================================================
# Name        : GenerationClasseCPP.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (31/07/2017)
# Description : Génération de classe C++
#===============================================================================

# Classe de définition d'un auteur

class Auteur(object):
    def __init__(self, prenom, nom, email):
        self.prenom = prenom
        self.nom = nom
        self.email = email

# Classe de définition d'une version

class Version(object):
    def __init__(self, numero, date):
        self.numero = numero
        self.date = date

# Classe abstraite de définition d'un membre

class Membre(object):
    def __init__(self, nom, type, mode=""):
        self.nom = nom
        self.type = type
        self.mode = mode
    def get_declaration(self):
        return "%s%s %s" % (self.type, self.mode, self.nom)
    def get_parametre(self):
        return "const %s%s %s" % (self.type, "&" if not self.estPointeur() else "*", self.nom)
    def get_valeur_defaut(self):
        if self.estPointeur():
            return "0"
        elif self.estNatif():
            if self.type in ["bool"]:
                return "false"
            if self.type in ["char", "int", "unsigned int"]:
                return "0"
            if self.type in ["float", "double", "unsigned float", "unsigned double"]:
                return "0.0"
        else:
            return "%s()" % (self.type)
    def get_initialisation(self):
        return "%s(%s)" % (self.nom, self.get_valeur_defaut())
    def get_getter(self): pass  # Méthode virtuelle pure
    def get_setter(self): pass  # Méthode virtuelle pure
    def estPointeur(self):
        return self.mode == "*"
    def estReference(self):
        return self.mode == "&"
    def estNatif(self):
        return self.type in ["bool", "char", "int", "float", "double", "unsigned int", "unsigned float", "unsigned double"]
    def estStandard(self):
        return self.type.startswith("std::string") or self.type.startswith("std::vector") or self.type.startswith("std::map")
    def nomMajuscule(self):
        return str(self.nom[0].upper() + self.nom[1:])

# Classe de définition d'un membre dans le fichier d'entête

class Membre_Entete(Membre):
    def __init__(self, nom, type, mode=""):
        super(Membre_Entete, self).__init__(nom, type, mode)
    def get_getter(self):
        return "const %s%s get%s() const" % (self.type, "&" if not self.estPointeur() else "*", self.nomMajuscule())
    def get_setter(self):
        return "void set%s(%s)" % (self.nomMajuscule(), self.get_parametre())

# Classe de définition d'un membre dans le fichier source

class Membre_Source(Membre):
    def __init__(self, nom, type, mode=""):
        super(Membre_Source, self).__init__(nom, type, mode)
    def get_getter(self, classe):
        return "const %s%s %s::get%s() const\n{\n    return this->%s;\n}" % (self.type, "&" if not self.estPointeur() else "*", classe.nom, self.nomMajuscule(), self.nom)
    def get_setter(self, classe):
        return "void %s::set%s(%s)\n{\n    this->%s = %s%s;\n}" % (classe.nom, self.nomMajuscule(), self.get_parametre(), self.nom, "" if not self.estPointeur() else "(%s*) " % (self.type), self.nom)

# Classe abstraite de définition d'une classe

class Classe(object):
    def __init__(self, nom, heritage=None, membres=None, auteur=None, version=None):
        self.nom = nom
        self.heritage = heritage
        self.membres = membres if membres is not None else []
        self.auteur = auteur if auteur is not None else Auteur("FirstName", "LastName", "FirstName.LastName@DomainName.DomaineExt")
        self.version = version if version is not None else Version("1.0.0", "DD/MM/YYYY")
    def get_parametre(self):
        return "const %s& %s" % (self.nom, self.nomMinuscule())
    def get_inclusions(self):
        inclusions = []
        if self.heritage is not None:
            inclusions.append(self.heritage)
        for membre in self.membres:
            if membre.estNatif() or membre.estStandard():
                continue
            if membre.type not in inclusions:
                inclusions.append(membre.type)
        return sorted(inclusions)
    def get_membres(self):
        membres = str()
        for membre in self.membres:
            membres += membre.nom + ", "
        return membres.rstrip(", ")
    def get_membres_parametres(self):
        membres = str()
        for membre in self.membres:
            membres += membre.get_parametre() + ", "
        return membres.rstrip(", ")
    def get_membres_valeurs_defaut(self):
        membres = str()
        for membre in self.membres:
            membres += membre.get_valeur_defaut() + ", "
        return membres.rstrip(", ")
    def get_membres_initialisations(self):
        membres = str()
        for membre in self.membres:
            if membre.estNatif() or membre.estPointeur():
                membres += membre.get_initialisation() + ", "
        return membres.rstrip(", ")
    def gen_classe(self): pass  # Méthode virtuelle pure
    def gen_entete(self): pass  # Méthode virtuelle pure
    def gen_inclusions(self): pass  # Méthode virtuelle pure
    def gen_constructeurs(self): pass  # Méthode virtuelle pure
    def gen_getters(self): pass  # Méthode virtuelle pure
    def gen_setters(self): pass  # Méthode virtuelle pure
    def gen_methodes_generiques(self): pass  # Méthode virtuelle pure
    def gen_methodes_specifiques(self): pass  # Méthode virtuelle pure
    def gen_membres(self): pass  # Méthode virtuelle pure
    def gen_structures(self): pass  # Méthode virtuelle pure
    def nomMinuscule(self):
        return str(self.nom[0].lower() + self.nom[1:])
    def nomMajuscules(self):
        return str(self.nom.upper())

# Classe de définition d'une classe dans le fichier d'entête

class Classe_Entete(Classe):
    def __init__(self, nom, heritage=None, membres=None, auteur=None, version=None):
        super(Classe_Entete, self).__init__(nom, heritage, membres, auteur, version)
    def gen_classe(self):
        texte = str()
        texte += self.gen_entete() + "\n"
        texte += self.gen_definition_debut() + "\n"
        texte += self.gen_inclusions() + "\n"
        texte += self.gen_classe_debut() + "\n"
        texte += self.gen_constructeurs() + "\n"
        texte += self.gen_getters() + "\n"
        texte += self.gen_setters() + "\n"
        texte += self.gen_methodes_generiques() + "\n"
        texte += self.gen_methodes_specifiques() + "\n"
        texte += self.gen_membres() + "\n"
        texte += self.gen_classe_fin() + "\n"
        texte += self.gen_structures() + "\n"
        texte += self.gen_definition_fin() + "\n"
        return texte
    def gen_entete(self):
        texte = str()
        texte += "//==============================================================================" + "\n"
        texte += "// Name        : %s.h" % (self.nom) + "\n"
        texte += "// Author      : %s %s (%s)" % (self.auteur.prenom, self.auteur.nom, self.auteur.email) + "\n"
        texte += "// Version     : %s (%s)" % (self.version.numero, self.version.date) + "\n"
        texte += "// Description : Header file of the %s class" % (self.nom) + "\n"
        texte += "//==============================================================================" + "\n"
        return texte
    def gen_definition_debut(self):
        texte = str()
        texte += "#ifndef %s_H" % (self.nomMajuscules()) + "\n"
        texte += "#define %s_H" % (self.nomMajuscules()) + "\n"
        return texte
    def gen_inclusions(self):
        texte = str()
        for inclusion in self.get_inclusions():
            texte += "#include \"%s.h\"" % (inclusion) + "\n"
        texte += "#include <map>" + "\n"
        texte += "#include <string>" + "\n"
        texte += "#include <vector>" + "\n"
        return texte
    def gen_classe_debut(self):
        texte = str()
        if self.heritage is None:
            texte += "class %s" % (self.nom) + "\n"
        else:
            texte += "class %s : public %s" % (self.nom, self.heritage) + "\n"
        texte += "{" + "\n"
        texte += "public:" + "\n"
        return texte.rstrip("\n")
    def gen_constructeurs(self):
        texte = str()
        texte += "    // Constructeurs et destructeurs" + "\n"
        texte += "    %s();" % (self.nom) + "\n"
        texte += "    %s(%s);" % (self.nom, self.get_membres_parametres()) + "\n"
        texte += "    %s(%s);" % (self.nom, self.get_parametre()) + "\n"
        texte += "    virtual ~%s();" % (self.nom) + "\n"
        return texte
    def gen_getters(self):
        texte = str()
        texte += "    // Getters" + "\n"
        for membre in self.membres:
            texte += "    %s;" % (membre.get_getter()) + "\n"
        return texte
    def gen_setters(self):
        texte = str()
        texte += "    // Setters" + "\n"
        for membre in self.membres:
            texte += "    %s;" % (membre.get_setter()) + "\n"
        return texte
    def gen_methodes_generiques(self):
        texte = str()
        texte += "    // Méthodes génériques" + "\n"
        texte += "    void clear();" + "\n"
        texte += "    void set(%s);" % (self.get_membres_parametres()) + "\n"
        texte += "    void copy(%s);" % (self.get_parametre()) + "\n"
        texte += "    bool equals(%s) const;" % (self.get_parametre()) + "\n"
        texte += "    void fromString(const std::string& fromString, const char& sep);" + "\n"
        texte += "    const std::string toString(const char& sep) const;" + "\n"
        return texte
    def gen_methodes_specifiques(self):
        texte = str()
        texte += "    // Méthodes spécifiques" + "\n"
        texte += "    // TODO Méthodes spécifiques de la classe '%s'" % (self.nom) + "\n"
        return texte
    def gen_membres(self):
        texte = str()
        texte += "private:" + "\n"
        texte += "    // Membres de classe" + "\n"
        for membre in self.membres:
            texte += "    %s;" % (membre.get_declaration()) + "\n"
        return texte.rstrip("\n")
    def gen_classe_fin(self):
        texte = str()
        texte += "};" + "\n"
        return texte
    def gen_structures(self):
        texte = str()
        texte += "typedef %s* Ptr%s;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::vector<%s> Liste%s_;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::vector<Ptr%s> ListePtr%s_;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::map<int, %s> MapId%s_;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::map<int, Ptr%s> MapIdPtr%s_;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::map<std::string, %s> MapNoms%s_;" % (self.nom, self.nom) + "\n"
        texte += "typedef std::map<std::string, Ptr%s> MapNomsPtr%s_;" % (self.nom, self.nom) + "\n"
        return texte
    def gen_definition_fin(self):
        texte = str()
        texte += "#endif // %s_H" % (self.nomMajuscules()) + "\n"
        return texte.rstrip("\n")

# Classe de définition d'une classe dans le fichier source

class Classe_Source(Classe):
    def __init__(self, nom, heritage=None, membres=None, auteur=None, version=None):
        super(Classe_Source, self).__init__(nom, heritage, membres, auteur, version)
    def get_membres_getters(self):
        membres = str()
        for membre in self.membres:
            membres += "%s.get%s()" % (self.nomMinuscule(), membre.nomMajuscule()) + ", "
        return membres.rstrip(", ")
    def get_membres_setters(self):
        membres = str()
        for membre in self.membres:
            membres += "    this->set%s(%s);" % (membre.nomMajuscule(), membre.nom) + "\n"
        return membres.rstrip("\n")
    def get_membres_comparaisons(self):
        membres = str()
        for membre in self.membres:
            if membre.estNatif() or membre.estStandard():
                membres += "    if (this->get%s() != %s.get%s())" % (membre.nomMajuscule(), self.nomMinuscule(), membre.nomMajuscule()) + "\n"
            elif not membre.estPointeur():
                membres += "    if (!this->get%s().equals(%s.get%s()))" % (membre.nomMajuscule(), self.nomMinuscule(), membre.nomMajuscule()) + "\n"
            else:
                membres += "    if (!this->get%s()->equals(*%s.get%s()))" % (membre.nomMajuscule(), self.nomMinuscule(), membre.nomMajuscule()) + "\n"
            membres += "        return false;" + "\n"
        return membres.rstrip("\n")
    def gen_classe(self):
        texte = str()
        texte += self.gen_entete() + "\n"
        texte += self.gen_inclusions() + "\n"
        texte += self.gen_constructeurs() + "\n"
        texte += self.gen_getters() + "\n"
        texte += self.gen_setters() + "\n"
        texte += self.gen_methodes_generiques() + "\n"
        return texte
    def gen_entete(self):
        texte = str()
        texte += "//==============================================================================" + "\n"
        texte += "// Name        : %s.cpp" % (self.nom) + "\n"
        texte += "// Author      : %s %s (%s)" % (self.auteur.prenom, self.auteur.nom, self.auteur.email) + "\n"
        texte += "// Version     : %s (%s)" % (self.version.numero, self.version.date) + "\n"
        texte += "// Description : Source file of the %s class" % (self.nom) + "\n"
        texte += "//==============================================================================" + "\n"
        return texte
    def gen_inclusions(self):
        texte = str()
        texte += "#include \"%s.h\"" % (self.nom) + "\n"
        return texte
    def gen_constructeurs(self):
        texte = str()
        texte += "%s::%s()%s\n{\n    this->clear();\n}" % (self.nom, self.nom, " :\n        %s" % (self.get_membres_initialisations()) if self.get_membres_initialisations() != "" else "") + "\n\n"
        texte += "%s::%s(%s) :\n        %s()\n{\n    this->set(%s);\n}" % (self.nom, self.nom, self.get_membres_parametres(), self.nom, self.get_membres()) + "\n\n"
        texte += "%s::%s(%s) :\n        %s()\n{\n    this->copy(%s);\n}" % (self.nom, self.nom, self.get_parametre(), self.nom, self.nomMinuscule()) + "\n\n"
        texte += "%s::~%s()\n{\n\n}" % (self.nom, self.nom) + "\n"
        return texte
    def gen_getters(self):
        texte = str()
        for membre in self.membres:
            texte += membre.get_getter(self) + "\n\n"
        return texte.rstrip("\n") + "\n"
    def gen_setters(self):
        texte = str()
        for membre in self.membres:
            texte += membre.get_setter(self) + "\n\n"
        return texte.rstrip("\n") + "\n"
    def gen_methodes_generiques(self):
        texte = str()
        texteClear = "    this->set(%s);" % (self.get_membres_valeurs_defaut()) + "\n"
        texteSet = "%s" % (self.get_membres_setters()) + "\n"
        texteCopy = "    this->set(%s);" % (self.get_membres_getters()) + "\n"
        texteEquals = "%s\n    return true;" % (self.get_membres_comparaisons()) + "\n"
        texteFromString = str()
        texteFromString += "    // TODO void %s::fromString(const std::string& fromString, const char& sep)" % (self.nom) + "\n"
        texteFromString += "#warning \"'void %s::fromString(const std::string& fromString, const char& sep)' not implemented\"" % (self.nom) + "\n"
        texteToString = str()
        texteToString += "    // TODO const std::string %s::toString(const char& sep) const" % (self.nom) + "\n"
        texteToString += "#warning \"'const std::string %s::toString(const char& sep) const' not implemented\"" % (self.nom) + "\n"
        texteToString += "    return std::string();" + "\n"
        texte += "void %s::clear()\n{\n%s\n}" % (self.nom, texteClear.rstrip("\n")) + "\n\n"
        texte += "void %s::set(%s)\n{\n%s\n}" % (self.nom, self.get_membres_parametres(), texteSet.rstrip("\n")) + "\n\n"
        texte += "void %s::copy(%s)\n{\n%s\n}" % (self.nom, self.get_parametre(), texteCopy.rstrip("\n")) + "\n\n"
        texte += "bool %s::equals(%s) const\n{\n%s\n}" % (self.nom, self.get_parametre(), texteEquals.rstrip("\n")) + "\n\n"
        texte += "void %s::fromString(const std::string& fromString, const char& sep)\n{\n%s\n}" % (self.nom, texteFromString.rstrip("\n")) + "\n\n"
        texte += "const std::string %s::toString(const char& sep) const\n{\n%s\n}" % (self.nom, texteToString.rstrip("\n")) + "\n\n"
        return texte.rstrip("\n")
    def gen_methodes_specifiques(self):
        return str()
    def gen_membres(self):
        return str()
    def gen_structures(self):
        return str()

# Programme principal

from LectureEcritureFichier import lireFichier, ecrireFichier
import os, sys

if __name__ == "__main__":
    fichierDefinitions = sys.argv[1]
    repertoireEntetes = sys.argv[2]
    repertoireSources = sys.argv[3]
    if not os.path.isdir(repertoireEntetes):
        os.mkdir(repertoireEntetes)
    if not os.path.isdir(repertoireSources):
        os.mkdir(repertoireSources)
    lignes = lireFichier(fichierDefinitions)
    auteur = Auteur("FirstName", "LastName", "FirstName.LastName@DomainName.DomaineExt")
    version = Version("1.0.0", "DD/MM/YYYY")
    classe = Classe(None)
    for ligne in lignes:
        if ligne.startswith("a"):
            ligne = ligne.lstrip("a").lstrip()
            auteur = Auteur(ligne.split(";")[0], ligne.split(";")[1], ligne.split(";")[2])
        elif ligne.startswith("v"):
            ligne = ligne.lstrip("v").lstrip()
            version = Version(ligne.split(";")[0], ligne.split(";")[1])
        elif ligne.startswith("c"):
            ligne = ligne.lstrip("c").lstrip()
            classe = Classe(None)
            classe.nom = ligne
        elif ligne.startswith("h"):
            ligne = ligne.lstrip("h").lstrip()
            classe.heritage = ligne
        elif ligne.startswith("m"):
            ligne = ligne.lstrip("m").lstrip()
            membre = Membre(None, None, "")
            membre.nom = ligne.split()[len(ligne.split()) - 1]
            membre.type = " ".join(ligne.replace("*", "").replace("&", "").split()[:len(ligne.split()) - 1])
            if "*" in ligne:
                membre.mode = "*"
            elif "&" in ligne:
                membre.mode = "&"
            classe.membres.append(membre)
        elif ligne.strip() == "" and classe.nom is not None:
            membres_entete = []
            membres_source = []
            for membre in classe.membres:
                membre_entete = Membre_Entete(membre.nom, membre.type, membre.mode)
                membre_source = Membre_Source(membre.nom, membre.type, membre.mode)
                membres_entete.append(membre_entete)
                membres_source.append(membre_source)
            classe_entete = Classe_Entete(classe.nom, classe.heritage, membres_entete, auteur, version)
            classe_source = Classe_Source(classe.nom, classe.heritage, membres_source, auteur, version)
            print "Génération du fichier %s/%s.h" % (repertoireEntetes, classe.nom)
            print "Génération du fichier %s/%s.cpp" % (repertoireSources, classe.nom)
            ecrireFichier("%s/%s.h" % (repertoireEntetes, classe_entete.nom), classe_entete.gen_classe().split("\n"))
            ecrireFichier("%s/%s.cpp" % (repertoireSources, classe_source.nom), classe_source.gen_classe().split("\n"))
