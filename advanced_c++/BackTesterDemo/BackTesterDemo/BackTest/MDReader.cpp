//
// Created by sebastiend on 18/10/2018.
//

#include "MDReader.h"

time_t strTime2unix(std::string timeStamp)
{
    struct tm tm;
    memset(&tm, 0, sizeof(tm));

    sscanf(timeStamp.c_str(), "%d-%d-%d %d:%d:%d",
           &tm.tm_year, &tm.tm_mon, &tm.tm_mday,
           &tm.tm_hour, &tm.tm_min, &tm.tm_sec);

    tm.tm_year -= 1900;
    tm.tm_mon--;

    return mktime(&tm)-timezone;
}