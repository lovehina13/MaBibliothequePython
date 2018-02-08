//==============================================================================
// Name        : ClasseFille.cpp
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (31/07/2017)
// Description : Source file of the ClasseFille class
//==============================================================================

#include "ClasseFille.h"

ClasseFille::ClasseFille()
{
    this->clear();
}

ClasseFille::ClasseFille(const ClassePointeurs& pointeurs) :
        ClasseFille()
{
    this->set(pointeurs);
}

ClasseFille::ClasseFille(const ClasseFille& classeFille) :
        ClasseFille()
{
    this->copy(classeFille);
}

ClasseFille::~ClasseFille()
{

}

const ClassePointeurs& ClasseFille::getPointeurs() const
{
    return this->pointeurs;
}

void ClasseFille::setPointeurs(const ClassePointeurs& pointeurs)
{
    this->pointeurs = pointeurs;
}

void ClasseFille::clear()
{
    this->set(ClassePointeurs());
}

void ClasseFille::set(const ClassePointeurs& pointeurs)
{
    this->setPointeurs(pointeurs);
}

void ClasseFille::copy(const ClasseFille& classeFille)
{
    this->set(classeFille.getPointeurs());
}

bool ClasseFille::equals(const ClasseFille& classeFille) const
{
    if (!this->getPointeurs().equals(classeFille.getPointeurs()))
        return false;
    return true;
}

void ClasseFille::fromString(const std::string& fromString, const char& sep)
{
    // TODO void ClasseFille::fromString(const std::string& fromString, const char& sep)
#warning "'void ClasseFille::fromString(const std::string& fromString, const char& sep)' not implemented"
}

const std::string ClasseFille::toString(const char& sep) const
{
    // TODO const std::string ClasseFille::toString(const char& sep) const
#warning "'const std::string ClasseFille::toString(const char& sep) const' not implemented"
    return std::string();
}
