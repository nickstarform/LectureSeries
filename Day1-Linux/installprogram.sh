#!/bin/bash

args="${1}"
cwd=`pwd`

if [ -z ${args} ]; then
    echo "Must specify a program/version to install/update"
    echo "example \`installprogram Python/3.7.0\`"
    exit
elif [ "${args}" == "--help" ]; then
    echo "Following a certain structure will try to install"\
    echo "programs in a more common directory"
    echo
    echo "Run the \`installprogram make\` to create the directory structure"\ 
    echo "and run \`installprogram clean\` when you delete a program from src"
    exit
elif [ "${args}" == "--help" ]; then
    echo "Following a certain structure will try to install"\
    echo "programs in a more common directory"
    echo
    echo "Run the \`installprogram make\` to create the directory structure"\
    echo "and run \`installprogram clean\` when you delete a program from src"
    exit
elif [ "${args}" == "clean" ]; then
    find . -type l -exec sh -c 'for x; do [ -e "$x" ] || rm "$x"; done' _ {} +
    echo "Removed all broken symlinks"
    exit
elif [ "${args}" == "make" ]; then
    mkdir -p "bin" "include" "src" "lib" "lib64" "share"   
    echo "Created the structure needed. Install programs to "\
    echo "src/ProgramName/version and then rerun this file with the"\
    echo "command \`installprogram ProgramName/version\`"
    exit
fi

if [ ! -d "src/${args}" ]; then
    echo "src/${args} not found within sub-directories"
    echo "Assuming the directory follows the form src/Program/version"
    exit
fi

IFS='/' read -ra ADDR <<< "${args}"

program="${ADDR[0]}"
version="${ADDR[1]}"
location="${cwd}/src/${args}"

clear

echo "Installing program ${program}, version ${version}"

read -p "Please press [ENTER] to continue or CTRL-C to cancel" var
if [ ${#var} -ne 0 ]; then
  exit
fi

for d in ${location}/*/ ; do
    IFS='/' read -ra ADDR <<< "${d}"
    subdir="${ADDR[-1]}"
    # echo "${d} -> ${cwd}/${subdir}/"
    ln -sf ${d}/* "${cwd}/${subdir}/"
done

echo "Files can be found in ${cwd}/bin"
echo "Add this to your path via "
echo "export PATH=\"${cwd}/bin:\${PATH}\""
echo "or adding to your ~/.bashrc or ~/.bash_profile"

# end of file
