#!/usr/bin/env python
import os
import bz2
import sys
import json
import itertools
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('dinput')
parser.add_argument('doutput')
parser.add_argument('dgold')
parser.add_argument('deval')
args = parser.parse_args()


res = []
with bz2.open(os.path.join(args.doutput, 'output.json.bz2')) as f:
    pred = json.load(f)
with bz2.open(os.path.join(args.dgold, 'test.json.bz2')) as f:
    gold = json.load(f)


r = 0
errors = []
for p, g in itertools.zip_longest(pred, gold):
    errors.append(dict(
        round=r,
        gold=g,
        pred=p,
        correct=g == p,
    ))

with open(os.path.join(args.deval, 'eval.json'), 'wt') as f:
    json.dump(errors, f, indent=2)
print(sum(e['correct'] for e in errors) / len(errors))
