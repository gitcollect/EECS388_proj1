#!/usr/bin/env bash

if [ -e fastcoll ]
then
    echo "Generating Collisions"
else
    echo "Compiling fastcoll"
    make -C fastcoll_dir/
    mv fastcoll_dir/fastcoll  ../
fi


