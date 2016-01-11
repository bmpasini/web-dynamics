# !/bin/bash
ROOT_PATH="/san_data/research/bmpasini/domain-analysis"
JOB_PATH="$ROOT_PATH/script/2-new-links/1-url"
INPUT_PATH="$ROOT_PATH/script/0-outlinks-relevance/2-merge-files/pageData"
OUTPUT_PATH="$JOB_PATH/NewLinks"

function run_hadoop {
    echo "Run hadoop on $2"
    
    rm -rf $OUTPUT_PATH/
    chmod +x $JOB_PATH/map.py $JOB_PATH/reduce.py
    /san_data/research/bmpasini/lib/hadoop-2.6.0/bin/hadoop jar /san_data/research/bmpasini/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=4 \
    -file $JOB_PATH/map.py \
    -mapper $JOB_PATH/map.py \
    -file $JOB_PATH/reduce.py \
    -reducer $JOB_PATH/reduce.py \
    -input file://$INPUT_PATH/ebola/2015-12-15/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-16/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-17/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-18/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-19/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-20/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-21/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-22/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-23/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-24/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-25/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-26/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-27/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-28/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-29/part-00000 \
    -input file://$INPUT_PATH/ebola/2015-12-30/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-01/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-02/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-03/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-04/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-05/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-06/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-07/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-08/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-09/part-00000 \
    -input file://$INPUT_PATH/ebola/2016-01-10/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-15/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-16/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-17/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-18/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-19/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-20/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-21/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-22/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-23/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-24/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-25/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-26/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-27/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-28/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-29/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-30/part-00000 \
    -input file://$INPUT_PATH/movies/2015-12-31/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-01/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-02/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-03/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-04/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-05/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-06/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-07/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-08/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-09/part-00000 \
    -input file://$INPUT_PATH/movies/2016-01-10/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-19/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-20/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-21/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-22/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-23/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-24/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-25/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-26/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-27/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-28/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-29/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-30/part-00000 \
    -input file://$INPUT_PATH/movies-2/2015-12-31/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-01/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-02/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-03/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-04/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-05/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-06/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-07/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-08/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-09/part-00000 \
    -input file://$INPUT_PATH/movies-2/2016-01-10/part-00000 \
    -output file://$OUTPUT_PATH
}

run_hadoop

sleep 1
echo "Waiting analysis finish..."
wait
echo "done."
