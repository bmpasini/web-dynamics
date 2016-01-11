# !/bin/bash
ROOT_PATH="/san_data/research/bmpasini/domain-analysis"
JOB_PATH="$ROOT_PATH/script/2-new-links/6-rate-domain"
INPUT_PATH="$ROOT_PATH/script/2-new-links/5-rate-site/NewLinksRateSite"
OUTPUT_PATH="$JOB_PATH/NewLinksRateDomain"

function run_hadoop {
    echo "Run hadoop on $1"
    
    rm -rf $OUTPUT_PATH/
    chmod +x $JOB_PATH/map.py $JOB_PATH/reduce.py
    /san_data/research/bmpasini/lib/hadoop-2.6.0/bin/hadoop jar /san_data/research/bmpasini/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=2 \
    -file $JOB_PATH/map.py \
    -mapper $JOB_PATH/map.py \
    -file $JOB_PATH/reduce.py \
    -reducer $JOB_PATH/reduce.py \
    -input file://$INPUT_PATH/part-00000 \
    -output file://$OUTPUT_PATH
}

run_hadoop

sleep 1
echo "Waiting analysis finish..."
wait
echo "done."
