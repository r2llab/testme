#!/usr/bin/env bash
set -e
set -x

python grade.py $@ > /eval/eval.txt
