//
// Created by sebastiend on 24/10/2018.
//

#include "MyOrderBook.h"


bool MyOrderBook::is_empty() const{
    return bids.empty() and asks.empty();
}

void MyOrderBook::add_bid(int price, PriceUpdate update){
    add(price,update, true);
}
void MyOrderBook::add_ask(int price, PriceUpdate update){
    add(price,update, false);
};

void MyOrderBook::add(int price, PriceUpdate update, bool bid) {
    
    if(bid){
        if (bidshash.find(update.get_order_id()) == bidshash.end()){
            bids.insert(std::pair<price_t, PriceUpdate>(price,update));
            for (MapIter it = bids.begin(); it != bids.end(); it++)
                bidshash[it->second.get_order_id()] = it;
        }
        else{
            MapIter it = bidshash.find(update.get_order_id())->second;
            it->second.set_quantity(update.get_quantity());
        }
    }
    else
    {
        if (askshash.find(update.get_order_id()) == askshash.end()){
            asks.insert(std::pair<price_t, PriceUpdate>(price,update));
            for (MapIter it = asks.begin(); it != asks.end(); it++)
                askshash[it->second.get_order_id()] = it;
        }
        else{
            MapIter it = askshash.find(update.get_order_id())->second;
            it->second.set_quantity(update.get_quantity());
        }
    }
    
}



void MyOrderBook::remove_bid(int price, PriceUpdate update){
    remove(price,update, true);
}
void MyOrderBook::remove_ask(int price, PriceUpdate update){
    remove(price,update, false);
};

void MyOrderBook::clear()
{
    bids.clear();
    asks.clear();
    bidshash.clear();
    askshash.clear();
}

void MyOrderBook::handle_price_update(const PriceUpdate &pu)
{
    switch(pu.get_action())
    {
        case action_t::NEW:
            if(pu.get_is_buy())
                add_bid(pu.get_price(),pu);
            else
                add_ask(pu.get_price(),pu);
            break;
        case action_t::MODIFY:
            if(pu.get_is_buy())
                add_bid(pu.get_price(),pu);
            else
                add_ask(pu.get_price(),pu);
            break;
        case action_t::REMOVE:
            if(pu.get_is_buy())
                remove_bid(pu.get_price(),pu);
            else
                remove_ask(pu.get_price(),pu);
            break;
    }

}

void MyOrderBook::remove(int price, PriceUpdate update, bool bid) {
    if (bid){
        if (bidshash.find(update.get_order_id()) != bidshash.end()){
            MapIter it = bidshash.find(update.get_order_id())->second;
            bids.erase(it);
            for (MapIter it = bids.begin(); it != bids.end(); it++)
                bidshash[it->second.get_order_id()] = it;
        }
    }
    else
    {
        if (askshash.find(update.get_order_id()) != askshash.end()){
        MapIter it = askshash.find(update.get_order_id())->second;
        asks.erase(it);
        for (MapIter it = asks.begin(); it != asks.end(); it++)
            askshash[it->second.get_order_id()] = it;
        }
    }
}


std::ostream& operator<<(std::ostream &os, const MyOrderBook &book) {
    if (book.is_empty())
    {
        os << "ORDER BOOK EMPTY";
        return os;
    }

    os << "ASKS" << std::endl;
    for(auto it = book.asks.begin();
        it!=book.asks.end();
        ++it)
    {
        os << it->first << "\t" << it->second.get_quantity() << std::endl;
    }
    os << "BIDS" << std::endl;
    for(auto it = book.bids.begin();
        it!=book.bids.end();
        ++it)
    {
        os << it->first << "\t" << it->second.get_quantity() << std::endl;
    }
    return os;
}


std::ostream& operator<<(std::ostream &os, const MyOrderBook::BookUpdates &ba) {
    auto print = [&](const MyOrderBook::BookUpdates::BookUpdate_ &e, const std::string &text)
    {
        bool have_value = e.is_initialized();
        if(have_value)
        {
            auto value = e.get();
            os << value.second << text << "s @" << value.first;

        } else{
            os << "NO" << text;
        }
    };
    print(ba.bid, "bid");
    os << ", ";
    print(ba.ask, "ask");
    return os;
}

boost::optional<int> MyOrderBook::BookUpdates::spread() const{
    boost::optional<int> result;
    if(bid.is_initialized() and ask.is_initialized())
        result=ask.get().first - bid.get().first;
    return result;
}




MyOrderBook::BookUpdates MyOrderBook::get_bid_ask() const {
    BookUpdates result;
    auto best_bid = bids.rbegin();
    if(best_bid != bids.rend() ){
        PriceUpdate bid_ = best_bid->second;
        result.bid = std::pair<price_t,BookUpdate>(best_bid->first,BookUpdate(0,bid_.get_price(),bid_.get_quantity(),bid_.get_venue(),bid_.get_is_buy(),bid_.get_symbol(),bid_.get_epoch_time()));
    }
    auto best_ask = asks.begin();
    if(best_ask != asks.end() ){
        PriceUpdate ask_ = best_ask->second;
        result.ask = std::pair<price_t,BookUpdate>(best_ask->first,BookUpdate(0,ask_.get_price(),ask_.get_quantity(),ask_.get_venue(),ask_.get_is_buy(),ask_.get_symbol(),ask_.get_epoch_time()));
    }
    return result;
}