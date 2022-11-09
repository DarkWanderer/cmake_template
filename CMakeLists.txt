cmake_minimum_required(VERSION 3.8)

project("cmake_visual_studio_example")

option(ASAN_ENABLED "Build this target with AddressSanitizer" OFF)

include(ASan.cmake)

if(ASAN_ENABLED)
  enable_asan()
endif()

add_executable(hello-world "helloworld.cpp")
add_executable(use-after-free "use-after-free.cpp")

include(CTest)
add_test(NAME namespace.class.use-after-free COMMAND $<TARGET_FILE:use-after-free>)
add_test(NAME namespace.class.hello-world COMMAND $<TARGET_FILE:hello-world>)
