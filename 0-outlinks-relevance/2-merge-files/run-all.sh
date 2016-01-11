# !/bin/bash
ROOT_PATH="/san_data/research/bmpasini/domain-analysis"
JOB_PATH="$ROOT_PATH/script/0-outlinks-relevance/2-merge-files"
INPUT_PATH="$ROOT_PATH/script/0-outlinks-relevance/1-outlinks-relevance/OutlinksRelevance"
OUTPUT_PATH="$JOB_PATH/pageData"

function run_hadoop {
    echo "Run hadoop on $2"
    
    rm -rf $OUTPUT_PATH/$1/$2
    chmod +x $JOB_PATH/map.py $JOB_PATH/reduce.py
    /san_data/research/bmpasini/lib/hadoop-2.6.0/bin/hadoop jar /san_data/research/bmpasini/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=1 \
    -file $JOB_PATH/map.py \
    -mapper $JOB_PATH/map.py \
    -file $JOB_PATH/reduce.py \
    -reducer $JOB_PATH/reduce.py \
    -input file://$ROOT_PATH/$1/pageData-$2 \
    -input file://$INPUT_PATH/$1/$2/part-00000 \
    -output file://$OUTPUT_PATH/$1/$2
}

function run_domain {
    echo "Generating files for $1"

    rm -rf $OUTPUT_PATH/$1/
    run_hadoop $1 2015-12-15
    run_hadoop $1 2015-12-16
    run_hadoop $1 2015-12-17
    run_hadoop $1 2015-12-18
    run_hadoop $1 2015-12-19
    run_hadoop $1 2015-12-20
    run_hadoop $1 2015-12-21
    run_hadoop $1 2015-12-22
    run_hadoop $1 2015-12-23
    run_hadoop $1 2015-12-24
    run_hadoop $1 2015-12-25
    run_hadoop $1 2015-12-26
    run_hadoop $1 2015-12-27
    run_hadoop $1 2015-12-28
    run_hadoop $1 2015-12-29
    run_hadoop $1 2015-12-30
    run_hadoop $1 2015-12-31
    run_hadoop $1 2016-01-01
    run_hadoop $1 2016-01-02
    run_hadoop $1 2016-01-03
    run_hadoop $1 2016-01-04
    run_hadoop $1 2016-01-05
    run_hadoop $1 2016-01-06
    run_hadoop $1 2016-01-07
    run_hadoop $1 2015-12-15
    run_hadoop $1 2015-12-16
    run_hadoop $1 2015-12-17
    run_hadoop $1 2015-12-18
    run_hadoop $1 2015-12-19
    run_hadoop $1 2015-12-20
    run_hadoop $1 2015-12-21
    run_hadoop $1 2015-12-22
    run_hadoop $1 2015-12-23
    run_hadoop $1 2015-12-24
    run_hadoop $1 2015-12-25
    run_hadoop $1 2015-12-26
    run_hadoop $1 2015-12-27
    run_hadoop $1 2015-12-28
    run_hadoop $1 2015-12-29
    run_hadoop $1 2015-12-30
    run_hadoop $1 2015-12-31
    run_hadoop $1 2016-01-01
    run_hadoop $1 2016-01-02
    run_hadoop $1 2016-01-03
    run_hadoop $1 2016-01-04
    run_hadoop $1 2016-01-05
    run_hadoop $1 2016-01-06
    run_hadoop $1 2016-01-07
}

rm -rf $OUTPUT_PATH

run_domain ebola &
run_domain movies &

sleep 1
echo "Waiting analysis finish..."
wait
echo "done."
