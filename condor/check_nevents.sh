#!/bin/bash

TAG=v2.5

diff -s <(grep "UL17" samples.py | grep -v "    #" | grep -v "C2V" | col 14 | sort -g) <(head -q -n1 `ls /nfs-7/userdata/phchang/VBSHWWNanoSkim_${TAG}/*UL17*/merged/nevents.txt | grep -v C2V` | sort -g)
paste   <(grep "UL17" samples.py | grep -v "    #" | grep -v "C2V" | col 14 | sort -g) <(head    -n1 `ls /nfs-7/userdata/phchang/VBSHWWNanoSkim_${TAG}/*UL17*/merged/nevents.txt | grep -v C2V` | grep -v "^$" | paste -d" " - - | awk '{print $4, $2}' | sort -g) | column -s $'\t' -t

diff -s <(grep "UL18" samples.py | grep -v "    #" | grep -v "C2V" | col 14 | sort -g) <(head -q -n1 `ls /nfs-7/userdata/phchang/VBSHWWNanoSkim_${TAG}/*UL18*/merged/nevents.txt | grep -v C2V` | sort -g)
paste   <(grep "UL18" samples.py | grep -v "    #" | grep -v "C2V" | col 14 | sort -g) <(head    -n1 `ls /nfs-7/userdata/phchang/VBSHWWNanoSkim_${TAG}/*UL18*/merged/nevents.txt | grep -v C2V` | grep -v "^$" | paste -d" " - - | awk '{print $4, $2}' | sort -g) | column -s $'\t' -t
