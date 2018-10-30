#!/bin/bash

# This file will walk you through the lecture for Day 1. 
# It goes through some more advanced commands that will be used
# and that the users should be comfortable with

# ssh'ing into the nhn system
ssh username@login.nhn.ou.edu
# try to open caja ./ it fails since no GUI

# now allow gui
ssh -XY username@login.nhn.ou.edu
# try again
# caja ./

# while ssh issue vncserver
# take note of the computer (hostname) and which display (:1)
vncviewer -via username@login.nhn.ou.edu computer:display

# end of file
