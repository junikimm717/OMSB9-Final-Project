#!/usr/bin/env bash


FILES=($(ls))

X=0

for i in ${FILES[*]}; do
    mv $i $X.PNG
    X=$(($X + 1))
    echo $X
done
