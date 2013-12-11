#!/bin/bash

#This script shows the dependence's tree of a package
#Usage: list_dependences.sh package_name_that_yoy_want_see_the_tree
#Example: list_dependences.sh text_to_speech



#(package_name, level) parameters
function list_dep {

	deps=`rospack depends1 $1`

	for package in $deps; do
		points=""
		for ident in $(seq 0 $2); do points="$points........"; done
		echo $points $package
		list_dep $package `expr $2 + 1`
	done
}

if [ $# -lt 1 ]; then echo "Usage: $0 package_name"; echo "Example: $0 text_to_speech"; exit; fi

echo $1
list_dep $1 0

