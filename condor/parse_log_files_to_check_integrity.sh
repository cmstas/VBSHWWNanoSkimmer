
usage()
{
    echo "Usage:"
    echo ""
    echo "       sh $0 TAG"
    echo ""
    echo ""
    exit
}

if [ -z $1 ]; then
    usage
fi

TAG=$1

for DIR in $(ls -d tasks/CondorTask_*${TAG}); do

    # Compute
    IDXS=$(grep -r "output_.*.root" ${DIR}/logs/std_logs/ | grep "TRANSFER:EXIT" | sort -g | uniq  | tr "/" " " | col 26 | tr "_" " "  | tr "." " " | col 2 | sort -g | uniq)
    NFILES=$(grep -r "output_.*.root" ${DIR}/logs/std_logs/ | grep "TRANSFER:EXIT" | sort -g | uniq  | tr "/" " " | col 26 | tr "_" " "  | tr "." " " | col 2 | sort -g | uniq | wc -l)
    LASTINDEX=$(grep -r "output_.*.root" ${DIR}/logs/std_logs/ | grep "TRANSFER:EXIT" | sort -g | uniq  | tr "/" " " | col 26 | tr "_" " "  | tr "." " " | col 2 | sort -g | uniq | tail -n 1)

    if [[ "${NFILES}" != "${LASTINDEX}" ]]; then

        # Printing summary
        echo "===================================================================================="
        echo Checking ... $DIR
        echo "NFILES: ${NFILES}"
        echo "LASTINDEX: ${LASTINDEX}"
        echo "===================================================================================="
        echo ""

        # Printing indexs that are found in the log files
        rm -f .idxs.txt
        for idx in ${IDXS}; do
            echo $idx >> .idxs.txt
        done

        # Printing the full sequence
        rm -f .seqs.txt
        for idx in $(seq ${LASTINDEX}); do
            echo $idx >> .seqs.txt
        done

        # Printing difference
        for IDX in $(diff .idxs.txt .seqs.txt | grep ">" | awk '{print $2}'); do
            # echo ${IDX}
            # echo ${DIR}/logs/std_logs/
            OUTPUTDIR=$(grep -r "OUTPUTDIR" ${DIR}/logs/std_logs/ | awk '{print $2}' | sort -g | uniq)
            OUTPUTFILE=$(ls ${OUTPUTDIR}/output_${IDX}.root 2>/dev/null)
            OUTPUTNEVENTSFILE=$(ls ${OUTPUTDIR}/output_${IDX}_nevents.txt 2>/dev/null)
            echo "   Checking ... ${OUTPUTDIR}/output_${IDX}.root"
            if [ -f "${OUTPUTFILE}" ]; then
                echo "   OUTPUTFILE        EXISTS"
            else
                echo "   OUTPUTFILE        MISSING"
            fi
            if [ -f "${OUTPUTNEVENTSFILE}" ]; then
                echo "   OUTPUTNEVENTSFILE EXISTS"
            else
                echo "   OUTPUTNEVENTSFILE MISSING"
            fi
        done

        echo ""
    fi
done
