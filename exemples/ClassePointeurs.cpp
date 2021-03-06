//==============================================================================
// Name        : ClassePointeurs.cpp
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Source file of the ClassePointeurs class
//==============================================================================

#include "ClassePointeurs.h"

ClassePointeurs::ClassePointeurs() :
        pointeurNombreEntier(nullptr), pointeurNombreReel(nullptr), pointeurTexte(nullptr)
{
    this->clear();
}

ClassePointeurs::ClassePointeurs(const int* pointeurNombreEntier, const double* pointeurNombreReel, const std::string* pointeurTexte) :
        ClassePointeurs()
{
    this->set(pointeurNombreEntier, pointeurNombreReel, pointeurTexte);
}

ClassePointeurs::ClassePointeurs(const ClassePointeurs& classePointeurs) :
        ClassePointeurs()
{
    this->copy(classePointeurs);
}

ClassePointeurs::~ClassePointeurs()
{

}

ClassePointeurs& ClassePointeurs::operator=(const ClassePointeurs& classePointeurs)
{
    this->copy(classePointeurs);
    return *this;
}

bool ClassePointeurs::operator==(const ClassePointeurs& classePointeurs) const
{
    return this->equals(classePointeurs);
}

bool ClassePointeurs::operator!=(const ClassePointeurs& classePointeurs) const
{
    return !this->equals(classePointeurs);
}

const int* ClassePointeurs::getPointeurNombreEntier() const
{
    return this->pointeurNombreEntier;
}

const double* ClassePointeurs::getPointeurNombreReel() const
{
    return this->pointeurNombreReel;
}

const std::string* ClassePointeurs::getPointeurTexte() const
{
    return this->pointeurTexte;
}

void ClassePointeurs::setPointeurNombreEntier(const int* pointeurNombreEntier)
{
    this->pointeurNombreEntier = const_cast<int*>(pointeurNombreEntier);
}

void ClassePointeurs::setPointeurNombreReel(const double* pointeurNombreReel)
{
    this->pointeurNombreReel = const_cast<double*>(pointeurNombreReel);
}

void ClassePointeurs::setPointeurTexte(const std::string* pointeurTexte)
{
    this->pointeurTexte = const_cast<std::string*>(pointeurTexte);
}

void ClassePointeurs::clear()
{
    this->set(nullptr, nullptr, nullptr);
}

void ClassePointeurs::set(const int* pointeurNombreEntier, const double* pointeurNombreReel, const std::string* pointeurTexte)
{
    this->setPointeurNombreEntier(pointeurNombreEntier);
    this->setPointeurNombreReel(pointeurNombreReel);
    this->setPointeurTexte(pointeurTexte);
}

void ClassePointeurs::copy(const ClassePointeurs& classePointeurs)
{
    this->set(classePointeurs.getPointeurNombreEntier(), classePointeurs.getPointeurNombreReel(), classePointeurs.getPointeurTexte());
}

bool ClassePointeurs::equals(const ClassePointeurs& classePointeurs) const
{
    if (this->getPointeurNombreEntier() != classePointeurs.getPointeurNombreEntier())
        return false;
    if (this->getPointeurNombreReel() != classePointeurs.getPointeurNombreReel())
        return false;
    if (this->getPointeurTexte() != classePointeurs.getPointeurTexte())
        return false;
    return true;
}

void ClassePointeurs::fromString(const std::string& fromString, const char& sep)
{
    // TODO void ClassePointeurs::fromString(const std::string& fromString, const char& sep)
#warning "'void ClassePointeurs::fromString(const std::string& fromString, const char& sep)' not implemented"
}

const std::string ClassePointeurs::toString(const char& sep) const
{
    // TODO const std::string ClassePointeurs::toString(const char& sep) const
#warning "'const std::string ClassePointeurs::toString(const char& sep) const' not implemented"
    return std::string();
}
