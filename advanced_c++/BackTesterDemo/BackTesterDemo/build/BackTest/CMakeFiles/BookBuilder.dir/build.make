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
include BackTest/CMakeFiles/BookBuilder.dir/depend.make

# Include the progress variables for this target.
include BackTest/CMakeFiles/BookBuilder.dir/progress.make

# Include the compile flags for this target's objects.
include BackTest/CMakeFiles/BookBuilder.dir/flags.make

BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o: BackTest/CMakeFiles/BookBuilder.dir/flags.make
BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o: ../BackTest/BookBuilder.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o -c /home/kkkristy/BackTesterDemo/BackTest/BookBuilder.cpp

BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BookBuilder.dir/BookBuilder.cpp.i"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kkkristy/BackTesterDemo/BackTest/BookBuilder.cpp > CMakeFiles/BookBuilder.dir/BookBuilder.cpp.i

BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BookBuilder.dir/BookBuilder.cpp.s"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && /bin/x86_64-linux-gnu-g++-9 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kkkristy/BackTesterDemo/BackTest/BookBuilder.cpp -o CMakeFiles/BookBuilder.dir/BookBuilder.cpp.s

# Object files for target BookBuilder
BookBuilder_OBJECTS = \
"CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o"

# External object files for target BookBuilder
BookBuilder_EXTERNAL_OBJECTS =

BackTest/libBookBuilder.a: BackTest/CMakeFiles/BookBuilder.dir/BookBuilder.cpp.o
BackTest/libBookBuilder.a: BackTest/CMakeFiles/BookBuilder.dir/build.make
BackTest/libBookBuilder.a: BackTest/CMakeFiles/BookBuilder.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kkkristy/BackTesterDemo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libBookBuilder.a"
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -P CMakeFiles/BookBuilder.dir/cmake_clean_target.cmake
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/BookBuilder.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
BackTest/CMakeFiles/BookBuilder.dir/build: BackTest/libBookBuilder.a

.PHONY : BackTest/CMakeFiles/BookBuilder.dir/build

BackTest/CMakeFiles/BookBuilder.dir/clean:
	cd /home/kkkristy/BackTesterDemo/build/BackTest && $(CMAKE_COMMAND) -P CMakeFiles/BookBuilder.dir/cmake_clean.cmake
.PHONY : BackTest/CMakeFiles/BookBuilder.dir/clean

BackTest/CMakeFiles/BookBuilder.dir/depend:
	cd /home/kkkristy/BackTesterDemo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kkkristy/BackTesterDemo /home/kkkristy/BackTesterDemo/BackTest /home/kkkristy/BackTesterDemo/build /home/kkkristy/BackTesterDemo/build/BackTest /home/kkkristy/BackTesterDemo/build/BackTest/CMakeFiles/BookBuilder.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : BackTest/CMakeFiles/BookBuilder.dir/depend

