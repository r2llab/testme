#!/usr/bin/env python
from testme import TestMe
import json
import unittest


class MyTest(TestMe):

    def evaluate(self, data, gold, output):
        self.run_submission(data=data, output=output)
        for test in ['bfs', 'dfs', 'lowest_cost_first', 'astar']:
            with output.joinpath(f'{test}.json').open() as f:
                pred = json.load(f)
            with gold.joinpath(f'{test}.json').open() as f:
                ground_truth = json.load(f)
            with self.subTest(msg=test):
                self.assertListEqual(pred, ground_truth)

    def test_public(self):
        self.evaluate(self.ARGS.data, self.ARGS.gold, output=self.ARGS.output.joinpath('public'))

    @unittest.skip('This is run during official eval only')
    def test_private(self):
        for i in range(3):
            name = f'query_{i}'
            with self.subTest(msg=name):
                output = self.ARGS.output.joinpath(name)
                dprivate = self.ARGS.private.joinpath(name)
                self.evaluate(dprivate.joinpath('data'), dprivate.joinpath('gold'), output=output)


if __name__ == '__main__':
    MyTest.autorun()
