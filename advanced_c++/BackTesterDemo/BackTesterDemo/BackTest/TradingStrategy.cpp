//
// Created by sebastiend on 06/10/2018.
//

#include "TradingStrategy.h"


bool Execution::insert_order(long timestamp_,
                  bool is_buy_,
                  double price_,
                  unsigned int quantity_,
                  const char * venue_,
                  const char * symbol_,
                  ordertype type_,
                  unsigned int id_)
{
    e.setTimeStamp(timestamp_);
    e.setSide(is_buy_);
    e.setPrice(price_);
    e.setQuantity(quantity_);
    e.setVenue(venue_);
    e.setType(type_);
    e.setSymbol(symbol_);
    e.setOrderID(id_);
    return true;
}

bool TradingStrategy::process_book_update(BookUpdate &bu){
    if(!is_working)
        return false;
    if (signal.is_tradeable(bu)) {
        signal.insert_book_update(bu);
        time = bu.get_epoch_time();
        if (signal.go_long()) {
            execution.insert_order(bu.get_epoch_time(), true,
                                   bu.get_price(), bu.get_quantity(), bu.get_venue(), bu.get_symbol(), ordertype::LIMIT,
                                   order_id++);
            execution.set_tradeable(true);
            return process_execution();
        }
        else if (signal.go_short()) {
            execution.insert_order(bu.get_epoch_time(), false,
                                   bu.get_price(), bu.get_quantity(), bu.get_venue(), bu.get_symbol(), ordertype::LIMIT,
                                   order_id++);
            execution.set_tradeable(true);
            return process_execution();
        }
        else
        {
            holdings = positions[bu.get_symbol()]*bu.get_price();
        }
    }
    return false;
}


bool TradingStrategy::process_book_update(){
    if(!is_working)
        return false;
    if(bookbuilder_to_strategy.empty())
        return true;
    BookUpdate &bu = bookbuilder_to_strategy.front();
    bookbuilder_to_strategy.pop();
    return process_book_update(bu);
}

bool TradingStrategy::process_execution() {
    if(!is_working)
        return false;
    Order order;
    if (execution.is_tradeable()) {
        order.setType(execution.get_order().getOrderType());
        order.setVenue(execution.get_order().getVenue());
        order.setQuantity(execution.get_order().getQuantity());
        order.setPrice(execution.get_order().getPrice());
        order.setOrderID(execution.get_order().getID());
        order.setSymbol(execution.get_order().getSymbol());
        order.setSide(execution.get_order().isBuy());
        order.setTimeStamp(execution.get_order().getTimeStamp());
        execution.set_tradeable(false);
        //std::cout << "strategy push an order" << std::endl;
        strategy_to_ordermanager.push(order);
    }
    return true;
};

bool TradingStrategy::process_market_response()
{
    if(!is_working)
        return false;
    if (ordermanager_to_strategy.empty())
        return true;
    ExecutionOrder &eo = ordermanager_to_strategy.front();
    ordermanager_to_strategy.pop();
    if (eo.getState() == FILLED) {
        if (eo.isBuy()) {
            cash -= eo.getPrice() * eo.getQuantity(); 
            positions[eo.getSymbol()] += eo.getQuantity();
            holdings = positions[eo.getSymbol()]*eo.getPrice();
        }
        else{
            cash += eo.getPrice() * eo.getQuantity();
            positions[eo.getSymbol()] -= eo.getQuantity();
            holdings = positions[eo.getSymbol()]*eo.getPrice();
        }
    }

    return true;
}

int TradingStrategy::get_position(std::string symbol)
{
    return positions[symbol];
//return 0;
}

unsigned int TradingStrategy::get_number_of_rejections() {
    return number_of_rejections;
    //return 0;
}

unsigned int TradingStrategy::get_number_of_fills() {
    return number_of_fills;
    //return 0;
}

double TradingStrategy::get_cash() {
    return std::round(cash * 1000000.0) / 1000000.0;
}

void TradingStrategy::reset_position(){
    positions.clear();
}

double TradingStrategy::get_holdings()
{
    return holdings;
}

unsigned int TradingStrategy::get_time()
{
    return time;
}

void status_report(TradingStrategy& ts)
{
    std::cout << ts.get_time() << "," << ts.get_position("USDCNY") << "," << ts.get_cash() << "," << ts.get_holdings() << ","
    << ts.get_cash()+ts.get_holdings() << std::endl;
}