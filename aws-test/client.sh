#!/bin/sh

sleeplittle=10
sleepbig=1000

j=1

while [ $j -le 10 ]
do
    i=1

    while [ $i -le 10 ]
    do
    #returns the seconds and current nanoseconds
    var1=`date +%s%N`

    #visit AWS gateway API address
    #backend function is a python application generating random number
    curl https://a5wqxok61f.execute-api.us-east-2.amazonaws.com/test/
    var2=`date +%s%N`

    result=$((var2 - var1))

    echo ""
    echo $result

    sleep $sleeplittle
    i=$(( $i + 1 ))
     done

     sleep $sleepbig

     echo ""
     echo ""
     echo "After 1000s idle"

     j=$(( $j + 1 ))
done