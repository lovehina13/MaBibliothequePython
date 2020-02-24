//==============================================================================
// Name        : ClasseMere.cpp
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Source file of the ClasseMere class
//==============================================================================

#include "ClasseMere.h"

ClasseMere::ClasseMere() :
        nom(std::string()), valeurs(ClasseValeurs())
{
    this->clear();
}

ClasseMere::ClasseMere(const std::string& nom, const ClasseValeurs& valeurs) :
        ClasseMere()
{
    this->set(nom, valeurs);
}

ClasseMere::ClasseMere(const ClasseMere& classeMere) :
        ClasseMere()
{
    this->copy(classeMere);
}

ClasseMere::~ClasseMere()
{

}

ClasseMere& ClasseMere::operator=(const ClasseMere& classeMere)
{
    this->copy(classeMere);
    return *this;
}

bool ClasseMere::operator==(const ClasseMere& classeMere) const
{
    return this->equals(classeMere);
}

bool ClasseMere::operator!=(const ClasseMere& classeMere) const
{
    return !this->equals(classeMere);
}

const std::string& ClasseMere::getNom() const
{
    return this->nom;
}

const ClasseValeurs& ClasseMere::getValeurs() const
{
    return this->valeurs;
}

void ClasseMere::setNom(const std::string& nom)
{
    this->nom = nom;
}

void ClasseMere::setValeurs(const ClasseValeurs& valeurs)
{
    this->valeurs = valeurs;
}

void ClasseMere::clear()
{
    this->set(std::string(), ClasseValeurs());
}

void ClasseMere::set(const std::string& nom, const ClasseValeurs& valeurs)
{
    this->setNom(nom);
    this->setValeurs(valeurs);
}

void ClasseMere::copy(const ClasseMere& classeMere)
{
    this->set(classeMere.getNom(), classeMere.getValeurs());
}

bool ClasseMere::equals(const ClasseMere& classeMere) const
{
    if (this->getNom() != classeMere.getNom())
        return false;
    if (this->getValeurs() != classeMere.getValeurs())
        return false;
    return true;
}

void ClasseMere::fromString(const std::string& fromString, const char& sep)
{
    // TODO void ClasseMere::fromString(const std::string& fromString, const char& sep)
#warning "'void ClasseMere::fromString(const std::string& fromString, const char& sep)' not implemented"
}

const std::string ClasseMere::toString(const char& sep) const
{
    // TODO const std::string ClasseMere::toString(const char& sep) const
#warning "'const std::string ClasseMere::toString(const char& sep) const' not implemented"
    return std::string();
}
