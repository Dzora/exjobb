#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Please enter host ip"
	exit 1
fi

sh run.sh "$1" 30080 5 0 5