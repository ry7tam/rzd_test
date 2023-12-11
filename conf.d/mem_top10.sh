#!/bin/bash
z=$(ps aux)
while read -r z
do
   var=$var$(awk '{print "memory_usage{process=\""$11"\", pid=\""$2"\"}", $4z}');
done <<< "$z"

echo $var >> /home/data/mem_top10.prom
