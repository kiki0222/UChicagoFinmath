//
// Created by sebastiend on 24/10/2018.
//

#ifndef MyOrderBookDEMO_MYMyOrderBook_H
#define MyOrderBookDEMO_MYMyOrderBook_H


#include <map>
#include <iostream>
#include <boost/optional.hpp>
#include <PriceUpdate.h>
#include <unordered_map>
#include <BookUpdate.h>
// Iterators
typedef std::multimap<price_t,PriceUpdate>::iterator MapIter;
typedef std::multimap<price_t,PriceUpdate>::reverse_iterator MapReverseIter;
typedef std::unordered_map<order_id_t,MapIter>::iterator HashmapIter;

// Multimaps: price -> order
typedef std::multimap<price_t,PriceUpdate,std::greater<price_t> > BidsMap;
typedef std::multimap< price_t,PriceUpdate,std::less<price_t> > AsksMap;

// Hashmaps: order id -> multimap iterator (for quick lookup by order ID)
typedef std::unordered_map<order_id_t,MapIter> BidsHash;
typedef std::unordered_map<order_id_t,MapIter> AsksHash;


class MyOrderBook {
    /* HOMEWORK THIS IS THE DATA STRUCTURE YOU NEED TO CHANGE */
    BidsMap bids;
    AsksMap asks;
    BidsHash bidshash;
    AsksHash askshash;
    /* You need to have a data structure storing price update */

    void add(int price, PriceUpdate update, bool bid);
    void remove(int price, PriceUpdate update, bool bid);
public:
    /* You will need to replace BidAsk by BookUpdate */
    struct BookUpdates{
        typedef boost::optional<std::pair<price_t,BookUpdate>> BookUpdate_;
        BookUpdate_ ask;
        BookUpdate_ bid;
        boost::optional<int> spread() const;
    };
    bool is_empty() const;
    void add_bid(int price, PriceUpdate update);
    void add_ask(int price, PriceUpdate update);
    void remove_bid(int price, PriceUpdate update);
    void remove_ask(int price, PriceUpdate update);
    void handle_price_update(const PriceUpdate &pu);
    void clear();

    MyOrderBook::BookUpdates get_bid_ask() const;
    friend std::ostream & operator << (std::ostream &os, const MyOrderBook &book);
    friend std::ostream & operator << (std::ostream &os, const MyOrderBook::BookUpdates &ba);

};



#endif //MyOrderBookDEMO_MYMyOrderBook_H
