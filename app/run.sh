#!/bin/sh

#sudo docker start bridge1

var1=`date "+%s%N"`
sudo docker exec bridge1 python test.py
var2=`date "+%s%N"`

diff=`expr $var2 - $var1`

echo $diff
