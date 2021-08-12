#!/bin/bash

REFTAG=v2.4
TARTAG=v2.5
NFSBASEDIR=/nfs-7/userdata/phchang
PREFIX=VBSHWWNanoSkim_

# Loop over reference tag directory
for i in $(ls -d ${NFSBASEDIR}/${PREFIX}${REFTAG}/*); do
    # Replace ${REFTAG} with ${TARTAG}
    REFSAMPLENAME=$(basename ${i})
    TARSAMPLENAME=$(basename ${i//_${REFTAG}/_${TARTAG}})
    REFNEVENTS=${NFSBASEDIR}/${PREFIX}${REFTAG}/${REFSAMPLENAME}/merged/nevents.txt
    TARNEVENTS=${NFSBASEDIR}/${PREFIX}${TARTAG}/${TARSAMPLENAME}/merged/nevents.txt
    # Check whether both nevents.txt are found
    if [ -f ${REFNEVENTS} ] && [ -f ${TARNEVENTS} ]; then
        diff ${REFNEVENTS} ${TARNEVENTS}
        # if exit status not equal to 0 then something is wrong
        if [ $? -ne 0 ]; then
            echo "Found difference"
            echo ${TARNEVENTS}
            cat ${TARNEVENTS}
            echo ${REFNEVENTS}
            cat ${REFNEVENTS}
        fi
    else
        echo ${TARSAMPLENAME}
        echo ${REFSAMPLENAME}
        echo "Did not find both"
    fi
done

