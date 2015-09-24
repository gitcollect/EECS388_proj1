#!/usr/bin/env bash


# function pulled from submit.sh
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



python test.py > out.txt
diff_out out.txt test_sig_out_aggents_server.out "test.py"

python bleichenbacher.py "eecs388+coconor+1000" > out.txt
diff_out out.txt bleichenbacher_sig.out "Signature Comparison"





