# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.14

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.2.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.2.2\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Krist\CLionProjects\OrderBookDemo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug

# Include any dependencies generated for this target.
include OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/depend.make

# Include the progress variables for this target.
include OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/progress.make

# Include the compile flags for this target's objects.
include OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/flags.make

OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj: OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/flags.make
OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj: OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/includes_CXX.rsp
OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj: ../OrderBookTests/lib/googletest/src/gtest_main.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj"
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && C:\PROGRA~2\Dev-Cpp\MinGW64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\gtest_main.dir\src\gtest_main.cc.obj -c C:\Users\Krist\CLionProjects\OrderBookDemo\OrderBookTests\lib\googletest\src\gtest_main.cc

OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gtest_main.dir/src/gtest_main.cc.i"
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && C:\PROGRA~2\Dev-Cpp\MinGW64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\Krist\CLionProjects\OrderBookDemo\OrderBookTests\lib\googletest\src\gtest_main.cc > CMakeFiles\gtest_main.dir\src\gtest_main.cc.i

OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gtest_main.dir/src/gtest_main.cc.s"
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && C:\PROGRA~2\Dev-Cpp\MinGW64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\Krist\CLionProjects\OrderBookDemo\OrderBookTests\lib\googletest\src\gtest_main.cc -o CMakeFiles\gtest_main.dir\src\gtest_main.cc.s

# Object files for target gtest_main
gtest_main_OBJECTS = \
"CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj"

# External object files for target gtest_main
gtest_main_EXTERNAL_OBJECTS =

lib/libgtest_maind.a: OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.obj
lib/libgtest_maind.a: OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/build.make
lib/libgtest_maind.a: OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library ..\..\..\lib\libgtest_maind.a"
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && $(CMAKE_COMMAND) -P CMakeFiles\gtest_main.dir\cmake_clean_target.cmake
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\gtest_main.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/build: lib/libgtest_maind.a

.PHONY : OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/build

OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/clean:
	cd /d C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest && $(CMAKE_COMMAND) -P CMakeFiles\gtest_main.dir\cmake_clean.cmake
.PHONY : OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/clean

OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Krist\CLionProjects\OrderBookDemo C:\Users\Krist\CLionProjects\OrderBookDemo\OrderBookTests\lib\googletest C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest C:\Users\Krist\CLionProjects\OrderBookDemo\cmake-build-debug\OrderBookTests\lib\googletest\CMakeFiles\gtest_main.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : OrderBookTests/lib/googletest/CMakeFiles/gtest_main.dir/depend

