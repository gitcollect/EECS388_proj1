#!/usr/bin/env bash

# Variables

# moves the file to the submit folder
function copy_to_submit_folder {
    cp $1 Submition/
}

function diff_out {
    DIFF=$(diff $1 $2)

    if [ "$DIFF" != "" ]
    then
        echo "ERROR in $3"
        exit 1
    else
        echo "$3 success!"
        rm $1
    fi
}

#Clean submition
rm -f Submition/*
rm -f *.tar

echo "Submiting for EECS 388 Project 1"

# Part 1.2
# Test Part 1 aggainst the Server
python Part1_2/len_ext_attack.py "http://eecs388.org/project1/api?token=a1913e8031748f7a5dbd070125bd1cd1&user=admin&command1=ListFiles&command2=NoOp" > part1_2_out.txt

diff_out part1_2_out.txt Part1_2/part1_2_correct.txt "Part 1.2"

# copy the file to the correct directory
copy_to_submit_folder Part1_2/len_ext_attack.py

echo "Part 2.2 Sucsess"
cp Part2_1/generating_collisions.txt Submition/


# finaly create tar
tar -zcf project1.coconor.cwscott.tar.gz Submition/*


