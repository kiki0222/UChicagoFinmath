//
// Created by sebastiend on 06/10/2018.
//

#ifndef IEOR_HOMEWORK5_TRADINGSTRATEGY_H
#define IEOR_HOMEWORK5_TRADINGSTRATEGY_H
#include "AppBase.h"
#include "BookUpdate.h"
#include "Order.h"
#include <unordered_map>
#include <string>
#include <iostream>
//#include <ntdef.h>
#include <cmath>

class Signal{
public:
    std::vector<BookUpdate> datalist ;
    void insert_book_update(BookUpdate bu){ 
        if (datalist.size()<15) datalist.push_back(bu); 
        else {datalist.erase(datalist.begin()); datalist.push_back(bu);}
    }
    double get_14day_rsi(){
        std::vector<double> price_change;
        for (int i = 1; i < datalist.size(); i++) 
            price_change.push_back(datalist[i].get_price()-datalist[i-1].get_price());
        int gain_days = 0;
        int loss_days = 0;
        double gain = 0;
        double loss = 0;
        for (int i = 0; i < price_change.size(); i++)
        {
            if (price_change[i] >= 0){ gain_days++; gain += price_change[i]/datalist[i].get_price();}
            else { loss_days++; loss += price_change[i]/datalist[i].get_price();}
            //std::cout << price_change[i]/datalist[i].get_price() << std::endl;
        } 
        //std::cout << loss << std::endl;
        //std::cout << gain << std::endl;
        double avg_gain = gain/gain_days;
        double avg_loss = -loss/loss_days;
        double rsi = 100-(100/(1+avg_gain/avg_loss));
        return std::round(rsi * 1000000.0) / 1000000.0;
    }
    bool go_long(){return (get_14day_rsi()<30) && (datalist.size()==15);}
    bool go_short(){return (get_14day_rsi()>50) && (datalist.size()==15);}
    bool is_tradeable(BookUpdate &bu){return true;}
};

class Execution{
private:
    Order e;
    bool tradeable;
public:

    Execution():tradeable(false){}
    bool insert_order(long timestamp_,
                      bool is_buy_,
                      double price_,
                      unsigned int quantity_,
                      const char * venue_,
                      const char * symbol_,
                      ordertype type_,
                      unsigned int id_);
    bool is_tradeable() {return tradeable;}
    void set_tradeable(bool is_tradable){tradeable=is_tradable;};
    Order & get_order() {return e;}
};

class TradingStrategy : public AppBase {
private:
    Signal signal;
    Execution execution;
    int order_id;
    std::unordered_map<std::string,int> positions;
    unsigned int number_of_rejections;
    unsigned int number_of_fills;
    double cash;
    double holdings;
    unsigned int time;


public:
    TradingStrategy(
            std::queue<Order> &strategy_to_ordermanager_,
            std::queue<ExecutionOrder> &ordermanager_to_strategy_,
            std::queue<Order> &ordermanager_to_simulator_,
            std::queue<ExecutionOrder> &simulator_to_ordermanager_,
            std::queue<BookUpdate> &bookbuilder_to_strategy_
    ):
    AppBase(strategy_to_ordermanager_,
              ordermanager_to_strategy_,
              ordermanager_to_simulator_,
              simulator_to_ordermanager_,
              bookbuilder_to_strategy_),
              signal(),
              execution(),
              order_id(1),
              number_of_rejections(0),
              number_of_fills(0),
              cash(10000),
              holdings(0),
              time(0){}
    virtual void start() {is_working=true;}
    virtual void stop() {
        positions.clear();
        is_working=false;
    }


    bool process_book_update(BookUpdate &bu);
    bool process_book_update();
    bool process_execution();
    bool process_market_response();
    int get_position(std::string symbol);
    unsigned int get_number_of_rejections();
    unsigned int get_number_of_fills();
    void reset_position();
    double get_cash();
    double get_holdings();
    unsigned int get_time();

    friend void status_report(TradingStrategy& ts);

};




#endif //IEOR_HOMEWORK5_TRADINGSTRATEGY_H