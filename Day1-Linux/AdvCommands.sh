#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It goes through some more advanced commands that will be used
# and that the users should be comfortable with

# Slide 

echo "This file is for testing seed and awk" >> sedawk.txt

# made an error lets fix it

sed -i.backup 's/seed/sed/g' sedawk.txt

cat sedawk.txt

awk -F' ' '{ print "Created with "$6 " and read with "  $8 }' sedawk.txt

find . name -type f

which sed


