#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It helps you to install your own program

# Set this to the location you want to install all programs to
# I suggest a directory like "/home/username/programs"
# just so it is easy to find
export INSTALL_LOCAL="/path/to/install/location"

# this is to help you organize manually installing programs
mkdir -p "${INSTALL_LOCAL}/bin" "${INSTALL_LOCAL}/include" "${INSTALL_LOCAL}/src" 
mkdir -p "${INSTALL_LOCAL}/lib" "${INSTALL_LOCAL}/lib64" "${INSTALL_LOCAL}/share"

# download a new version of python
wget "https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz"

# uncompress it
tar -xJvf "Python-3.7.0.tar.xz"

# move into the new directory
cd Python-3.7.0

# make a temporary build directory
mkdir _build_dir && cd _build_dir

# configure the program install to your system
# --prefix is the location to install something to
../configure --prefix="${INSTALL_LOCAL}/src/Python/3.7.0"

# compiles the program and moves the appropriate files
make && make install

# installprogram.sh is a small bash script to install programs
# to a more common directory. This has to be in the same level
# as the src bin ... 

# copy the installprogram.sh file from the github/Day1-Linux
# repo into the INSTALL_LOCAL location you set above
# move into that install location
cp ../../installprogram.sh "${INSTALL_LOCAL}/"
cd "${INSTALL_LOCAL}/"

# now call the installprogram.sh shell script.
# This program just goes into the src/ directory and gets
# the program you specify and updates the appropriate 
# directories.
./installprogram.sh Python/3.7.0

# so all you have to do now is update your path
# you can add this to your .*rc file
export PATH="${INSTALL_LOCAL}/bin:${PATH}"

# end of file
