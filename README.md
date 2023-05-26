# cmake_template

This repository provides a template for a GitHub-based CMake project which supports building & debugging using Visual Studio on both Windows and Linux

# Quick Start

1. Setup WSL subsystem: https://learn.microsoft.com/en-us/windows/wsl/install
1. Install required packages on WSL: `sudo apt-get install gcc g++ gdb cmake`
1. Clone this repository
1. Open the cloned repository as "directory" in Visual Studio (as opposed to "open solution")
1. Open Visual Studio settings, find CMake section, set following option:
![image](https://github.com/DarkWanderer/cmake_template/assets/2542609/d3661d3b-f666-4b29-911b-d11613343e3a)
1. Select target machine, configuration and target: ![image](https://github.com/DarkWanderer/cmake_template/assets/2542609/85dc4c62-b955-4ad2-a692-d8b94b9e4eea)
1. Press "Debug" and enjoy seamless debugging of a Linux binary in Visual Studio

# Things to try

* Launch sanitizers.exe executable in `x64 ASan` configuration
* Put a breakpoint in helloworld.cpp
* Running/debug tests under ASan config

All of above works remotely on Linux
