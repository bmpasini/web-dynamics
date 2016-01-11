# !/bin/bash
ROOT_PATH="/san_data/research/bmpasini/domain-analysis"
JOB_PATH="$ROOT_PATH/script/2-new-links/4-rate-url"
INPUT_PATH="$ROOT_PATH/script/2-new-links/1-url/NewLinks"
OUTPUT_PATH="$JOB_PATH/NewLinksRateUrl"

function run_hadoop {
    echo "Run hadoop..."
    
    rm -rf $OUTPUT_PATH/
    chmod +x $JOB_PATH/map-1.py $JOB_PATH/reduce-1.py
    /san_data/research/bmpasini/lib/hadoop-2.6.0/bin/hadoop jar /san_data/research/bmpasini/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=4 \
    -file $JOB_PATH/map-1.py \
    -mapper $JOB_PATH/map-1.py \
    -file $JOB_PATH/reduce-1.py \
    -reducer $JOB_PATH/reduce-1.py \
    -input file://$INPUT_PATH/part-00000 \
    -output file://$OUTPUT_PATH
}

run_hadoop

sleep 1
echo "Waiting analysis finish..."
wait
echo "done."
