#!/bin/bash

# $DIR is the path to the directory where this specific script is sitting
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Help
usage()
{
  echo "ERROR - Usage:"
  echo
  echo "      sh $(basename $0) OPTIONSTRINGS ..."
  echo
  echo "Options with arguments:"
  echo "  -h    Help                   (Display this message)"
  echo "  -d    nano skim dir          (Path to the NanoSkim outputs)"
  echo
  exit
}

# Command-line opts
while getopts ":d:h" OPTION; do
  case $OPTION in
    d) NANOSKIMDIR=${OPTARG};;
    h) usage;;
    :) usage;;
  esac
done

if [ -z ${NANOSKIMDIR} ]; then usage; fi

# to shift away the parsed options
shift $(($OPTIND - 1))

# Verbose
date
echo "================================================"
echo "$(basename $0) $*"
echo "$(basename $0) $*" >> $DIR/.$(basename $0).history
echo "------------------------------------------------"
echo "NANOSKIMDIR    : ${NANOSKIMDIR}"
echo "================================================"

TAG=$(basename $NANOSKIMDIR)
NFSDIR=/nfs-7/userdata/phchang/VBSHWWNanoSkim_${TAG}/
NSAMPLES=$(ls -d ${NANOSKIMDIR}/* | wc -l)

rm -f .haddjobs.txt
IDX=1
for SAMPLEDIR in $(ls -d ${NANOSKIMDIR}/*); do
    SAMPLENAME=$(basename ${SAMPLEDIR})
    MERGEDDIR=${NFSDIR}/${SAMPLENAME}/merged/
    mkdir -p ${MERGEDDIR}
    echo "Processing ... ${IDX} / ${NSAMPLES} samples (dataset=${SAMPLENAME})"
    if [ ! -f ${MERGEDDIR}/nevents.txt ]; then
        TOTALNEVENTS=0
        TOTALNEFFEVENTS=0
        for NEVENTSFILE in $(ls $SAMPLEDIR/*_nevents.txt); do
            POSWEIGHTS=$(tail -n 2 $NEVENTSFILE | head -n 1)
            NEGWEIGHTS=$(tail -n 1 $NEVENTSFILE)
            TOTALNEVENTS=$((TOTALNEVENTS + ${POSWEIGHTS}))
            TOTALNEVENTS=$((TOTALNEVENTS + ${NEGWEIGHTS}))
            TOTALNEFFEVENTS=$((TOTALNEFFEVENTS + ${POSWEIGHTS}))
            TOTALNEFFEVENTS=$((TOTALNEFFEVENTS - ${NEGWEIGHTS}))
        done
        echo ${TOTALNEVENTS} > ${MERGEDDIR}/nevents.txt
        echo ${TOTALNEFFEVENTS} >> ${MERGEDDIR}/nevents.txt
    fi
    # hadding
    if [ ! -f ${MERGEDDIR}/output.root ]; then
        if [ ! -f ${DIR}/haddnano.py ]; then
            wget https://raw.githubusercontent.com/cms-nanoAOD/nanoAOD-tools/master/scripts/haddnano.py -O ${DIR}/haddnano.py
        fi
        CMD="python ${DIR}/haddnano.py ${MERGEDDIR}/output.root ${SAMPLEDIR}/*.root > ${MERGEDDIR}/output_hadd.log 2>&1"
        echo $CMD >> .haddjobs.txt
        # EXITCODE=$?
        # if [ $EXITCODE -ne 0 ]; then
        #     echo $CMD
        #     echo "ERROR - Fail to process $SAMPLEDIR"
        #     exit
        # fi
    fi
    IDX=$((IDX + 1))
done

xargs.sh .haddjobs.txt
