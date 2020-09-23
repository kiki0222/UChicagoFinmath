#include <iostream>
#include <OrderBook.h>
#include <MyOrderBook.h>
#include <chrono>
#include <MDReader.h>
using namespace std::chrono;

/*
* https://www.geeksforgeeks.org/measure-execution-time-with-high-precision-in-c-c/
*/

void measure_performance(OrderBook &myob, const char * note, const int number_of_iteration=1000)
{
    int price=0;
    int amount=0;
    myob.clear();
    // Get starting timepoint
    auto start = high_resolution_clock::now();

    for(int k=0;k<number_of_iteration;k++)
    {
        price = 25 + ( std::rand() % ( 63 - 25 + 1 ) );
        amount = 140 + ( std::rand() % ( 140 - 80 + 1 ) );
        myob.add_bid(price,amount);
        price = 25 + ( std::rand() % ( 63 - 25 + 1 ) );
        amount = 140 + ( std::rand() % ( 140 - 80 + 1 ) );
        myob.add_ask(price,amount);
        myob.get_bid_ask().spread();
    }

    // Get ending timepoint
    auto stop = high_resolution_clock::now();
    // Get duration. Substart timepoints to
    // get durarion. To cast it to proper unit
    // use duration cast method
    auto duration = duration_cast<nanoseconds>(stop - start);
    std::cout << note << std::endl;
    std::cout << "Time taken by function: "
              << duration.count()/number_of_iteration << " nanoseconds/price_update" << std::endl;

    myob.clear();
}

void measure_performance(MyOrderBook &myob, const char * note, const int number_of_iteration=1000)
{
    int price=0;
    int amount=0;
    int order_id=0;
    myob.clear();
    // Get starting timepoint
    auto start = high_resolution_clock::now();

    for(int k=0;k<number_of_iteration;k++)
    {
        price = 25 + ( std::rand() % ( 63 - 25 + 1 ) );
        amount = 140 + ( std::rand() % ( 140 - 80 + 1 ) );
        PriceUpdate pu(NEW,price,amount,"",true,"",0,++order_id);
        myob.add_bid(price,pu);
        price = 25 + ( std::rand() % ( 63 - 25 + 1 ) );
        amount = 140 + ( std::rand() % ( 140 - 80 + 1 ) );
        myob.add_ask(price,pu);
        myob.get_bid_ask().spread();
    }

    // Get ending timepoint
    auto stop = high_resolution_clock::now();
    // Get duration. Substart timepoints to
    // get durarion. To cast it to proper unit
    // use duration cast method
    auto duration = duration_cast<nanoseconds>(stop - start);
    std::cout << note << std::endl;
    std::cout << "Time taken by function: "
              << duration.count()/number_of_iteration << " nanoseconds/price_update" << std::endl;

    myob.clear();
}

int main() {
    MyOrderBook myob;
    OrderBook ob;
    
    measure_performance(ob, "REFERENCE IMPLEMENTATION", 1000);
    measure_performance(myob, "YOUR IMPLEMENTATION", 1000);
    

    MDReader reader("/home/kkkristy/OrderBookDemo/InputFiles/trading_arena.csv",",",10); // MODIFY THIS LINE 

    // Get the data from CSV File
    std::vector<PriceUpdate> dataList = reader.getData();

    for(const PriceUpdate &vec : dataList)
    {
        ob.handle_price_update(vec);
    }

    // Get the data from CSV File
    std::vector<PriceUpdate> dataList2 = reader.getData();


    for(const PriceUpdate &vec : dataList2)
    {
        myob.handle_price_update(vec);
    }

    std::cout << "REFERENCE OUTPUT" << std::endl;
    std::cout << ob << std::endl;

    std::cout << "YOUR OUTPUT" << std::endl;
    std::cout << myob << std::endl;

    ob.clear();
    myob.clear();


    return 0;
}
