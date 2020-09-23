cmake_minimum_required(VERSION 3.12)
project(BackTesterDemo)

find_package(Boost REQUIRED COMPONENTS date_time system filesystem)

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIR})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")

set(SOURCE_FILES main.cpp)
add_executable(BackTesterDemo ${SOURCE_FILES})


include_directories(BackTest)
add_subdirectory(BackTest)
add_subdirectory(Tests)

target_link_libraries(BackTesterDemo MDReader BookBuilder TradingStrategy OrderManager MarketSimulator)


include_directories(${Boost_INCLUDE_DIRS})
target_link_libraries(BackTesterDemo ${Boost_DATE_TIME_LIBRARY} ${Boost_LIBRARIES})