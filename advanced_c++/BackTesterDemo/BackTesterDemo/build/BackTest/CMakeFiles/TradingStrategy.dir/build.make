# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kkkristy/BackTesterDemo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kkkristy/BackTesterDemo/build

# Include any dependencies generated for this target.
include BackTest/CMakeFiles/TradingStrategy.dir/depend.make

# Include the progress variables for this target.
include BackTest/CMakeFiles/TradingStrategy.dir/progress.make

# Include the compile flags for this target's objects.
include BackTest/CMakeFiles/TradingStrategy.dir/flags.make

BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o: BackTest/CMakeFiles/TradingStrategy.dir/flags.make
BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o: ../BackTest/TradingStrategy.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o -c /home/kkkristy/BackTesterDemo/BackTest/TradingStrategy.cpp

BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/BackTest/TradingStrategy.cpp > CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.i

BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/BackTest/TradingStrategy.cpp -o CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.s

BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.o: BackTest/CMakeFiles/TradingStrategy.dir/flags.make
BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.o: ../BackTest/AppBase.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/TradingStrategy.dir/AppBase.cpp.o -c /home/kkkristy/BackTesterDemo/BackTest/AppBase.cpp

BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TradingStrategy.dir/AppBase.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/BackTest/AppBase.cpp > CMakeFiles/TradingStrategy.dir/AppBase.cpp.i

BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TradingStrategy.dir/AppBase.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/BackTest/AppBase.cpp -o CMakeFiles/TradingStrategy.dir/AppBase.cpp.s

BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o: BackTest/CMakeFiles/TradingStrategy.dir/flags.make
BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o: ../BackTest/BookUpdate.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o -c /home/kkkristy/BackTesterDemo/BackTest/BookUpdate.cpp

BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/BackTest/BookUpdate.cpp > CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.i

BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/BackTest/BookUpdate.cpp -o CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.s

BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.o: BackTest/CMakeFiles/TradingStrategy.dir/flags.make
BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.o: ../BackTest/Order.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/TradingStrategy.dir/Order.cpp.o -c /home/kkkristy/BackTesterDemo/BackTest/Order.cpp

BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TradingStrategy.dir/Order.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/BackTest/Order.cpp > CMakeFiles/TradingStrategy.dir/Order.cpp.i

BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TradingStrategy.dir/Order.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/BackTest/Order.cpp -o CMakeFiles/TradingStrategy.dir/Order.cpp.s

# Object files for target TradingStrategy
TradingStrategy_OBJECTS = \
"CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o" \
"CMakeFiles/TradingStrategy.dir/AppBase.cpp.o" \
"CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o" \
"CMakeFiles/TradingStrategy.dir/Order.cpp.o"

# External object files for target TradingStrategy
TradingStrategy_EXTERNAL_OBJECTS =

BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/TradingStrategy.cpp.o
BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/AppBase.cpp.o
BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/BookUpdate.cpp.o
BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/Order.cpp.o
BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/build.make
BackTest/libTradingStrategy.a: BackTest/CMakeFiles/TradingStrategy.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX static library libTradingStrategy.a"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -P CMakeFiles/TradingStrategy.dir/cmake_clean_target.cmake
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/TradingStrategy.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
BackTest/CMakeFiles/TradingStrategy.dir/build: BackTest/libTradingStrategy.a

.PHONY : BackTest/CMakeFiles/TradingStrategy.dir/build

BackTest/CMakeFiles/TradingStrategy.dir/clean:
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -P CMakeFiles/TradingStrategy.dir/cmake_clean.cmake
.PHONY : BackTest/CMakeFiles/TradingStrategy.dir/clean

BackTest/CMakeFiles/TradingStrategy.dir/depend:
	cd /home/kkkristy/BackTesterDemo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kkkristy/BackTesterDemo /home/kkkristy/BackTesterDemo/BackTest /home/kkkristy/BackTesterDemo/build /home/kkkristy/BackTesterDemo/build/BackTest /home/kkkristy/BackTesterDemo/build/BackTest/CMakeFiles/TradingStrategy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : BackTest/CMakeFiles/TradingStrategy.dir/depend

