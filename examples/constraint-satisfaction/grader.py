#!/usr/bin/env python
from testme import TestMe
import json


class MyTest(TestMe):

    def test_public(self):
        self.run_submission()
        with self.ARGS.output.joinpath('output.json').open() as f:
            pred = json.load(f)
        with self.ARGS.gold.joinpath('output.json').open() as f:
            gold = json.load(f)
        self.assertDictEqual(gold, pred)


if __name__ == '__main__':
    MyTest.autorun()
