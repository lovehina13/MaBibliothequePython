//==============================================================================
// Name        : ClasseFille.cpp
// Author      : Alexis Foerster (alexis.foerster@gmail.com)
// Version     : 1.0.0 (09/02/2018)
// Description : Source file of the ClasseFille class
//==============================================================================

#include "ClasseFille.h"

ClasseFille::ClasseFille() :
        ClasseMere(), pointeurs(nullptr)
{
    this->clear();
}

ClasseFille::ClasseFille(const ClasseMere& classeMere, const ClassePointeurs* pointeurs) :
        ClasseFille()
{
    this->set(classeMere, pointeurs);
}

ClasseFille::ClasseFille(const ClasseFille& classeFille) :
        ClasseFille()
{
    this->copy(classeFille);
}

ClasseFille::~ClasseFille()
{

}

ClasseFille& ClasseFille::operator=(const ClasseFille& classeFille)
{
    this->copy(classeFille);
    return *this;
}

bool ClasseFille::operator==(const ClasseFille& classeFille) const
{
    return this->equals(classeFille);
}

bool ClasseFille::operator!=(const ClasseFille& classeFille) const
{
    return !this->equals(classeFille);
}

const ClassePointeurs* ClasseFille::getPointeurs() const
{
    return this->pointeurs;
}

void ClasseFille::setPointeurs(const ClassePointeurs* pointeurs)
{
    this->pointeurs = const_cast<ClassePointeurs*>(pointeurs);
}

void ClasseFille::clear()
{
    this->set(ClasseMere(), nullptr);
}

void ClasseFille::set(const ClasseMere& classeMere, const ClassePointeurs* pointeurs)
{
    ClasseMere::copy(classeMere);
    this->setPointeurs(pointeurs);
}

void ClasseFille::copy(const ClasseFille& classeFille)
{
    this->set(classeFille, classeFille.getPointeurs());
}

bool ClasseFille::equals(const ClasseFille& classeFille) const
{
    if (!ClasseMere::equals(classeFille))
        return false;
    if (this->getPointeurs() != classeFille.getPointeurs())
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
