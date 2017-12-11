#!/usr/bin/env bash

echo $(($(fastq_quality_filter -i test.fastq -q 20 -p 90 -Q 33 | wc -l) / 4))
