function(enable_asan)
  if(MSVC)
    if(CMAKE_SIZEOF_VOID_P EQUAL 8) # 64-bit build
        set(ASAN_ARCHITECTURE "x86_64")
    else()
        set(ASAN_ARCHITECTURE "i386")
    endif()

    if (${CMAKE_BUILD_TYPE} STREQUAL "Debug")
        set(ASAN_LIBRARY_NAME "clang_rt.asan_dbg_dynamic-${ASAN_ARCHITECTURE}.dll")
    else()
        set(ASAN_LIBRARY_NAME "clang_rt.asan_dynamic-${ASAN_ARCHITECTURE}.dll")
    endif()
    set(LLVM_SYMBOLIZER_NAME "llvm-symbolizer.exe")
    
    find_file (ASAN_LIBRARY_SOURCE
        NAMES ${ASAN_LIBRARY_NAME}
        REQUIRED
        HINTS $ENV{LIBPATH}
        DOC "Path to Clang AddressSanitizer runtime"
    )

    find_file (LLVM_SYMBOLIZER_SOURCE
        NAMES ${LLVM_SYMBOLIZER_NAME}
        REQUIRED
        HINTS $ENV{LIBPATH}
        DOC "Path to Clang AddressSanitizer runtime"
    )

    add_custom_command(
        COMMENT "Copying ${ASAN_LIBRARY_SOURCE} to ${CMAKE_BINARY_DIR}}"
        OUTPUT ${CMAKE_BINARY_DIR}/${ASAN_LIBRARY_NAME}
        MAIN_DEPENDENCY ${ASAN_LIBRARY_SOURCE}
        COMMAND ${CMAKE_COMMAND} -E copy ${ASAN_LIBRARY_SOURCE} ${CMAKE_BINARY_DIR}
    )

    add_custom_command(
        COMMENT "Copying ${LLVM_SYMBOLIZER_SOURCE} to ${CMAKE_BINARY_DIR}}"
        OUTPUT ${CMAKE_BINARY_DIR}/${LLVM_SYMBOLIZER_NAME}
        MAIN_DEPENDENCY ${LLVM_SYMBOLIZER_SOURCE}
        COMMAND ${CMAKE_COMMAND} -E copy ${LLVM_SYMBOLIZER_SOURCE} ${CMAKE_BINARY_DIR}
    )

    add_custom_target(CopyAsanBinaries ALL DEPENDS ${ASAN_LIBRARY_NAME} ${LLVM_SYMBOLIZER_NAME})
    add_compile_options(/fsanitize=address /Zi /Oy-)
  else()
    add_compile_options(-fsanitize=address -fno-omit-frame-pointer)
    add_link_options(-fsanitize=address)
  endif()
  message(STATUS "Address Sanitizer Enabled")
endfunction()
