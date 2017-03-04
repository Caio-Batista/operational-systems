#!/bin/bash

entrada=$1
tmp=0
for i in `seq 1 $entrada`;
do
	tempo=`date +%s`
	./cpu_burn
 	tempo2=`date +%s`
	runtime=$((tempo2-tempo))
	echo $runtime
done
