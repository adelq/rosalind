#!/usr/bin/env bash

rm *.fa

while read line
do
  if [[ ${line:0:1} == '>' ]]
  then
    outfile=${line#>}.fa
    echo $line > $outfile
  else
    echo $line >> $outfile
  fi
done < ${1}

lalign36 *.fa |
    grep -A3 "100.0% identity" |
    tail -n1 |
    cut -f2 -d" " |
    tee /dev/tty |
    wc -c
