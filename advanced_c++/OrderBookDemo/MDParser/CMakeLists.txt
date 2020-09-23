project(MDReader)

add_definitions(-std=gnu++11)

set(HEADER_FILES MDReader.h)
set(SOURCE_FILES MDReader.cpp)

add_library(MDReader STATIC  ${SOURCE_FILES} ${HEADER_FILE})


