#!/usr/bin/env python
import os
import json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('dinput')
parser.add_argument('doutput')
parser.add_argument('dgold')
parser.add_argument('deval')
args = parser.parse_args()


with open(os.path.join(args.doutput, 'tree.json')) as f:
    pred = json.load(f)
with open(os.path.join(args.dgold, 'tree.json')) as f:
    gold = json.load(f)
with open(os.path.join(args.deval, 'tree_eval.json'), 'wt') as f:
    json.dump(dict(
        gold=gold,
        learned=pred,
        correct=gold == pred,
    ), f, indent=2)

with open(os.path.join(args.doutput, 'output.json')) as f:
    pred = json.load(f)
with open(os.path.join(args.dgold, 'output.json')) as f:
    gold = json.load(f)
with open(os.path.join(args.deval, 'pred_eval.json'), 'wt') as f:
    json.dump(dict(
        gold=gold,
        learned=pred,
        correct=gold == pred,
    ), f, indent=2)
