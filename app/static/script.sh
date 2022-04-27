#!/bin/bash

# changing the name of all the files in a directory to numbers
echo $((i++))
for FILE in $1/*
do
    mv $FILE $1/$((i++)).jpg
done
