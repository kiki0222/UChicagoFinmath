#include <gtest/gtest.h>
#include <OrderBook.h>
#include <MyOrderBook.h>

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
