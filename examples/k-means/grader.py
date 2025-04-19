#!/usr/bin/env python
import bz2
import json
import unittest
import itertools
from testme import TestMe


class MyTest(TestMe):

    def evaluate(self, data, gold, min_acc: float):
        self.run_submission(data=data)
        with bz2.open(self.ARGS.output.joinpath('output.json.bz2')) as f:
            pred = json.load(f)
        with bz2.open(gold.joinpath('test.json.bz2')) as f:
            gold = json.load(f)

        num_clusters = max(gold)
        best_acc = 0
        best_gold = None

        for mapping in itertools.permutations(list(range(num_clusters+1))):
            gold_relabeled = [mapping[i] for i in gold]
            correct = [g == p for g, p in itertools.zip_longest(gold_relabeled, pred)]
            acc = sum(correct) / len(correct)
            if acc > best_acc:
                best_gold = gold_relabeled
                best_acc = acc
        self.assertGreaterEqual(best_acc, min_acc)

    def test_public(self):
        self.evaluate(self.ARGS.data, self.ARGS.gold, min_acc=0.83)

    @unittest.skip('This is run during official eval only')
    def test_private(self):
        self.evaluate(self.ARGS.private.joinpath('in_dist', 'data'), self.ARGS.private.joinpath('in_dist', 'gold'), min_acc=0.80)


if __name__ == '__main__':
    MyTest.autorun()
