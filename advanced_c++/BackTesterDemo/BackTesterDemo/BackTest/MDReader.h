//
// Created by sebastiend on 18/10/2018.
//

#ifndef IEOR_HOMEWORK5_MARKETDATAREADER_H
#define IEOR_HOMEWORK5_MARKETDATAREADER_H
#include <fstream>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>
#include <BookUpdate.h>
#include <memory>
#include <ctime>

using namespace boost::posix_time;

using namespace std;

//parse time by myself
time_t strTime2unix(std::string timeStamp);

class MDReader
{
    const std::string fileName;
    const std::string delimeter;
    const unsigned int number_of_line;
    const bool is_header;





public:
    MDReader(std::string filename,
            std::string delm = ",",
            unsigned int number_of_line_ = 10,
            bool is_header_ = true) :
            fileName(filename),
            delimeter(delm),
            number_of_line(number_of_line_),
            is_header(is_header_)
    { }

    /*
    * Parses through csv file line by line and returns the data
    * in vector of vector of strings.
    */
    std::vector<BookUpdate> getData()
    {
        unsigned int current_number_of_line=0;
        std::ifstream file(fileName);

        if (!file)
        {
            cerr << "File could not be opened!\n"; // Report error
            cerr << "Error code: " << strerror(errno); // Get some info as to why
            exit(1);
        }

        std::vector<BookUpdate> dataList;

        std::string line = "";
        // Iterate through each line and split the content using delimeter
        bool is_header_handled=false;


        while (getline(file, line))
        {
            if(is_header and !is_header_handled)
            {
                is_header_handled=true;
                continue;
            }
            line.erase( std::remove(line.begin(), line.end(), '\r'), line.end() );
            std::vector<std::string> vec;
            boost::algorithm::split(vec, line, boost::is_any_of(delimeter));
            /*
            std::string ts("2002-01-20 23:59:59");
            ptime t(time_from_string(vec[0]));
            ptime start(time_from_string("1970-01-01 00:00:00.000"));
            time_duration dur = t - start;
            */
            time_t epoch = strTime2unix(vec[0]);

            BookUpdate b(0,std::round(std::stof(vec[1])*1000000.0)/1000000.0,100,"FX",true,"USDCNY",epoch);
            dataList.push_back(b);

            if(number_of_line!=0 and current_number_of_line++>=number_of_line)
            {
                break;
            }
        }
        // Close the File
        file.close();

        return dataList;
    }
};


#endif //IEOR_HOMEWORK5_MARKETDATAREADER_H