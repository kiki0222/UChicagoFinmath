project(BackTester)

add_definitions(-std=gnu++11)

set(HEADER_FILES MDReader.h)
set(SOURCE_FILES MDReader.cpp)

add_library(MDReader STATIC  ${SOURCE_FILES} ${HEADER_FILE})

set(HEADER_FILES1 BookBuilder.h)
set(SOURCE_FILES1 BookBuilder.cpp)

add_library(BookBuilder STATIC  ${SOURCE_FILES1} ${HEADER_FILES1})


set(HEADER_FILES2 TradingStrategy.h)
set(SOURCE_FILES2 TradingStrategy.cpp AppBase.cpp BookUpdate.cpp Order.cpp)

add_library(TradingStrategy STATIC  ${SOURCE_FILES2} ${EADER_FILES2})

set(HEADER_FILES3 OrderManager.h)
set(SOURCE_FILES3 OrderManager.cpp AppBase.cpp Order.cpp)

add_library(OrderManager STATIC  ${SOURCE_FILES3} ${EADER_FILES3})

set(HEADER_FILES4 MarketSimulator.h)
set(SOURCE_FILES4 MarketSimulator.cpp AppBase.cpp Order.cpp)

add_library(MarketSimulator STATIC  ${SOURCE_FILES4} ${EADER_FILES4})