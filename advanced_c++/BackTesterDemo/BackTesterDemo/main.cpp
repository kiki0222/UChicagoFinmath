#include <iostream>
#include "Order.h"
#include "BookUpdate.h"
#include "MarketSimulator.h"
#include "OrderManager.h"
#include "TradingStrategy.h"
#include "MDReader.h"
#include "BookBuilder.h"

int main() {

    std::queue<Order> strategy_to_ordermanager;
    std::queue<ExecutionOrder> ordermanager_to_strategy;
    std::queue<Order> ordermanager_to_simulator;
    std::queue<ExecutionOrder> simulator_to_ordermanager;
    std::queue<BookUpdate> bookbuilder_to_strategy;

    TradingStrategy ts1(strategy_to_ordermanager,
                        ordermanager_to_strategy,
                        ordermanager_to_simulator,
                        simulator_to_ordermanager,
                        bookbuilder_to_strategy);

    MarketSimulator simulator(strategy_to_ordermanager,
                              ordermanager_to_strategy,
                              ordermanager_to_simulator,
                              simulator_to_ordermanager,
                              bookbuilder_to_strategy);

    OrderManager order_manager(strategy_to_ordermanager,
                               ordermanager_to_strategy,
                               ordermanager_to_simulator,
                               simulator_to_ordermanager,
                               bookbuilder_to_strategy);

    BookBuilder book_builder(strategy_to_ordermanager,
                                ordermanager_to_strategy,
                                ordermanager_to_simulator,
                                simulator_to_ordermanager,
                                bookbuilder_to_strategy);


    book_builder.start();
    simulator.start();
    order_manager.start();
    ts1.start();


    while(!bookbuilder_to_strategy.empty())
    {
        ts1.process_book_update();
        order_manager.handle_order();
        simulator.handle_order();
        order_manager.handle_execution_order();
        ts1.process_market_response();
        order_manager.handle_execution_order();
        ts1.process_market_response();
        status_report(ts1);
    }
    return 0;
}

//