CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# ------------------------------------------------------------------------------
# Build Dependencies to build all standard modules
#
# Centos:
# yum groupinstall 'Development Tools'
# yum install zlib-devel
# yum install readline-devel
# yum install ncurses-devel
# yum install openssl-devel
# yum install gdbm-devel
# yum install sqlite-devel
# yum install bzip2-devel
# ------------------------------------------------------------------------------

set(python_version $ENV{REZ_BUILD_PROJECT_VERSION})
#string(REPLACE "." "_" python_version_modified ${python_version})

# ------------------------------------------------------------------------------
#message("=====================================================================")
# Print environment variables
#execute_process(COMMAND "${CMAKE_COMMAND}" "-E" "environment")

# Print CMake variables
#get_cmake_property(_variableNames VARIABLES)
#list (SORT _variableNames)
#foreach (_variableName ${_variableNames})
#message(STATUS "${_variableName}=${${_variableName}}")
#endforeach()
#message("=====================================================================")
# ------------------------------------------------------------------------------

#rez_set_archive(
#    url_python python/Python-${python_version}.tgz
#    http://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz
#)

# I am having issues extracting the tar file, so, I untar myself and I am
# pointing to the extracted folder here.

ExternalProject_add(
    python
    #URL url_python
    SOURCE_DIR "/home/marcelo/Dev/payload/python/Python-2.7.5"
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-ipv6 --enable-unicode=ucs4  LDFLAGS=-Wl,-rpath,'$$ORIGIN/../lib/'
    INSTALL_COMMAND make install VERBOSE=1
    ALWAYS 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1
    BUILD_IN_SOURCE 1
)

#install(
#    FILES cmake/FindPython.cmake cmake/python.cmake
#    DESTINATION cmake
#)

