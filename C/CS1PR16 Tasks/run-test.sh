#!/bin/bash

# This little script runs the tests defined in the directory test and compares
# the output of your program with the expected output.
#
# You do not need to temper with it.

if [[ "$1" == "" ]]; then
	echo "Synopsis: $0 <executable-to-test>"
	exit 1
fi

if [[ ${1:0:1} == "/" ]]; then
	p=$1
else
	p=./$1
fi

if [[ ! -e $p ]]; then
	echo "Cannot find the executable: $p"
	exit 1
fi

if [[ ! -e test ]] ; then
	echo "Could not find the test directory!"
	exit 1
fi

if [[ $(ls test|grep ".in$"|wc -l) == 0 ]] ; then
	echo "Could not find a test inside the test directory"
	exit 1
fi

summarks=0
totalmarks=0

for i in test/*.in ; do
	marks=${i%.in}.marks
	if [[ -e $marks ]]; then
		marks=$(cat $marks)
	else
		marks=1
	fi
	totalmarks=$(($totalmarks + $marks))

  out=${i%.in}.out
	param=${i%.in}.param
	if [[ -e $param ]]; then
    mapfile -t < "$param"
		$p "${MAPFILE[@]}" < $i > tmp 2>&1
	else
		$p < $i > tmp 2>&1
	fi
	ERR=$?
	if [[ $ERR == 0 ]] ; then
  	cmp -s tmp $out > /dev/null
		ERR=$?
		if [[ $ERR != 0 ]]; then
	    echo ">>> Got >>>>>>>>"
	    cat tmp
	    echo "<<<<<<<<<<<<<<<<"
			echo
	    echo ">>> Expected >>>"
	    cat $out
	    echo "<<<<<<<<<<<<<<<<"
		fi
	fi
  if [[ $ERR != 0 ]]; then
    echo "ERR: $ERR"
  else
    echo "OK: $i"
		summarks=$(($summarks + $marks))
  fi
done

echo
echo "Total $summarks/$totalmarks"

rm tmp
