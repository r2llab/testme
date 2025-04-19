import os
import bz2
import json
import math
import re
from collections import Counter, defaultdict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def word_tokenize(sentence):
    return [x for x in re.split(r'([.,!?]+)?\s+', sentence.lower()) if x]


class NaiveBayes:

    def __init__(self, class_priors=None):
        # key: class label, value: counts of (class)
        self.class_priors = Counter()
        # a dictionary of key: class_label, value: inner dict
        # where each inner dict has key: token id, value: counts of (token id | class)
        self.conditionals = defaultdict(Counter)

    def save(self, dout):
        """
        Save necessary states to the output directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'wt') as f:
            json.dump(dict(
                class_priors=self.class_priors,
                conditionals=self.conditionals,
            ), f)

    @classmethod
    def load(cls, dout):
        """
        Loads NB model from directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'rt') as f:
            d = json.load(f)
        nb = cls()
        nb.class_priors.update(d['class_priors'])
        for k, v in d['conditionals'].items():
            nb.conditionals[k].update(v)
        return nb

    @classmethod
    def preprocess(cls, dataset: list, stop_words: set, text_key: str = 'text', tokens_key: str = 'tokens'):
        for ex in dataset:
            ex[tokens_key] = [t for t in word_tokenize(ex[text_key]) if t not in stop_words]

    def train(self, data: list):
        """
        Train from a list of examples
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def predict(self, data: list) -> list:
        """
        Predict labels for a list of examples. Remember to apply Laplace smoothing.
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    parser.add_argument('--train', action='store_true', help='train the model')
    parser.add_argument('--dcheckpoint', help='directory to save checkpoint', default=os.getcwd())
    args = parser.parse_args()

    with bz2.open(os.path.join(args.dinput, 'stop_words.json.bz2'), 'rt') as f:
        stop_words = set(json.load(f))

    data = {}
    splits = ['test']
    if args.train:
        splits.extend(['train', 'val'])
    for split in splits:
        fname = os.path.join(args.dinput, f'{split}.json.bz2')
        if os.path.isfile(fname):
            print(f'Loading {fname}')
            with bz2.open(fname, 'rt') as f:
                data[split] = json.load(f)
                NaiveBayes.preprocess(data[split], stop_words)

    if args.train:
        nb = NaiveBayes()
        nb.train(data['train'])
        nb.save(args.dcheckpoint)

    nb = NaiveBayes.load(args.dcheckpoint)

    if args.train:
        pred = nb.predict(data['val'])
        correct = sum(p == ex['label'] for ex, p in zip(data['val'], pred))
        total = len(data["val"])
        print(f'Validation accuracy: {correct} / {total} = {correct/total}')

    pred = nb.predict(data['test'])
    print('Making predictions on test')
    with bz2.open(os.path.join(args.doutput, 'output.json.bz2'), 'wt') as f:
        json.dump(pred, f, indent=2)
