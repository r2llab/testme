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


res = []
for test in ['bfs', 'dfs', 'lowest_cost_first', 'astar']:
    with open(os.path.join(args.doutput, f'{test}.json')) as f:
        pred = json.load(f)
    with open(os.path.join(args.dgold, f'{test}.json')) as f:
        gold = json.load(f)
    res.append(dict(test=test, correct=pred == gold, pred=', '.join(pred), gold=', '.join(gold)))

with open(os.path.join(args.deval, 'eval.json'), 'wt') as f:
    json.dump(res, f, indent=2)
