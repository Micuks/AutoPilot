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
CMAKE_SOURCE_DIR = /home/micuks/Code/AutoPilot/Sample/Build

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/micuks/Code/AutoPilot/Sample/Build/build_release

# Include any dependencies generated for this target.
include LKA/CMakeFiles/LKA.dir/depend.make

# Include the progress variables for this target.
include LKA/CMakeFiles/LKA.dir/progress.make

# Include the compile flags for this target's objects.
include LKA/CMakeFiles/LKA.dir/flags.make

LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.o: LKA/CMakeFiles/LKA.dir/flags.make
LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.o: /home/micuks/Code/AutoPilot/Sample/Workshop/LKA/src/LKASample.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/micuks/Code/AutoPilot/Sample/Build/build_release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.o"
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/clang++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/LKA.dir/src/LKASample.cpp.o -c /home/micuks/Code/AutoPilot/Sample/Workshop/LKA/src/LKASample.cpp

LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/LKA.dir/src/LKASample.cpp.i"
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/micuks/Code/AutoPilot/Sample/Workshop/LKA/src/LKASample.cpp > CMakeFiles/LKA.dir/src/LKASample.cpp.i

LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/LKA.dir/src/LKASample.cpp.s"
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/micuks/Code/AutoPilot/Sample/Workshop/LKA/src/LKASample.cpp -o CMakeFiles/LKA.dir/src/LKASample.cpp.s

# Object files for target LKA
LKA_OBJECTS = \
"CMakeFiles/LKA.dir/src/LKASample.cpp.o"

# External object files for target LKA
LKA_EXTERNAL_OBJECTS =

/home/micuks/Code/AutoPilot/Sample/bin/LKA: LKA/CMakeFiles/LKA.dir/src/LKASample.cpp.o
/home/micuks/Code/AutoPilot/Sample/bin/LKA: LKA/CMakeFiles/LKA.dir/build.make
/home/micuks/Code/AutoPilot/Sample/bin/LKA: /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libSimOneIOAPI.so
/home/micuks/Code/AutoPilot/Sample/bin/LKA: /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libSSD.so
/home/micuks/Code/AutoPilot/Sample/bin/LKA: /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libHDMapModule.so
/home/micuks/Code/AutoPilot/Sample/bin/LKA: /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libSSD.so
/home/micuks/Code/AutoPilot/Sample/bin/LKA: /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libHDMapModule.so
/home/micuks/Code/AutoPilot/Sample/bin/LKA: LKA/CMakeFiles/LKA.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/micuks/Code/AutoPilot/Sample/Build/build_release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/micuks/Code/AutoPilot/Sample/bin/LKA"
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LKA.dir/link.txt --verbose=$(VERBOSE)
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/cmake -E copy_if_different /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libSimOneIOAPI.so /home/micuks/Code/AutoPilot/Sample/Build/../bin/Release/libSimOneIOAPI.so
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/cmake -E copy_if_different /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libSSD.so /home/micuks/Code/AutoPilot/Sample/Build/../bin/Release/libSSD.so
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && /usr/bin/cmake -E copy_if_different /home/micuks/Code/AutoPilot/Sample/Build/../lib/Linux64/libHDMapModule.so /home/micuks/Code/AutoPilot/Sample/Build/../bin/Release/libHDMapModule.so

# Rule to build all files generated by this target.
LKA/CMakeFiles/LKA.dir/build: /home/micuks/Code/AutoPilot/Sample/bin/LKA

.PHONY : LKA/CMakeFiles/LKA.dir/build

LKA/CMakeFiles/LKA.dir/clean:
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA && $(CMAKE_COMMAND) -P CMakeFiles/LKA.dir/cmake_clean.cmake
.PHONY : LKA/CMakeFiles/LKA.dir/clean

LKA/CMakeFiles/LKA.dir/depend:
	cd /home/micuks/Code/AutoPilot/Sample/Build/build_release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/micuks/Code/AutoPilot/Sample/Build /home/micuks/Code/AutoPilot/Sample/Workshop/LKA /home/micuks/Code/AutoPilot/Sample/Build/build_release /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA /home/micuks/Code/AutoPilot/Sample/Build/build_release/LKA/CMakeFiles/LKA.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : LKA/CMakeFiles/LKA.dir/depend
