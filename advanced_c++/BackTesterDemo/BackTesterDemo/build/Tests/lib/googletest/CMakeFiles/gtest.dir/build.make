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
include Tests/lib/googletest/CMakeFiles/gtest.dir/depend.make

# Include the progress variables for this target.
include Tests/lib/googletest/CMakeFiles/gtest.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/lib/googletest/CMakeFiles/gtest.dir/flags.make

Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o: Tests/lib/googletest/CMakeFiles/gtest.dir/flags.make
Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o: ../Tests/lib/googletest/src/gtest-all.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o"
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/gtest.dir/src/gtest-all.cc.o -c /home/kkkristy/BackTesterDemo/Tests/lib/googletest/src/gtest-all.cc

Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gtest.dir/src/gtest-all.cc.i"
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/Tests/lib/googletest/src/gtest-all.cc > CMakeFiles/gtest.dir/src/gtest-all.cc.i

Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gtest.dir/src/gtest-all.cc.s"
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/Tests/lib/googletest/src/gtest-all.cc -o CMakeFiles/gtest.dir/src/gtest-all.cc.s

# Object files for target gtest
gtest_OBJECTS = \
"CMakeFiles/gtest.dir/src/gtest-all.cc.o"

# External object files for target gtest
gtest_EXTERNAL_OBJECTS =

lib/libgtestd.a: Tests/lib/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o
lib/libgtestd.a: Tests/lib/googletest/CMakeFiles/gtest.dir/build.make
lib/libgtestd.a: Tests/lib/googletest/CMakeFiles/gtest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library ../../../lib/libgtestd.a"
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && $(CMAKE_COMMAND) -P CMakeFiles/gtest.dir/cmake_clean_target.cmake
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gtest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/lib/googletest/CMakeFiles/gtest.dir/build: lib/libgtestd.a

.PHONY : Tests/lib/googletest/CMakeFiles/gtest.dir/build

Tests/lib/googletest/CMakeFiles/gtest.dir/clean:
	cd /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest && $(CMAKE_COMMAND) -P CMakeFiles/gtest.dir/cmake_clean.cmake
.PHONY : Tests/lib/googletest/CMakeFiles/gtest.dir/clean

Tests/lib/googletest/CMakeFiles/gtest.dir/depend:
	cd /home/kkkristy/BackTesterDemo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kkkristy/BackTesterDemo /home/kkkristy/BackTesterDemo/Tests/lib/googletest /home/kkkristy/BackTesterDemo/build /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest /home/kkkristy/BackTesterDemo/build/Tests/lib/googletest/CMakeFiles/gtest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Tests/lib/googletest/CMakeFiles/gtest.dir/depend
