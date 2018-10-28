# This file will help teach you some of the basics about using git

# create a test directory to make changes into
mkdir testing && cd testing

# initialize a new git repo (creates a .git dir in the current directory)
git init

# put some string into a file
echo "This is a test of how branches work. Master" > test.txt

# "stages" this file/directory. This holds and tracks changes made to the file now
git add test.txt

# commits the things that are staged with a message
git commit -m 'testing commit'

# see any changes to the tracked objects
git status

# see the branches
git branch

# make a branch
git branch devel
 
# move to the branch
git checkout devel

# notice the file is the same
cat test.txt

# change the file
sed -i 's/Master/Test/g' test.txt

# check what git tracks
git status

# see the changes exactly
git diff test.txt

# reset the changes back to the HEAD
git checkout test.txt

# change the file again and make a .bak backup
sed -i.bak 's/Master/Test/g' test.txt

# stage both files
git add test.txt*

# commit them
git commit -m 'testing commit. Testing branch'

# see the changes
git status

# check the difference between two branches
git diff master

# check the log of commits
git log

# move to the master branch
git checkout master

# check the log again
git log

# merge the devel branch to the master
git merge devel

# see the differences
ls

# clone the LectureSeries repo from github
# git clone works on any "bare" repo
git clone https://github.com/nickalaskreynolds/LectureSeries.git

# move into the directory
cd LectureSeries

# see what is inside
ls

# show what remote repos are saved
git remote show

# make a new file in the current directory
touch test.txt

# see the change
git status

# add the new change
git add test.txt && git commit -m 'testing'

# try to push the change to the remote repo
# (will fail since you dont have write access)
git remote push origin master
