#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It goes through the basic commands that will be used
# and that the users should be comfortable with

# Slide 
export INSTALL_LOCAL="/path/to/install/location"

mkdir -p "${INSTALL_LOCAL}/bin" "${INSTALL_LOCAL}/include" "${INSTALL_LOCAL}/src" 
mkdir -p "${INSTALL_LOCAL}/lib" "${INSTALL_LOCAL}/lib64" "${INSTALL_LOCAL}/share"

# Slide 

wget "https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz"

tar -xJvf "Python-3.7.0.tar.xz"

cd Python-3.7.0

mkdir _build_dir && cd _build_dir

../configure --prefix="${INSTALL_LOCAL}/src/Python/3.7.0"

make && make install

# Slide 
# installprogram.sh is a small bash script to install programs
# to a more common directory. This has to be in the same level
# as the src bin ... 

cp ../../installprogram.sh "${INSTALL_LOCAL}/"
cd "${INSTALL_LOCAL}/"
./installprogram.sh Python/3.7.0
