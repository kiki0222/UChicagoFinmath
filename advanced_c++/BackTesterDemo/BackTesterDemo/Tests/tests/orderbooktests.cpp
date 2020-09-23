#include <gtest/gtest.h>
#include "Order.h"
#include "BookUpdate.h"
#include "MarketSimulator.h"
#include "OrderManager.h"
#include "TradingStrategy.h"
#include "MDReader.h"
#include "BookBuilder.h"
#include "boost/date_time/gregorian/gregorian.hpp"
/*
TEST(OrderBookTests, OrderBookEmptyByDefault)
{
    OrderBook book;
    EXPECT_TRUE(book.is_empty());
}

TEST(OrderBookTests, OrderAdditionWorks)
{
    OrderBook book;
    book.add_bid(123,456);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    auto bid=bidask.bid.get();
    EXPECT_EQ(123, bid.first);
    EXPECT_EQ(456, bid.second);
}




TEST(OrderBookTests, OrderRemovalWorks)
{
    OrderBook book;
    book.add_bid(123,456);
    book.remove_bid(123,156);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    auto bid=bidask.bid.get();
    EXPECT_EQ(123, bid.first);
    EXPECT_EQ(456-156, bid.second);
}


TEST(OrderBookTests, SpreadCalculated)
{
    OrderBook book;
    book.add_bid(50,100);
    book.add_ask(70,100);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    EXPECT_TRUE(bidask.ask.is_initialized());
    auto spread=bidask.spread();
    EXPECT_TRUE(spread.is_initialized());
    EXPECT_EQ(20, spread.get());
}

TEST(MyOrderBookTests, OrderBookEmptyByDefault)
{
    MyOrderBook book;
    EXPECT_TRUE(book.is_empty());
}

TEST(MyOrderBookTests, OrderAdditionWorks)
{
    MyOrderBook book;
    PriceUpdate pu(NEW,123,456,"",1,"",0,0);
    book.add_bid(123,pu);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    auto bid=bidask.bid.get();
    EXPECT_EQ(123, bid.first);
    EXPECT_EQ(456, bid.second.get_quantity());
}

TEST(MyOrderBookTests, OrderModificationWorks)
{
    MyOrderBook book;
    PriceUpdate pu(NEW,123,456,"",1,"",0,0);
    book.add_bid(123,pu);
    PriceUpdate pu1(MODIFY,123,400,"",1,"",0,0);
    book.add_bid(123,pu1);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    auto bid=bidask.bid.get();
    EXPECT_EQ(123, bid.first);
    EXPECT_EQ(400, bid.second.get_quantity());
}

TEST(MyOrderBookTests, OrderRemovalWorks)
{
    MyOrderBook book;
    PriceUpdate pu(NEW,123,456,"",1,"",0,0);
    PriceUpdate pu1(REMOVE,123,456,"",1,"",0,0);
    book.add_bid(123,pu);
    book.remove_bid(123,pu1);
    auto bidask=book.get_bid_ask();
    EXPECT_FALSE(bidask.bid.is_initialized());
}

TEST(MyOrderBookTests, SpreadCalculated)
{
    MyOrderBook book;
    PriceUpdate pu(NEW,50,100,"",1,"",0,0);
    PriceUpdate pu1(NEW,70,100,"",0,"",1,1);
    book.add_bid(50,pu);
    book.add_ask(70,pu1);
    auto bidask=book.get_bid_ask();
    EXPECT_TRUE(bidask.bid.is_initialized());
    EXPECT_TRUE(bidask.ask.is_initialized());
    auto spread=bidask.spread();
    EXPECT_TRUE(spread.is_initialized());
    EXPECT_EQ(20, spread.get());
}
*/

TEST(MDReaderTests, ReadWorks)
{
    MDReader reader("/home/kkkristy/BackTester/InputFiles/CUR-CNY2019.csv",",",2);
    std::vector<BookUpdate> dataList = reader.getData();
    EXPECT_EQ(dataList[0].get_epoch_time(), 1560470400);
    EXPECT_EQ(dataList[0].get_price(), 6.9241);
    EXPECT_EQ(dataList[0].get_quantity(), 100);
    EXPECT_EQ(dataList[0].get_is_buy(), true);
    EXPECT_EQ(dataList[0].get_level(), 0);
    EXPECT_EQ(dataList.size(),3);
}

TEST(SignalTests, SignalWorks)
{
    MDReader reader("/home/kkkristy/BackTester/InputFiles/CUR-CNY2019.csv",",",14);
    std::vector<BookUpdate> dataList = reader.getData();
    Signal sig1;
    for (int i = 0; i < 5; i++) sig1.insert_book_update(dataList[i]);
    EXPECT_FALSE(sig1.go_long());
    EXPECT_FALSE(sig1.go_short());
    EXPECT_EQ(sig1.datalist.size(),5);
}

TEST(SignalTests, SignalWorks2)
{
    MDReader reader("/home/kkkristy/BackTester/InputFiles/CUR-CNY2019.csv",",",15);
    std::vector<BookUpdate> dataList = reader.getData();
    Signal sig1;
    for (int i = 0; i < 16; i++) sig1.insert_book_update(dataList[i]);
    //for (int i = 0; i < sig1.datalist.size(); i++) cout<<sig1.datalist[i].get_price()<<endl;
    EXPECT_TRUE(sig1.go_long()); //ACCORDING TO PYTHON OUTPUT
    EXPECT_EQ(sig1.datalist.size(),15);
}

TEST(TradingStrategyTests, TradingStrategyWorks)
{
    std::queue<Order> strategy_to_ordermanager;
    std::queue<ExecutionOrder> ordermanager_to_strategy;
    std::queue<Order> ordermanager_to_simulator;
    std::queue<ExecutionOrder> simulator_to_ordermanager;
    std::queue<BookUpdate> bookbuilder_to_strategy;
    TradingStrategy ts(strategy_to_ordermanager,
                        ordermanager_to_strategy,
                        ordermanager_to_simulator,
                        simulator_to_ordermanager,
                        bookbuilder_to_strategy);
    BookBuilder book_builder1(strategy_to_ordermanager,
                             ordermanager_to_strategy,
                             ordermanager_to_simulator,
                             simulator_to_ordermanager,
                             bookbuilder_to_strategy);
    book_builder1.start();
    ts.start();
    for (int i = 0; i<55; i++)
        ts.process_book_update();
    EXPECT_FALSE(strategy_to_ordermanager.back().isBuy()); //ACCORDING TO PYTHON OUTPUT
}