//==============================================================================
// Name        : ClasseFille.h
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Header file of the ClasseFille class
//==============================================================================

#ifndef CLASSEFILLE_H
#define CLASSEFILLE_H

#include "ClasseMere.h"
#include "ClassePointeurs.h"
#include <map>
#include <string>
#include <vector>

class ClasseFille : public ClasseMere
{
public:
    // Constructeurs et destructeurs
    ClasseFille();
    ClasseFille(const ClasseMere& classeMere, const ClassePointeurs* pointeurs);
    ClasseFille(const ClasseFille& classeFille);
    virtual ~ClasseFille();

    // Opérateurs
    ClasseFille& operator=(const ClasseFille& classeFille);
    bool operator==(const ClasseFille& classeFille) const;
    bool operator!=(const ClasseFille& classeFille) const;

    // Getters
    const ClassePointeurs* getPointeurs() const;

    // Setters
    void setPointeurs(const ClassePointeurs* pointeurs);

    // Méthodes génériques
    void clear();
    void set(const ClasseMere& classeMere, const ClassePointeurs* pointeurs);
    void copy(const ClasseFille& classeFille);
    bool equals(const ClasseFille& classeFille) const;
    void fromString(const std::string& fromString, const char& sep);
    const std::string toString(const char& sep) const;

    // Méthodes spécifiques
    // TODO Méthodes spécifiques de la classe 'ClasseFille'

private:
    // Membres de classe
    ClassePointeurs* pointeurs;
};

typedef ClasseFille* PtrClasseFille;
typedef std::vector<ClasseFille> ListeClasseFille_;
typedef std::vector<PtrClasseFille> ListePtrClasseFille_;
typedef std::map<int, ClasseFille> MapIdClasseFille_;
typedef std::map<int, PtrClasseFille> MapIdPtrClasseFille_;
typedef std::map<std::string, ClasseFille> MapNomsClasseFille_;
typedef std::map<std::string, PtrClasseFille> MapNomsPtrClasseFille_;

#endif // CLASSEFILLE_H
