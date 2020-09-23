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
#include <PriceUpdate.h>
using namespace boost::posix_time;

using namespace std;

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
    std::vector<PriceUpdate> getData()
    {
        unsigned int current_number_of_line=0;
        std::ifstream file(fileName);

        if (!file)
        {
            cerr << "File could not be opened!\n"; // Report error
            cerr << "Error code: " << strerror(errno); // Get some info as to why
            exit(1);
        }

        std::vector<PriceUpdate> dataList;

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

            if(vec[1]=="N"){
                PriceUpdate pu(action_t::NEW,
                        std::stoi(vec[3]), //price
                        std::stoi(vec[4]), //quantity
                        vec[7].c_str(), // venue
                        std::stoi(vec[5]) == 1, //is_buy
                        vec[6].c_str(), // symbol
                        std::stoi(vec[0]), //timestamp
                        std::stoi(vec[2])
                        );
                dataList.push_back(pu);
            }
            else if(vec[1]=="M"){
                PriceUpdate pu(action_t::MODIFY,
                               std::stoi(vec[5]), //price
                               std::stoi(vec[4]), //quantity
                               "", // venue
                               0, //is_buy
                               "", // symbol
                               std::stoi(vec[0]),//timestamp
                               std::stoi(vec[2]) //orderid
                );
                dataList.push_back(pu);
            }
            else if(vec[1]=="D"){
                PriceUpdate pu(action_t::REMOVE,
                               std::stoi(vec[4]), //price
                               std::stoi(vec[3]), //quantity
                               "", // venue
                               0, //is_buy
                               "", // symbol
                               std::stoi(vec[0]), //timestamp
                               std::stoi(vec[2]) //orderid
                );
                dataList.push_back(pu);
            }

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
