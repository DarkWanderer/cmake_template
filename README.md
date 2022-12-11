# cmake_crossplatform_example

This repository provides an example of how to set up CMakePresets.json to enable remote build/debugging in Visual Studio 2019 or above. A generator allowing to create customized versions is also available

# Quick Start

1. Setup WSL subsystem: https://learn.microsoft.com/en-us/windows/wsl/install
1. Install gcc and gdb packages on WSL
1. Clone this repository
1. Open the cloned repository as "directory" in Visual Studio (as opposed to "open solution")
1. Open Visual Studio settings, find CMake section, set following option:
![image](https://user-images.githubusercontent.com/2542609/193409789-5077a5aa-0859-4d2d-bb7f-abc5a71b0d5c.png)
1. Select target machine, configuration and target: ![image](https://user-images.githubusercontent.com/2542609/193409920-70778cdd-ead4-4b0b-9924-e3d83a74800b.png)
1. Press "Debug" and enjoy seamless debugging of a Linux binary in Visual Studio

# Things to try

* Try launching use-after-free executable in `x64 ASan` configuration
* Try putting a breakpoint in helloworld.cpp and launching it under Linux
* Try running/debugging tests under ASan config
