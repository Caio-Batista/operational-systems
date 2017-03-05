#!/bin/bash

entrada=$1
tipodepolitica=$2

tempodeexecucao=0;
for i in `seq 1 $entrada`;
do
	tempo=`date +%s`
	./cpu_burn $tipodepolitica
 	tempo2=`date +%s`
	runtime=$((tempo2-tempo))
	tempodeexecucao=$((tempodeexecucao+runtime))	
	
done
echo "Execucoes: " $entrada  " tempo em s: "  $tempodeexecucao
