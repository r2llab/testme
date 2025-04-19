#!/usr/bin/env python
from testme import TestMe
import bz2
import json
import unittest


class MyTest(TestMe):

    def evaluate(self, data, gold, min_acc: float):
        self.run_submission(data=data)
        with bz2.open(self.ARGS.output.joinpath('output.json.bz2')) as f:
            pred = json.load(f)
        with bz2.open(gold.joinpath('test.json.bz2')) as f:
            gold = json.load(f)
        acc = sum(p == g for p, g in zip(pred, gold)) / len(gold)
        self.assertGreaterEqual(acc, min_acc)

    def test_public(self):
        self.evaluate(self.ARGS.data, self.ARGS.gold, min_acc=0.8)

    @unittest.skip('This is run during official eval only')
    def test_in_dist_private(self):
        self.evaluate(self.ARGS.private.joinpath('in_dist', 'data'), self.ARGS.private.joinpath('in_dist', 'gold'), min_acc=0.80)

    @unittest.skip('This is run during official eval only')
    def test_out_dist_private(self):
        self.evaluate(self.ARGS.private.joinpath('out_dist', 'data'), self.ARGS.private.joinpath('out_dist', 'gold'), min_acc=0.65)


if __name__ == '__main__':
    MyTest.autorun()
