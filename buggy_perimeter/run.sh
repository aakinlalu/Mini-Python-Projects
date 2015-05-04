#!/usr/bin/env bash

# Make sure that python file is execuatble
chmod +x ./perimeter.py

# run perimeter script for each of the sample data csv files
for f in ./sample_data/*.csv
do
    printf "%-28s" $f
    ./perimeter.py $f
done
