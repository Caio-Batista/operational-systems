#!/bin/bash

entrada=$1

for i in `seq 1 15`;
do
sudo perf sched record ./run_cpu_burn.sh $entrada
sudo perf sched latency | grep run_cpu_burn
done
