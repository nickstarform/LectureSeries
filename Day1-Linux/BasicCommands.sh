#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It goes through the basic commands that will be used
# and that the users should be comfortable with

# makes a file with hello world on first line
echo "Hello World!" >> hello.txt

# replies with hello world
cat hello.txt

# copy file to new name
cp hello.txt hello_copy.txt

# list all files
ls 

# make a directory
mkdir testing

# move file to new name
mv hello.txt testing/hello_mv.txt

# make a new file with a spelling error
echo "Hello Wrld" >> hello.txt

# show the difference
diff hello.txt testing/hello_mv.txt

# correct the current file with regex
sed -i 's/Wrld/World/g' hello.txt

# print out World!
awk '{print $2}' hello.txt 

# show the difference
diff hello.txt testing/hello_mv.txt

# which cat program are you using
which cat

# show the man page
man cat

# append your current working directory to hello.txt
echo `pwd` >> hello.txt

# read the last line
tail -n1 hello.txt

# read the first line
head -n1 hello.txt

# move to the new directory
cd testing

# symbolic link (soft link) the file to a new name
ln -sf ../hello.txt ./hello.sym.txt

# move to the higher directory
cd ..

# tarball and compress the testing directory
tar -czvf testing.tar.gz testing

# see all the new files
ls

# end of file
