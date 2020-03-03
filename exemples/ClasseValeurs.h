//==============================================================================
// Name        : ClasseValeurs.h
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Header file of the ClasseValeurs class
//==============================================================================

#ifndef CLASSEVALEURS_H
#define CLASSEVALEURS_H

#include <map>
#include <string>
#include <vector>

class ClasseValeurs
{
public:
    // Constructeurs et destructeurs
    ClasseValeurs();
    ClasseValeurs(const int& nombreEntier, const double& nombreReel, const std::string& texte);
    ClasseValeurs(const ClasseValeurs& classeValeurs);
    virtual ~ClasseValeurs();

    // Opérateurs
    ClasseValeurs& operator=(const ClasseValeurs& classeValeurs);
    bool operator==(const ClasseValeurs& classeValeurs) const;
    bool operator!=(const ClasseValeurs& classeValeurs) const;

    // Getters
    const int& getNombreEntier() const;
    const double& getNombreReel() const;
    const std::string& getTexte() const;

    // Setters
    void setNombreEntier(const int& nombreEntier);
    void setNombreReel(const double& nombreReel);
    void setTexte(const std::string& texte);

    // Méthodes génériques
    void clear();
    void set(const int& nombreEntier, const double& nombreReel, const std::string& texte);
    void copy(const ClasseValeurs& classeValeurs);
    bool equals(const ClasseValeurs& classeValeurs) const;
    void fromString(const std::string& fromString, const char& sep);
    const std::string toString(const char& sep) const;

    // Méthodes spécifiques
    // TODO Méthodes spécifiques de la classe 'ClasseValeurs'

private:
    // Membres de classe
    int nombreEntier;
    double nombreReel;
    std::string texte;
};

typedef ClasseValeurs* PtrClasseValeurs;
typedef const ClasseValeurs* CPtrClasseValeurs;
typedef std::vector<ClasseValeurs> ListeClasseValeurs_;
typedef std::vector<PtrClasseValeurs> ListePtrClasseValeurs_;
typedef std::vector<CPtrClasseValeurs> ListeCPtrClasseValeurs_;
typedef std::map<int, ClasseValeurs> MapIdClasseValeurs_;
typedef std::map<int, PtrClasseValeurs> MapIdPtrClasseValeurs_;
typedef std::map<int, CPtrClasseValeurs> MapIdCPtrClasseValeurs_;
typedef std::map<std::string, ClasseValeurs> MapNomsClasseValeurs_;
typedef std::map<std::string, PtrClasseValeurs> MapNomsPtrClasseValeurs_;
typedef std::map<std::string, CPtrClasseValeurs> MapNomsCPtrClasseValeurs_;

#endif // CLASSEVALEURS_H
