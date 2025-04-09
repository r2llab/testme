#!/usr/bin/env bash
set -x
set -e

rm -rf submit submit.zip
mkdir -p submit

# Add files you want to submit
cp Dockerfile submit
cp myprogram.py submit
cp run.sh submit
cp user.txt submit
cp state.json.bz2 submit

# make zip file
zip -r submit.zip submit
