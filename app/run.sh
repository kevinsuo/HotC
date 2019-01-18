#!/bin/sh

#sudo docker start bridge1

i=1
N=10

while [ $i -le $N ]
do

#	get nanosecond
	var1=`date "+%s%N"`

	sudo docker start bridge1

#	sudo docker exec bridge1 nodejs test.js
#	sudo docker exec bridge1 python test.py
	sudo docker exec bridge1 ./run-java.sh
#	sudo docker exec bridge1 ./run-go.sh


	var2=`date "+%s%N"`

	diff=`expr $var2 - $var1`

	sudo docker stop bridge1

	echo $diff

	sleep 3
	i=$(( $i + 1 ))
done
