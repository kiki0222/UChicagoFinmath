//
// Created by sebastiend on 06/10/2018.
//

#include "BookUpdate.h"

std::ostream& operator<<(std::ostream &os, const BookUpdate& bu)
{
    os<< bu.get_quantity();
    return os;
}