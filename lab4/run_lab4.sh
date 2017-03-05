#!/bin/bash

tipodepolitica=$1
numerodecpus=2;

for i in `seq 1 15`;
do
sudo perf sched record ./run_cpu_burn.sh $numerodecpus $tipodepolitica
sudo perf sched latency | grep run_cpu_burn
done																																	
