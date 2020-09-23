cmake_minimum_required(VERSION 3.12)
project(OrderBookDemo)

find_package(Boost REQUIRED COMPONENTS date_time system filesystem)

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIR})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")

set(SOURCE_FILES main.cpp)
add_executable(OrderBookDemo ${SOURCE_FILES})


include_directories(MDParser)
include_directories(OrderBook)
add_subdirectory(OrderBook)
add_subdirectory(OrderBookTests)
add_subdirectory(MDParser)

target_link_libraries(OrderBookDemo OrderBook MyOrderBook)


include_directories(${Boost_INCLUDE_DIRS})
target_link_libraries(OrderBookDemo ${Boost_DATE_TIME_LIBRARY} ${Boost_LIBRARIES})