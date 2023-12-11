#!/bin/bash

process_info=$(ps -eo pid,comm,%mem --sort=-%mem | head -n 11 | tail -n 10)

 echo "$process_info" | while read -r pid cmd mem; do
    echo top_10_mem"{id=\"$pid\",name=\"$cmd\",memory=\"$mem\"}" $(date +%s) >> 5.prom
done
