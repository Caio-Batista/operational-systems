#!/bin/bash

entrada=$1

for i in `seq 1 $entrada`;
do
	time ./cpu_burn &
done
