#!/usr/bin/env python
import json
from testme import TestMe


class MyTest(TestMe):

    def test_public(self):
        self.run_submission()
        with self.ARGS.output.joinpath('tree.json').open() as f:
            pred = json.load(f)
        with self.ARGS.gold.joinpath('tree.json').open() as f:
            gold = json.load(f)

        with self.subTest(msg='Tree learning'):
            self.assertDictEqual(gold, pred)

        with self.ARGS.output.joinpath('pred.json').open() as f:
            pred = json.load(f)
        with self.ARGS.gold.joinpath('pred.json').open() as f:
            gold = json.load(f)

        with self.subTest(msg='Prediction'):
            self.assertListEqual(gold, pred)


if __name__ == '__main__':
    MyTest.autorun()
