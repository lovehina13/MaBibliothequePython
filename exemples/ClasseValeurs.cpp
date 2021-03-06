//==============================================================================
// Name        : ClasseValeurs.cpp
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Source file of the ClasseValeurs class
//==============================================================================

#include "ClasseValeurs.h"

ClasseValeurs::ClasseValeurs() :
        nombreEntier(0), nombreReel(0.0), texte(std::string())
{
    this->clear();
}

ClasseValeurs::ClasseValeurs(const int& nombreEntier, const double& nombreReel, const std::string& texte) :
        ClasseValeurs()
{
    this->set(nombreEntier, nombreReel, texte);
}

ClasseValeurs::ClasseValeurs(const ClasseValeurs& classeValeurs) :
        ClasseValeurs()
{
    this->copy(classeValeurs);
}

ClasseValeurs::~ClasseValeurs()
{

}

ClasseValeurs& ClasseValeurs::operator=(const ClasseValeurs& classeValeurs)
{
    this->copy(classeValeurs);
    return *this;
}

bool ClasseValeurs::operator==(const ClasseValeurs& classeValeurs) const
{
    return this->equals(classeValeurs);
}

bool ClasseValeurs::operator!=(const ClasseValeurs& classeValeurs) const
{
    return !this->equals(classeValeurs);
}

const int& ClasseValeurs::getNombreEntier() const
{
    return this->nombreEntier;
}

const double& ClasseValeurs::getNombreReel() const
{
    return this->nombreReel;
}

const std::string& ClasseValeurs::getTexte() const
{
    return this->texte;
}

void ClasseValeurs::setNombreEntier(const int& nombreEntier)
{
    this->nombreEntier = nombreEntier;
}

void ClasseValeurs::setNombreReel(const double& nombreReel)
{
    this->nombreReel = nombreReel;
}

void ClasseValeurs::setTexte(const std::string& texte)
{
    this->texte = texte;
}

void ClasseValeurs::clear()
{
    this->set(0, 0.0, std::string());
}

void ClasseValeurs::set(const int& nombreEntier, const double& nombreReel, const std::string& texte)
{
    this->setNombreEntier(nombreEntier);
    this->setNombreReel(nombreReel);
    this->setTexte(texte);
}

void ClasseValeurs::copy(const ClasseValeurs& classeValeurs)
{
    this->set(classeValeurs.getNombreEntier(), classeValeurs.getNombreReel(), classeValeurs.getTexte());
}

bool ClasseValeurs::equals(const ClasseValeurs& classeValeurs) const
{
    if (this->getNombreEntier() != classeValeurs.getNombreEntier())
        return false;
    if (this->getNombreReel() != classeValeurs.getNombreReel())
        return false;
    if (this->getTexte() != classeValeurs.getTexte())
        return false;
    return true;
}

void ClasseValeurs::fromString(const std::string& fromString, const char& sep)
{
    // TODO void ClasseValeurs::fromString(const std::string& fromString, const char& sep)
#warning "'void ClasseValeurs::fromString(const std::string& fromString, const char& sep)' not implemented"
}

const std::string ClasseValeurs::toString(const char& sep) const
{
    // TODO const std::string ClasseValeurs::toString(const char& sep) const
#warning "'const std::string ClasseValeurs::toString(const char& sep) const' not implemented"
    return std::string();
}
