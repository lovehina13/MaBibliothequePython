//==============================================================================
// Name        : ClasseMere.h
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Header file of the ClasseMere class
//==============================================================================

#ifndef CLASSEMERE_H
#define CLASSEMERE_H

#include "ClasseValeurs.h"
#include <map>
#include <string>
#include <vector>

class ClasseMere
{
public:
    // Constructeurs et destructeurs
    ClasseMere();
    ClasseMere(const std::string& nom, const ClasseValeurs& valeurs);
    ClasseMere(const ClasseMere& classeMere);
    virtual ~ClasseMere();

    // Getters
    const std::string& getNom() const;
    const ClasseValeurs& getValeurs() const;

    // Setters
    void setNom(const std::string& nom);
    void setValeurs(const ClasseValeurs& valeurs);

    // Méthodes génériques
    void clear();
    void set(const std::string& nom, const ClasseValeurs& valeurs);
    void copy(const ClasseMere& classeMere);
    bool equals(const ClasseMere& classeMere) const;
    void fromString(const std::string& fromString, const char& sep);
    const std::string toString(const char& sep) const;

    // Méthodes spécifiques
    // TODO Méthodes spécifiques de la classe 'ClasseMere'

private:
    // Membres de classe
    std::string nom;
    ClasseValeurs valeurs;
};

typedef ClasseMere* PtrClasseMere;
typedef std::vector<ClasseMere> ListeClasseMere_;
typedef std::vector<PtrClasseMere> ListePtrClasseMere_;
typedef std::map<int, ClasseMere> MapIdClasseMere_;
typedef std::map<int, PtrClasseMere> MapIdPtrClasseMere_;
typedef std::map<std::string, ClasseMere> MapNomsClasseMere_;
typedef std::map<std::string, PtrClasseMere> MapNomsPtrClasseMere_;

#endif // CLASSEMERE_H
