#!/usr/bin/env python
import os
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
with open(os.path.join(args.doutput, 'output.json')) as f:
    pred = json.load(f)
with open(os.path.join(args.dgold, 'output.json')) as f:
    gold = json.load(f)


round = 0
errors = []
for p, g in itertools.zip_longest(pred, gold):
    round += 1
    errors.append(dict(
        round=round,
        gold=gold,
        pred=pred,
        correct=gold == pred,
    ))

with open(os.path.join(args.deval, 'eval.json'), 'wt') as f:
    json.dump(errors, f, indent=2)
