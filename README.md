# cmake_crossplatform_example

An example of cross-platform setup of CMakePresets C++ project for Visual Studio

# Overview

This repository provides an example of how to set up CMakePresets.json to enable remote build/debugging in Visual Studio 2019 or above

# Quick Start

1. Setup WSL subsystem: https://learn.microsoft.com/en-us/windows/wsl/install
1. Insall clang, ninja-build, gdb packages on WSL
1. Clone the repository
1. Open the repository as "directory" in Visual Studio (as opposed to "open solution")
1. Open Visual Studio settings, find CMake section, set following option:
![image](https://user-images.githubusercontent.com/2542609/193409789-5077a5aa-0859-4d2d-bb7f-abc5a71b0d5c.png)
1. Select target machine, configuration and target: ![image](https://user-images.githubusercontent.com/2542609/193409920-70778cdd-ead4-4b0b-9924-e3d83a74800b.png)
1. Press "Debug" and enjoy seamless debugging from
