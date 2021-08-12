#!/bin/bash

rm -rf .jobs.txt
for i in $(condor_q -af ClusterId ProcId -constraint "JobStatus==5" | tr ' ' '.'); do
    echo "sh run_condor_job_locally.sh ${i} > logs/${i}.log 2>&1" >> .jobs.txt
done

xargs.sh .jobs.txt
