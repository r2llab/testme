#!/usr/bin/env bash
set -e
set -x

python grade.py /output/output.txt /gold/gold.txt > /eval/eval.txt
