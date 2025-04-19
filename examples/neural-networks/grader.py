#!/usr/bin/env python
from testme import TestMe
import bz2
import json
import unittest


class MyTest(TestMe):

    def evaluate(self, data, gold, max_mse: float, command='bash run.sh /input /output'):
        self.run_submission(data=data, command=command)
        with bz2.open(self.ARGS.output.joinpath('output.json.bz2')) as f:
            pred = json.load(f)
        with bz2.open(gold.joinpath('test.json.bz2')) as f:
            gold = json.load(f)
        mse = sum((p - g)**2 for p, g in zip(pred, gold)) / len(gold)
        self.assertLessEqual(mse, max_mse)

    def test_public(self):
        self.evaluate(self.ARGS.data, self.ARGS.gold, max_mse=1.7)

    @unittest.skip('This is run during official eval only')
    def test_in_dist_private(self):
        self.evaluate(self.ARGS.private.joinpath('in_dist', 'data'), self.ARGS.private.joinpath('in_dist', 'gold'), max_mse=1.8)


if __name__ == '__main__':
    MyTest.autorun()
