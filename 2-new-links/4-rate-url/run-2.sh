# !/bin/bash
ROOT_PATH="/san_data/research/bmpasini/domain-analysis"
JOB_PATH="$ROOT_PATH/script/2-new-links/4-rate-url"
EBOLA_SEEDS_PATH="/san_data/research/aeciosantos/topic-dynamics/ebola/ebola.6perdomain.seeds"
MOVIES_SEEDS_PATH="/san_data/research/aeciosantos/topic-dynamics/movies/movies.6perdomain.seeds"
INPUT_PATH="$JOB_PATH/NewLinksRateUrl"
OUTPUT_PATH="$JOB_PATH/NewLinksRateUrlSeeds"

function run_hadoop {
    echo "Run hadoop..."
    
    rm -rf $OUTPUT_PATH/
    chmod +x $JOB_PATH/map-2.py $JOB_PATH/reduce-2.py
    /san_data/research/bmpasini/lib/hadoop-2.6.0/bin/hadoop jar /san_data/research/bmpasini/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=4 \
    -file $JOB_PATH/map-2.py \
    -mapper $JOB_PATH/map-2.py \
    -file $JOB_PATH/reduce-2.py \
    -reducer $JOB_PATH/reduce-2.py \
    -input file://$EBOLA_SEEDS_PATH \
    -input file://$MOVIES_SEEDS_PATH \
    -input file://$INPUT_PATH/part-00000 \
    -output file://$OUTPUT_PATH
}

run_hadoop

sleep 1
echo "Waiting analysis finish..."
wait
echo "done."
