#!/bin/bash

#This script create a files in .rst format to generate html documentation with Sphinx.
#The files included will be all *.py files located on the current folder.
#The content will be printed on the screen. To print the content on one file you can do:
#./this_script_name.sh Title Subtitle > package_name_doc.rst

if [ $# -lt 2 ]
then
echo "Usage: ${0} 'Package Name Documentation' 'Package Name'"
echo "Example: ${0} 'Cocktail Party Documentation' 'Cocktail Party'";echo; exit
fi

title=${1}
subtitle=${2}

#Printing title.
text=''
for i in $(seq 0 ${#title}); do text=$text'='; done
echo $title
echo $text
echo

#Printing subtitle.
text=''
for i in $(seq 0 ${#subtitle}); do text=$text'-'; done
echo $subtitle
echo $text
echo

#Printing the title and the documentation of the files.
for file in `ls *.py`
do
echo $file
len=${#file}
text=''
for i in $(seq 0 $len);do text=$text'.'; done
echo $text
echo '.. automodule:: ' `echo $file | cut -d'.' -f1`
echo '   :members:'
echo
done
