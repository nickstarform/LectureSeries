
mkdir testing && cd testing

git init

echo "This is a test of how branches work. Master" > test.txt

git add test.txt

git commit -m 'testing commit'

git status

git branch

git branch devel
 
git checkout devel

cat test.txt

sed -i 's/Master/Test/g' test.txt

git status

cat test.txt

git checkout test.txt

sed -i 's/Master/Test/g' test.txt

git add test.txt

git commit -m 'testing commit. Testing branch'

git status

git add test.txt

git commit -m 'testing commit'

git log

git checkout master

git log
