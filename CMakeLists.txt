cmake_minimum_required(VERSION 3.8)

project("cmake_visual_studio_example")

option(SANITIZE "Enable selected sanitizer in build" OFF)

include(sanitizer.cmake)
if(SANITIZE)
  enable_sanitizer(${SANITIZE})
endif()

add_executable(hello-world "helloworld.cpp")
add_executable(sanitizers "sanitizers.cpp")

include(CTest)
add_test(NAME namespace.class.sanitizers COMMAND $<TARGET_FILE:sanitizers>)
add_test(NAME namespace.class.hello-world COMMAND $<TARGET_FILE:hello-world>)
