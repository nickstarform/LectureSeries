#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It goes through the basic commands that will be used
# and that the users should be comfortable with

echo "Hello World!" >> hello.txt

cat hello.txt

cp hello.txt hello_copy.txt

ls 

mkdir testing

mv hello.txt testing/hello_mv.txt

echo "Hello Wrld" >> hello.txt

diff hello.txt testing/hello_mv.txt

sed -i 's/Wrld/World/g' hello.txt

awk '{print $2}' hello.txt 

diff hello.txt testing/hello_mv.txt

which cat

man cat

echo `pwd` >> hello.txt

tail -n1 hello.txt

head -n1 hello.txt

cd testing

ln -sf ../hello.txt ./hello.sym.txt

cd ..

tar -czvf testing.tar.gz testing

ls

# end of file
