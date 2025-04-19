#!/usr/bin/env python
from testme import TestMe
import json
import unittest


class MyTest(TestMe):

    def evaluate(self, data, gold, max_diff: float, grid_name: str = 'fourroom'):
        self.run_submission(data=data, command=f'bash run.sh /input /output --grid_name {grid_name}')
        with self.ARGS.output.joinpath('output.json').open() as f:
            pred = json.load(f)
        with gold.joinpath('output.json').open() as f:
            gold = json.load(f)
        with self.subTest(msg='Receiver policy'):
            self.assertEqual(pred['receiver_policy'], gold['receiver_policy'])
        with self.subTest(msg='Sender policy'):
            self.assertEqual(pred['sender_policy'], gold['sender_policy'])
        with self.subTest(msg='Training reward'):
            self.assertAlmostEqual(pred['rtrain'], gold['rtrain'], max_diff)
        with self.subTest(msg='Test reward'):
            self.assertAlmostEqual(pred['rtest'], gold['rtest'], max_diff)

    def test_public(self):
        self.evaluate(self.ARGS.data, self.ARGS.gold, max_diff=0.01, grid_name='fourroom')

    @unittest.skip('This is run during official eval only')
    def test_maze(self):
        self.evaluate(self.ARGS.private.joinpath('maze', 'data'), self.ARGS.private.joinpath('maze', 'gold'), max_diff=0.01, grid_name='maze')

    def test_empty(self):
        self.evaluate(self.ARGS.private.joinpath('empty', 'data'), self.ARGS.private.joinpath('empty', 'gold'), max_diff=0.01, grid_name='empty')


if __name__ == '__main__':
    MyTest.autorun()
