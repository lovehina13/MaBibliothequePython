//==============================================================================
// Name        : ClassePointeurs.h
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Header file of the ClassePointeurs class
//==============================================================================

#ifndef CLASSEPOINTEURS_H
#define CLASSEPOINTEURS_H

#include <map>
#include <string>
#include <vector>

class ClassePointeurs
{
public:
    // Constructeurs et destructeurs
    ClassePointeurs();
    ClassePointeurs(const int* pointeurNombreEntier, const double* pointeurNombreReel, const std::string* pointeurTexte);
    ClassePointeurs(const ClassePointeurs& classePointeurs);
    virtual ~ClassePointeurs();

    // Opérateurs
    ClassePointeurs& operator=(const ClassePointeurs& classePointeurs);
    bool operator==(const ClassePointeurs& classePointeurs) const;
    bool operator!=(const ClassePointeurs& classePointeurs) const;

    // Getters
    const int* getPointeurNombreEntier() const;
    const double* getPointeurNombreReel() const;
    const std::string* getPointeurTexte() const;

    // Setters
    void setPointeurNombreEntier(const int* pointeurNombreEntier);
    void setPointeurNombreReel(const double* pointeurNombreReel);
    void setPointeurTexte(const std::string* pointeurTexte);

    // Méthodes génériques
    void clear();
    void set(const int* pointeurNombreEntier, const double* pointeurNombreReel, const std::string* pointeurTexte);
    void copy(const ClassePointeurs& classePointeurs);
    bool equals(const ClassePointeurs& classePointeurs) const;
    void fromString(const std::string& fromString, const char& sep);
    const std::string toString(const char& sep) const;

    // Méthodes spécifiques
    // TODO Méthodes spécifiques de la classe 'ClassePointeurs'

private:
    // Membres de classe
    int* pointeurNombreEntier;
    double* pointeurNombreReel;
    std::string* pointeurTexte;
};

typedef ClassePointeurs* PtrClassePointeurs;
typedef const ClassePointeurs* CPtrClassePointeurs;
typedef std::vector<ClassePointeurs> ListeClassePointeurs_;
typedef std::vector<PtrClassePointeurs> ListePtrClassePointeurs_;
typedef std::vector<CPtrClassePointeurs> ListeCPtrClassePointeurs_;
typedef std::map<int, ClassePointeurs> MapIdClassePointeurs_;
typedef std::map<int, PtrClassePointeurs> MapIdPtrClassePointeurs_;
typedef std::map<int, CPtrClassePointeurs> MapIdCPtrClassePointeurs_;
typedef std::map<std::string, ClassePointeurs> MapNomsClassePointeurs_;
typedef std::map<std::string, PtrClassePointeurs> MapNomsPtrClassePointeurs_;
typedef std::map<std::string, CPtrClassePointeurs> MapNomsCPtrClassePointeurs_;

#endif // CLASSEPOINTEURS_H
