#!/usr/bin/env bash

# fastcoll is currently living in Part2_1 dir
./../Part2_1/fastcoll -p prefix -o col1 col2

cat col1 suffix > file1.py
cat col2 suffix > file2.py

H1=$(openssl dgst -md5 file1.py | grep -o '[0-9a-f]*$')
H2=$(openssl dgst -md5 file2.py | grep -o '[0-9a-f]*$')

echo "SSL file1.py $H1"
echo "SSL file2.py $H2"

if [ $H1 != $H2 ]
then
    echo "The hashes are different"
    exit 1
else
    echo "The hashes are the same"
fi

