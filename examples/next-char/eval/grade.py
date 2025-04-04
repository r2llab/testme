#!/usr/bin/env python
import os
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('dinput')
parser.add_argument('doutput')
parser.add_argument('dgold')
parser.add_argument('deval')
args = parser.parse_args()


def load_pred(fname, force_limit=None):
    with open(fname) as f:
        loaded = []
        for line in f:
            line = line[:-1].lower()
            if force_limit is not None:
                line = line[:force_limit]
            loaded.append(line)
        return loaded


pred = load_pred(os.path.join(args.doutput, 'output.txt'), force_limit=3)
gold = load_pred(os.path.join(args.dgold, 'gold.txt'))

if len(pred) < len(gold):
    pred.extend([''] * (len(gold) - len(pred)))

res = []
correct = 0
for i, (p, g) in enumerate(zip(pred, gold)):
    right = g in p
    correct += right
    res.append('Input {}: {}, {} is {} in {}'.format(i, 'right' if right else 'wrong', g, 'in' if right else 'not in', p))
res.append('Success rate: {}'.format(correct/len(gold)))
with open(os.path.join(args.deval, 'eval.txt'), 'wt') as f:
    for line in res:
        f.write(line + '\n')
