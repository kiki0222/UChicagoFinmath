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
include Tests/tests/CMakeFiles/RunTests.dir/depend.make

# Include the progress variables for this target.
include Tests/tests/CMakeFiles/RunTests.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/tests/CMakeFiles/RunTests.dir/flags.make

Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.o: Tests/tests/CMakeFiles/RunTests.dir/flags.make
Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.o: ../Tests/tests/orderbooktests.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/Tests/tests && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/RunTests.dir/orderbooktests.cpp.o -c /home/kkkristy/BackTesterDemo/Tests/tests/orderbooktests.cpp

Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/RunTests.dir/orderbooktests.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/Tests/tests && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/Tests/tests/orderbooktests.cpp > CMakeFiles/RunTests.dir/orderbooktests.cpp.i

Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/RunTests.dir/orderbooktests.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/Tests/tests && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/Tests/tests/orderbooktests.cpp -o CMakeFiles/RunTests.dir/orderbooktests.cpp.s

# Object files for target RunTests
RunTests_OBJECTS = \
"CMakeFiles/RunTests.dir/orderbooktests.cpp.o"

# External object files for target RunTests
RunTests_EXTERNAL_OBJECTS =

Tests/tests/RunTests: Tests/tests/CMakeFiles/RunTests.dir/orderbooktests.cpp.o
Tests/tests/RunTests: Tests/tests/CMakeFiles/RunTests.dir/build.make
Tests/tests/RunTests: lib/libgtestd.a
Tests/tests/RunTests: lib/libgtest_maind.a
Tests/tests/RunTests: BackTest/libMDReader.a
Tests/tests/RunTests: BackTest/libBookBuilder.a
Tests/tests/RunTests: BackTest/libTradingStrategy.a
Tests/tests/RunTests: BackTest/libOrderManager.a
Tests/tests/RunTests: BackTest/libMarketSimulator.a
Tests/tests/RunTests: lib/libgtestd.a
Tests/tests/RunTests: Tests/tests/CMakeFiles/RunTests.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable RunTests"
	cd /home/kkkristy/BackTesterDemo/build/Tests/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/RunTests.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/tests/CMakeFiles/RunTests.dir/build: Tests/tests/RunTests

.PHONY : Tests/tests/CMakeFiles/RunTests.dir/build

Tests/tests/CMakeFiles/RunTests.dir/clean:
	cd /home/kkkristy/BackTesterDemo/build/Tests/tests && $(CMAKE_COMMAND) -P CMakeFiles/RunTests.dir/cmake_clean.cmake
.PHONY : Tests/tests/CMakeFiles/RunTests.dir/clean

Tests/tests/CMakeFiles/RunTests.dir/depend:
	cd /home/kkkristy/BackTesterDemo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kkkristy/BackTesterDemo /home/kkkristy/BackTesterDemo/Tests/tests /home/kkkristy/BackTesterDemo/build /home/kkkristy/BackTesterDemo/build/Tests/tests /home/kkkristy/BackTesterDemo/build/Tests/tests/CMakeFiles/RunTests.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Tests/tests/CMakeFiles/RunTests.dir/depend

