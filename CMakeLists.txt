cmake_minimum_required(VERSION 2.8)
project(pybind11-experiments)
set(CMAKE_CXX_STANDARD 17)


# ============  Conan Boostrap  ======================#

# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
   message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
   file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.13/conan.cmake"
                 "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(REQUIRES   pybind11/2.2.4@conan/stable
                BASIC_SETUP
                BUILD missing)

#============ Additional Commands =============#

# Copy target file to current directory whenerver it is rebuilt
function(copy_after_build TARGET_NAME )
    # Note: CMAKE_CURRENT_LIST_DIR is the directory where is this
    # CMakeLists.txt file.
    set(DESTDIR ${CMAKE_CURRENT_LIST_DIR}/bin/)
    file(MAKE_DIRECTORY ${DESTDIR})

    # Copy binary file to <CMakeLists.txt didctory>./bin
    # after target is compiled.
    add_custom_command(TARGET ${TARGET_NAME} POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy
                               $<TARGET_FILE:${TARGET_NAME}> ${DESTDIR}
                               )
endfunction()


#----------------------------------------------#
#    Target Configurations                     #
#----------------------------------------------#

find_package(pybind11 CONFIG REQUIRED)


# Target1: cashflow - Python module basics
#.....................................
pybind11_add_module(cashflow cashflow.cpp)
copy_after_build(cashflow)

pybind11_add_module(test2 test2.cpp)
copy_after_build(test2)



# Copy targets to ./ - Directory where is this file CMakeLists.txt (project top level dir)
# install(TARGETS basics DESTINATION ${CMAKE_CURRENT_LIST_DIR})


#add_executable( "main.cpp")
