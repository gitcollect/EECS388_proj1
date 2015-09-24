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
        echo "  $3 success!"
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

diff_out part1_2_out.txt Part1_2/part1_2_correct.txt "length extentions"
echo "Part 1.2 Sucsess"

# copy the file to the correct directory
copy_to_submit_folder Part1_2/len_ext_attack.py

# Part 2.1
cp Part2_1/generating_collisions.txt Submition/
echo "Part 2.1 Sucsess"

# Part 2.2

#Tests
# comparing the two hashes
H1=$(openssl dgst -md5 Part2_2/good.py | grep -o '[0-9a-f]*$')
H2=$(openssl dgst -md5 Part2_2/evil.py | grep -o '[0-9a-f]*$')

echo "  SSL good.py $H1"
echo "  SSL evil.py $H2"

if [ $H1 != $H2 ]
then
    echo "  The hashes are different"
    exit 1
else
    echo "  The hashes are the same"
fi

python Part2_2/good.py > good_test.txt
diff_out  good_test.txt Part2_2/out_good.txt "good.py"

python Part2_2/evil.py > evil_test.txt
diff_out evil_test.txt Part2_2/out_evil.txt "evil.py"

copy_to_submit_folder Part2_2/good.py
copy_to_submit_folder Part2_2/evil.py

echo "Part 2.2 Sucesss"


# run test for part 3.3
python Part3_3/test.py > out.txt
diff_out out.txt Part3_3/test_sig_out_aggents_server.out "test.py"

python Part3_3/bleichenbacher.py "eecs388+coconor+1000" > out.txt
diff_out out.txt Part3_3/bleichenbacher_sig.out "Signature Comparison"

copy_to_submit_folder Part3_3/bleichenbacher.py

echo "Part 3.3 Sucess"


copy_to_submit_folder writeup.txt
echo "Copying writeup.txt"

# finaly create tar
tar -zcf project1.coconor.cwscott.tar.gz Submition/*


