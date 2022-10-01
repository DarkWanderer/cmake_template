cmake_minimum_required(VERSION 3.8)

project("cmake_visual_studio_example")

add_executable(cmake_visual_studio_example "main.cpp")

option(ASAN_ENABLED "Build this target with AddressSanitizer" OFF)

if(ASAN_ENABLED)
  if(MSVC)    
	if(CMAKE_SIZEOF_VOID_P EQUAL 8) # 64-bit build
		set(ASAN_ARCHITECTURE "x86_64")
	else()
		set(ASAN_ARCHITECTURE "i386")
	endif()


	if (${CMAKE_BUILD_TYPE} STREQUAL "Debug")
		set(ASAN_LIBRARY_TARGET "clang_rt.asan_dbg_dynamic-${ASAN_ARCHITECTURE}.dll")
	else()
		set(ASAN_LIBRARY_TARGET "clang_rt.asan_dynamic-${ASAN_ARCHITECTURE}.dll")
	endif()
	
	find_file (ASAN_LIBRARY_SOURCE
		NAMES ${ASAN_LIBRARY_TARGET}
		REQUIRED
		HINTS $ENV{LIBPATH}
		DOC "Path to Clang AddressSanitizer runtime"
	)

	add_custom_command(
		COMMENT "Copying ${ASAN_LIBRARY_SOURCE} to ${CMAKE_BINARY_DIR}}"
		OUTPUT ${CMAKE_BINARY_DIR}/${ASAN_LIBRARY_TARGET}
		MAIN_DEPENDENCY ${ASAN_LIBRARY_SOURCE}
		COMMAND ${CMAKE_COMMAND} -E copy ${ASAN_LIBRARY_SOURCE} ${CMAKE_BINARY_DIR}
	)

    add_custom_target(CopyAsanBinaries DEPENDS ${ASAN_LIBRARY_TARGET})
	add_dependencies(cmake_visual_studio_example CopyAsanBinaries)
	target_compile_options(cmake_visual_studio_example PUBLIC /fsanitize=address /Zi)
  else()
    target_compile_options(cmake_visual_studio_example PUBLIC -fsanitize=address -fno-omit-frame-pointer)
    target_link_options(cmake_visual_studio_example PUBLIC -fsanitize=address)
  endif()
  message(STATUS "Address Sanitizer Enabled")
endif()
